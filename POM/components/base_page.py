from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

GLOBAL_TIMEOUT = 1


class BasePage:
    def __init__(self, driver, debug=False):
        self.driver = driver
        self.highlight = debug

    def load(self, url):
        self.driver.get(url)

    def wait_until_element_is_visible(self, locator, timeout=GLOBAL_TIMEOUT):
        by_locator = self.__get_by_locator(locator)
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator=by_locator))

    def wait_until_element_is_not_visible(self, locator, timeout=GLOBAL_TIMEOUT):
        by_locator = self.__get_by_locator(locator)
        WebDriverWait(self.driver, timeout).until_not(EC.visibility_of_element_located(locator=by_locator))

    def wait_until_page_contains_element(self, locator, timeout=GLOBAL_TIMEOUT):
        by_locator = self.__get_by_locator(locator)
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator=by_locator))

    def wait_until_page_does_not_contains_element(self, locator, timeout=GLOBAL_TIMEOUT):
        by_locator = self.__get_by_locator(locator)
        WebDriverWait(self.driver, timeout).until_not(EC.presence_of_element_located(locator=by_locator))

    def get_webelement(self, locator):
        by_locator = self.__get_by_locator(locator)
        element = self.driver.find_element(by=by_locator[0], value=by_locator[1])
        self.highlight_element(element)
        return element

    def get_webelements(self, locator):
        by_locator = self.__get_by_locator(locator)
        return self.driver.find_elements(by=by_locator[0], value=by_locator[1])

    def click_element(self, locator):
        element = self.__ensure_locator_is_webelement(locator)
        element.click()

    def input_text(self, locator, text):
        element = self.__ensure_locator_is_webelement(locator)
        element.send_keys(text)

    def get_text(self, locator):
        return self.__ensure_locator_is_webelement(locator).text

    def get_title(self):
        return self.driver.title

    def get_location(self):
        return self.dirver.current_url

    def go_to(self, page_url):
        self.driver.maximize_window()
        self.driver.get(page_url)

    def __get_by_locator(self, locator):
        fromIndex = 0
        toIndex = len(locator)
        by = By.XPATH
        if locator.lower().startswith("xpath"):
            fromIndex = len("xpath") + 1
            by = By.XPATH
        elif locator.lower().startswith("id"):
            fromIndex = len("id") + 1
            by = By.ID
        result = locator[fromIndex:toIndex]
        return (by, result)

    def new_tab(self, link):
        self.driver.execute_script(f"window.open('{link}','_blank');")

    def switch_to_tab(self, tab_index):
        tab = self.driver.window_handles[tab_index]
        self.driver.switch_to.window(tab)

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    def double_click_element(self, locator):
        element = self.__ensure_locator_is_webelement(locator)
        self.click_element(element)
        self.click_element(element)

    def get_browser_cookies(self):
        return self.driver.get_cookies()

    def get_browser_cookie(self, name):
        return self.driver.get_cookie(name)

    def get_attribute(self, locator, attribute):
        element = self.__ensure_locator_is_webelement(locator)
        return element.get_attribute(attribute)

    def scroll_element_into_view(self, locator):
        element = self.__ensure_locator_is_webelement(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def hover_element(self, locator):
        element = self.__ensure_locator_is_webelement(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def sleep(self, secs: float):
        time.sleep(secs)

    def __ensure_locator_is_webelement(self, locator):
        if isinstance(locator, str):
            return self.get_webelement(locator)
        return locator

    def highlight_element(self, element, effect_time=0.05, color="red", border=5):
        if self.highlight:
            driver = self.driver

            def apply_style(s):
                driver.execute_script(
                    "arguments[0].setAttribute('style', arguments[1]);",
                    element,
                    s,
                )

            original_style = element.get_attribute("style")
            apply_style("border: {0}px solid {1}; padding:{2}px".format(border, color, 5))
            time.sleep(effect_time)
            apply_style(original_style)
