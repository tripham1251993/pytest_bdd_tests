from pom.components.base_page import BasePage, GLOBAL_TIMEOUT
from resources import locators_manager


LOCATORS = locators_manager.get_locators("login_page")


class LoginPage(BasePage):
    def __init__(self, driver, debug=False):
        super().__init__(driver, debug)

    USERNAME_INPUT = LOCATORS.get("USERNAME_INPUT")
    PASSWORD_INPUT = LOCATORS.get("PASSWORD_INPUT")
    LOGIN_BUTTON = LOCATORS.get("LOGIN_BUTTON")
    VALIDATE_MESSAGE = LOCATORS.get("VALIDATE_MESSAGE")

    def wait_until_page_contains_username_input(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.USERNAME_INPUT, timeout)

    def wait_until_page_contains_password_input(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.PASSWORD_INPUT, timeout)

    def wait_until_page_contains_login_button(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.LOGIN_BUTTON, timeout)

    def wait_until_page_contains_validate_message(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.VALIDATE_MESSAGE, timeout)

    def wait_until_page_does_not_contain_username_input(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.USERNAME_INPUT, timeout)

    def wait_until_page_does_not_contain_password_input(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.PASSWORD_INPUT, timeout)

    def wait_until_page_does_not_contain_login_button(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.LOGIN_BUTTON, timeout)

    def wait_until_page_does_not_contain_validate_message(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.VALIDATE_MESSAGE, timeout)

    def wait_until_username_input_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.USERNAME_INPUT, timeout)

    def wait_until_password_input_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.PASSWORD_INPUT, timeout)

    def wait_until_login_button_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.LOGIN_BUTTON, timeout)

    def wait_until_validate_message_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.VALIDATE_MESSAGE, timeout)

    def wait_until_username_input_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.USERNAME_INPUT, timeout)

    def wait_until_password_input_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.PASSWORD_INPUT, timeout)

    def wait_until_login_button_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.LOGIN_BUTTON, timeout)

    def wait_until_validate_message_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.VALIDATE_MESSAGE, timeout)

    def click_on_username_input(self):
        self.click_element(self.USERNAME_INPUT)

    def click_on_password_input(self):
        self.click_element(self.PASSWORD_INPUT)

    def click_on_login_button(self):
        self.click_element(self.LOGIN_BUTTON)

    def click_on_validate_message(self):
        self.click_element(self.VALIDATE_MESSAGE)

    def hover_on_username_input(self):
        self.hover_element(self.USERNAME_INPUT)

    def hover_on_password_input(self):
        self.hover_element(self.PASSWORD_INPUT)

    def hover_on_login_button(self):
        self.hover_element(self.LOGIN_BUTTON)

    def hover_on_validate_message(self):
        self.hover_element(self.VALIDATE_MESSAGE)

    def scroll_username_input_into_view(self):
        self.hover_element(self.USERNAME_INPUT)

    def scroll_password_input_into_view(self):
        self.hover_element(self.PASSWORD_INPUT)

    def scroll_login_button_into_view(self):
        self.hover_element(self.LOGIN_BUTTON)

    def scroll_validate_message_into_view(self):
        self.hover_element(self.VALIDATE_MESSAGE)

    def enter_text_on_username_input(self, value):
        self.input_text(self.USERNAME_INPUT, value)

    def enter_text_on_password_input(self, value):
        self.input_text(self.PASSWORD_INPUT, value)

    def enter_text_on_login_button(self, value):
        self.input_text(self.LOGIN_BUTTON, value)

    def enter_text_on_validate_message(self, value):
        self.input_text(self.VALIDATE_MESSAGE, value)

    def get_username_input_text(self):
        return self.get_text(self.USERNAME_INPUT)

    def get_password_input_text(self):
        return self.get_text(self.PASSWORD_INPUT)

    def get_login_button_text(self):
        return self.get_text(self.LOGIN_BUTTON)

    def get_validate_message_text(self):
        return self.get_text(self.VALIDATE_MESSAGE)
