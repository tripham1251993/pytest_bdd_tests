from pom.components.base_page import BasePage, GLOBAL_TIMEOUT
from resources import locators_manager


LOCATORS = locators_manager.get_locators("user_management_page")


class UserManagementPage(BasePage):
    def __init__(self, driver, debug=False):
        super().__init__(driver, debug)

    USERNAME_INPUT = LOCATORS.get("USERNAME_INPUT")

    def wait_until_page_contains_username_input(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.USERNAME_INPUT, timeout)

    def wait_until_page_does_not_contain_username_input(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.USERNAME_INPUT, timeout)

    def wait_until_username_input_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.USERNAME_INPUT, timeout)

    def wait_until_username_input_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.USERNAME_INPUT, timeout)

    def click_on_username_input(self):
        self.click_element(self.USERNAME_INPUT)

    def hover_on_username_input(self):
        self.hover_element(self.USERNAME_INPUT)

    def scroll_username_input_into_view(self):
        self.hover_element(self.USERNAME_INPUT)

    def enter_text_on_username_input(self, value):
        self.input_text(self.USERNAME_INPUT, value)

    def get_username_input_text(self):
        return self.get_text(self.USERNAME_INPUT)
