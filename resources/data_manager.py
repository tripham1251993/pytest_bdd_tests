from core_lib import utilities as util
import os

dir_name = os.path.dirname(__file__).replace("resources", "")
LOCATOR_MAP = {
    "common_data": f"{dir_name}{os.sep}data{os.sep}e2e{os.sep}common_data.yaml",
    "login_data": f"{dir_name}{os.sep}data{os.sep}e2e{os.sep}login_data.yaml",
}


def get_data(data_name: str):
    return util.read_yaml(LOCATOR_MAP.get(data_name.lower()))
