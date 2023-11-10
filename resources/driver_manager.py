from selenium import webdriver

# Google Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Firefox
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

# Microsoft Edge
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import os
import sys

# config windows size for firefox
os.environ["MOZ_HEADLESS_WIDTH"] = "1920"
os.environ["MOZ_HEADLESS_HEIGHT"] = "1080"


class DriverManager:
    def __init__(self, browser, headless=False):
        if browser == "chrome":
            self.driver = self.__get_chromedriver(headless)
        elif browser == "firefox":
            self.driver = self.__get_firefoxdriver(headless)
        elif browser == "edge":
            self.driver = self.__get_edgedriver(headless)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def __get_chromedriver(self, headless=False):
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")
        path = ChromeDriverManager().install()
        sys.path.append(path)
        return webdriver.Chrome(
            service=ChromeService(path),
            options=options,
        )

    def __get_firefoxdriver(self, headless=False):
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
        path = GeckoDriverManager().install()
        sys.path.append(path)
        return webdriver.Firefox(
            service=FirefoxService(path),
            options=options,
        )

    def __get_edgedriver(self, headless=False):
        options = EdgeOptions()
        if headless:
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")
        path = EdgeChromiumDriverManager().install()
        sys.path.append(path)
        return webdriver.Edge(
            service=EdgeService(path),
            options=options,
        )
