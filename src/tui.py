import src.game_elements as game
import time

from selenium.webdriver.common.by import By

def load_room(driver):
    driver.get("https://jklm.fun")

    print("To start the script, either enter a room code or manually navigate to a room in the opened browser and click enter.")
    option = input("Room code/Confirmation: ")

    mode = input("What mode would you like to play in (rage/legit) - defaults to legit")
    if mode != "rage":
        mode = "legit"

    if option != "":
        driver.get(f"https://jklm.fun/{option}")


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

def playing_game(driver):
    game.play(driver)
