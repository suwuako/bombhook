import pathlib
import sys
import asyncio

import src.tui as tui

from selenium import webdriver
from selenium.webdriver.firefox.service import Service


class start():
    def __init__(self):
        windows = ["win32"]
        linux = ["linux", "linux2"]
        platform = sys.platform

        path = pathlib.Path().absolute()

        if platform in windows:
            driver = fr"{path}\external\geckodriver.exe"
        elif platform in linux:
            driver = fr"{path}.external.geckodriver"
        else:
            driver = fr"{path}.external.geckodriver"

        self.driver = webdriver.Firefox(service=Service(driver))

    def run(self):
        tui.load_room(self.driver)
        tui.in_game(self.driver)
        tui.playing_game(self.driver)


if __name__ == "__main__":
    start = start()
    start.run()