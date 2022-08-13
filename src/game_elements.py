import selenium
import time
import random

import src.lib as lib

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

def can_join(driver):
    return driver.find_element(By.CLASS_NAME, "join").is_displayed()

def write_input(driver, word, mode):
    input_box_xpath = "/html/body/div[2]/div[3]/div[2]/div[2]/form/input"
    input_box = driver.find_element(By.XPATH, input_box_xpath)

    if mode == "rage":
        input_box.send_keys(word)
        time.sleep(0.05)
        input_box.send_keys(Keys.RETURN)
        time.sleep(0.35)
        return

    elif mode == "legit":
        for letter in word:
            input_box.send_keys(letter)
            waittime = random.randint(10000,20000) * 0.00001

            time.sleep(waittime)
        input_box.send_keys(Keys.RETURN)
        time.sleep(0.35)
        return

def play(driver, wl):
    wordlist = wl
    print(wordlist)
    unused_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                      'U', 'V', 'W', 'X', 'Y', 'Z']
    syllable = "BRUHBRUHBRUHTHISWILLBRUHBRUHBRUH"
	# TODO: rewrite this poopy fart
    while True:
        selfturn = your_turn(driver)
        while selfturn == True:
            syllable = get_syllable(driver)
            print(f"The current syllable is {syllable}.")
            usable_words = lib.find_usable_words(driver, wordlist)
            best_word = lib.find_best_word(usable_words, unused_letters)
            print(best_word)
            print(f"Unused words: {unused_letters}")

            write_input(driver, best_word, "rage")

            index = 0
            for i in wordlist:
                if i == best_word:
                    print(f"removing {wordlist[index]} from current wordlist")
                    wordlist.pop(index)

                index += 1
            selfturn = your_turn(driver)

            for letter in unused_letters:
                if letter in best_word:
                    unused_letters.remove(letter)

            if unused_letters == []:
                unused_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                                  'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
