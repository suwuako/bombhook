import selenium
import time
import random

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def get_syllable(driver):
    class_name = "syllable"

    try:
        content = driver.find_element(By.CLASS_NAME, class_name)
        # .lower is used because wordlist is in lowercase
        return content.text
    except selenium.common.exceptions.NoSuchElementException:
        return False


# Bombparty attempts to make an "anticheat" by using an iframe but they underestimate my autism and dedication
def switch_to_iframe(driver):
    kill = False
    while True:
        time.sleep(1)
        try:
            # There is only one iframe element as of 7/11/2022
            game = driver.find_element(By.TAG_NAME, "iframe")
            driver.switch_to.frame(game)
            print("successfully switched to iframe!")
            kill = True

        except:
            pass

        if kill:
            return

def load_rules(driver):
    # TODO: load in roundtimes and other rules that dont use classes
    rules = dict()

    rules["starting_lives"] = int(driver.find_element(By.CLASS_NAME, "starting").get_attribute('value'))
    rules["max_lives"] = int(driver.find_element(By.CLASS_NAME, "max").get_attribute('value'))

    return rules

def your_turn(driver):
    return driver.find_element(By.CLASS_NAME, "selfTurn").is_displayed()

def find_best_word(usable_words, unused_letters):
    word_ranking = {}
    for word in usable_words:
        used_letters = []
        for letter in unused_letters:
            if letter in word and letter not in used_letters:
                used_letters.append(letter)

        word_ranking[word] = used_letters

    highest_letter_len = 0
    best_words = []
    for word, letters in word_ranking.items():
        if len(letters) > highest_letter_len:
            best_words = [word]
            highest_letter_len = len(letters)

        if len(letters) >= highest_letter_len:
            best_words.append(word)

    print(f"The best word(s) we can use is {best_words} with {highest_letter_len} letters")
    return random.choice(best_words)

def find_usable_words(driver, wordlist):
    usable_words = []
    syllable = get_syllable(driver)
    for i in wordlist:
        if syllable in i:
            usable_words.append(i)

    return usable_words

def play(driver, wl):
    wordlist = wl
    print(wordlist)
    unused_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                      'U', 'V', 'W', 'X', 'Y', 'Z']
    syllable = "BRUHBRUHBRUHTHISWILLBRUHBRUHBRUH"

    while True:
        if syllable != get_syllable(driver):
            syllable = get_syllable(driver)
            print(f"The current syllable is {syllable}.")
            usable_words = find_usable_words(driver, wordlist)
            best_word = find_best_word(usable_words, unused_letters)
            print(best_word)

        selfturn = your_turn(driver)
        if selfturn == True:
            input_box_xpath = "/html/body/div[2]/div[3]/div[2]/div[2]/form/input"

            input_box = driver.find_element(By.XPATH, input_box_xpath)
            input_box.send_keys(best_word)
            time.sleep(0.05)
            input_box.send_keys(Keys.RETURN)
            time.sleep(0.3)

            index = 0
            for i in wordlist:
                if i == best_word:
                    print(f"removing {wordlist[index]} from current wordlist")
                    wordlist.pop(index)

                index += 1

            for letter in unused_letters:
                if letter in best_word:
                    unused_letters.remove(letter)

        else:
            pass

        if unused_letters == []:
            unused_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                              'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']