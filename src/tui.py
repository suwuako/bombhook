import src.game_elements as game
import time

from selenium.webdriver.common.by import By

def load_room(driver):
    # remove this after testing
    '''
    driver.get("https://jklm.fun")

    print("To start the script, either enter a room code or manually navigate to a room in the opened browser and click enter.")
    option = input("Room code/Confirmation")

    if option != "":
        driver.get(f"https://jklm.fun/{option}")
    '''

    driver.get("https://jklm.fun/qpet")

def in_game(driver):
    print("Looks like we successfully joined a room. Checking if game is in progress...")

    # switch to game frame
    game.switch_to_iframe(driver)
    print("loading rules...")
    while True:
        try:
            ruleset = game.load_rules(driver)

            if ruleset["starting_lives"] and ruleset["max_lives"] != None or "":
                break
        except:
            pass

    print("Ruleset successfully loaded!")
    print(
f"""starting_lives : {ruleset["starting_lives"]}
max_lives : {ruleset["max_lives"]}""")

    print("I haven't coded in auto-join and other functionalities, so press enter when you're in a game.")
    input()

def playing_game(driver):
    syllable = None
    selfturn = None
    while True:
        if selfturn != game.your_turn:
            print("")
        selfturn = game.your_turn(driver)
        if selfturn = True:


        if syllable != game.get_syllable(driver):
            syllable = game.get_syllable(driver)
            print(f"The current syllable is {syllable}")