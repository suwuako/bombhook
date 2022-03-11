import pathlib
import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
        self.driver.get("https://jklm.fun/")
        # Wait for user to join game room
        input("Press enter after selecting your game room: ")



if __name__ == "__main__":
    start = start()
    start.run()