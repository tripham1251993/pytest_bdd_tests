from core_lib import utilities as util
import os

dir_name = os.path.dirname(__file__).replace("resources", "")
base_path = os.path.join(dir_name, "locators")
LOCATOR_MAP = {
    "login_page": os.path.join(base_path, "login_page.yaml"),
    "main_menu": os.path.join(base_path, "main_menu.yaml"),
    "user_management_page": os.path.join(base_path, "user_management_page.yaml"),
}


def get_locators(page_name: str):
    return util.read_yaml(LOCATOR_MAP.get(page_name.lower()))
