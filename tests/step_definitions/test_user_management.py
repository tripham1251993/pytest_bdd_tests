from pytest_bdd import scenarios, then
from pom.pages.user_management_page import UserManagementPage
import pytest

scenarios("../features/user_management.feature")


@pytest.fixture
def user_management_page(driver):
    page = UserManagementPage(driver)
    yield page


@then("User should see Username input")
def username_input_should_be_visible(user_management_page):
    user_management_page.wait_until_username_input_is_visible()
