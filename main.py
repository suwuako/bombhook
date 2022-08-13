import pathlib
import sys
import asyncio

import src.tui as tui
import src.game_elements as game

from selenium import webdriver
from selenium.webdriver.firefox.service import Service


class start():
    def __init__(self):
        windows = ["win32"]
        linux = ["linux", "linux32", "linux2"]
        platform = sys.platform

        path = pathlib.Path().absolute()

        if platform in windows:
            driver = fr"{path}\external\geckodriver.exe"
            wordlist = open(f"{path}\external\wordlist", "r")
        elif platform in linux:
            driver = fr"{path}/external/geckodriver"
            wordlist = open(f"{path}/external/wordlist", "r")
        else:
            driver = fr"{path}/external/geckodriver"
            wordlist = open(f"{path}/external/wordlist", "r")

        self.driver = webdriver.Firefox(service=Service(driver))
        self.wordlist = []

        lines = wordlist.readlines()
        for i in lines:
            self.wordlist.append(i.replace("\n", ""))

        del(wordlist)

    def run(self):
        tui.load_room(self.driver)
        tui.in_game(self.driver)
        game.play(self.driver, self.wordlist)


if __name__ == "__main__":
    start = start()
    start.run()
