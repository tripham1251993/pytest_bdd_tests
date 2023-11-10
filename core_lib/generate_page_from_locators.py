import os
import sys

dir_name = os.path.dirname(__file__).replace("core_lib", "")
if dir_name[-1] == "/":
    dir_name = dir_name[:-1]
sys.path.append(dir_name)
from resources import locators_manager
from core_lib import utilities


class_template = """
from pom.components.base_page import BasePage, GLOBAL_TIMEOUT
from resources import locators_manager


LOCATORS = locators_manager.get_locators("{}")


class {}(BasePage):
    def __init__(self, driver, debug=False):
        super().__init__(driver, debug)
"""

wait_contains_template = """
    def wait_until_page_contains_{}(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.{}, timeout)
"""

wait_not_contains_template = """
    def wait_until_page_does_not_contain_{}(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.{}, timeout)
"""

wait_until_visible_template = """
    def wait_until_{}_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.{}, timeout)
"""

wait_until_not_visible_template = """
    def wait_until_{}_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.{}, timeout)
"""

click_on_element_template = """
    def click_on_{}(self):
        self.click_element(self.{})
"""

hover_on_element_template = """
    def hover_on_{}(self):
        self.hover_element(self.{})
"""

scroll_element_template = """
    def scroll_{}_into_view(self):
        self.hover_element(self.{})
"""

input_text_template = """
    def enter_text_on_{}(self, value):
        self.input_text(self.{}, value)
"""

get_text_template = """
    def get_{}_text(self):
        return self.get_text(self.{})
"""

templates = [
    wait_contains_template,
    wait_not_contains_template,
    wait_until_visible_template,
    wait_until_not_visible_template,
    click_on_element_template,
    hover_on_element_template,
    scroll_element_template,
    input_text_template,
    get_text_template,
]

config = utilities.read_yaml(f"{dir_name}{os.sep}config{os.sep}generate_page_conf.yaml")

GAP = "    "
key = config.get("LOCATOR_KEYNAME")
class_name = key.replace("_", " ").title().replace(" ", "")
locators = locators_manager.get_locators(key)
class_output = class_template.format(key, class_name)

variables = []


def __dict_walk_through(_dict, key=""):
    for k, v in _dict.items():
        _key = f"{key}.{k}" if key else k
        if isinstance(v, dict):
            __dict_walk_through(v, _key)
        else:
            keys = _key.split(".")
            value = "LOCATORS"
            for item in keys:
                value = value + f'.get("{item}")'
            out = {"KEY": f'{_key.replace(".", "_")}', "VALUE": value}
            variables.append(out)


__dict_walk_through(locators)

for var in variables:
    out = var.get("KEY") + " = " + var.get("VALUE")
    class_output = f"{class_output}\n{GAP}{out}"

class_output = class_output + "\n"


def __generate_template_method(variables, template):
    result = ""
    for item in variables:
        key = item.get("KEY")
        result = result + template.format(key.lower(), key.upper())
    return result


for template in templates:
    class_output = class_output + __generate_template_method(variables, template)

path = f'{dir_name}{os.sep}{config.get("OUTPUT_FOLDER")}'
os.makedirs(path, exist_ok=True)
output_file = path + os.sep + f'{config.get("LOCATOR_KEYNAME")}.py'
utilities.write_file(output_file, class_output)

print(
    "Code generated\nFolder: [{}]\nFile name: [{}]".format(
        f'{config.get("OUTPUT_FOLDER")}', f"{config.get('LOCATOR_KEYNAME')}.py"
    )
)
