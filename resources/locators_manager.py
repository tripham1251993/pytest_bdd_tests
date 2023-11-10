from core_lib import utilities as util
import os

dir_name = os.path.dirname(__file__).replace("resources", "")
LOCATOR_MAP = {
    "login_page": f"{dir_name}{os.sep}locators{os.sep}login_page.yaml",
    "main_menu": f"{dir_name}{os.sep}locators{os.sep}main_menu.yaml",
    "user_management_page": (f"{dir_name}{os.sep}locators{os.sep}user_management_page.yaml"),
}


def get_locators(page_name: str):
    return util.read_yaml(LOCATOR_MAP.get(page_name.lower()))
