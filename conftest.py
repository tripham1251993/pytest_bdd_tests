from pytest_bdd import given, when, parsers
from resources.driver_manager import DriverManager
from resources import data_manager
from pom.components.base_page import BasePage
from pom.pages.login_page import LoginPage
from pom.components.main_menu import MainMenu
import allure
import pytest


# BROWSER = "chrome"
COMMON_DATA = data_manager.get_data("common_data")
LOGIN_DATA = data_manager.get_data("login_data")
ERROR_STEPS = {}


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser name that you want to run on [chorme, firefox, edge]",
    )


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture
def driver(browser):
    driver = DriverManager(browser).driver
    yield driver
    driver.quit()


@pytest.fixture
def login_page(driver):
    page = LoginPage(driver)
    yield page


@pytest.fixture
def main_menu(driver):
    page = MainMenu(driver)
    yield page


@given(parsers.parse("User navigate to {homepage}"))
def navigate_to_homepage(login_page, homepage):
    homepage = COMMON_DATA.get(homepage)
    login_page.load(homepage)


@when(parsers.parse("User enter {username} in username input"))
def enter_username(login_page, username):
    login_page.wait_until_username_input_is_visible()
    login_page.enter_text_on_username_input(LOGIN_DATA.get(username))


@when(parsers.parse("User enter {password} in password input"))
def enter_password(login_page, password):
    login_page.enter_text_on_password_input(LOGIN_DATA.get(password))


@when("User click login button")
def click_login_button(login_page):
    login_page.click_on_login_button()


@when("User click on Admin menu")
def click_admin_menu(main_menu):
    main_menu.click_on_admin_main_menu()


@when("User hover on Admin menu")
def hover_admin_menu(main_menu):
    main_menu.hover_on_admin_main_menu()


@when("User click on User Management submenu")
def click_user_management_submenu(main_menu):
    main_menu.click_on_admin_user_management_main_menu()


@when("User hover on User Management submenu")
def hover_user_management_submenu(main_menu):
    main_menu.hover_on_admin_user_management_main_menu()


@when("User click User submenu")
def click_user_submenu(main_menu):
    main_menu.click_on_admin_user_management_users()


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    for sc_step in scenario.steps:
        if sc_step.name == step.name:
            ERROR_STEPS[f"{feature.name}.{scenario.name}"] = step
            break

    for k, v in step_func_args.items():
        if isinstance(v, BasePage):
            driver = step_func_args[k].driver
    try:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="screenshot",
            attachment_type=allure.attachment_type.PNG,
        )
    except Exception as e:
        print("Fail to take screen-shot: {}".format(e))


def pytest_bdd_after_scenario(request, feature, scenario):
    print("Features: " + feature.name)
    print(" " * 2 + "Scenario: " + scenario.name)
    for step in scenario.steps:
        if ERROR_STEPS.__contains__(f"{feature.name}.{scenario.name}"):
            if step.name == ERROR_STEPS.get(f"{feature.name}.{scenario.name}").name:
                print(" " * 4 + "❌ " + f"{step.keyword} " + step.name)
                break
        print(" " * 4 + "✅ " + f"{step.keyword} " + step.name)
