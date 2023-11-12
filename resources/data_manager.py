from core_lib import utilities as util
import os

dir_name = os.path.dirname(__file__).replace("resources", "")
data_path = os.path.join(dir_name, "data", "e2e")
LOCATOR_MAP = {
    "common_data": os.path.join(data_path, "common_data.yaml"),
    "login_data": os.path.join(data_path, "login_data.yaml"),
}


def get_data(data_name: str):
    return util.read_yaml(LOCATOR_MAP.get(data_name.lower()))
