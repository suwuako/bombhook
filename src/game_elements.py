import selenium
import time
from selenium.webdriver.common.by import By

def get_syllable(driver):
    class_name = "syllable"

    try:
        content = driver.find_element(By.CLASS_NAME, class_name)
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
    a = driver.find_element(By.CLASS_NAME, "selfTurn").is_displayed()
    print(f"{a} selfturn")