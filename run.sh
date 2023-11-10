. .venv/Scripts/activate
rm -rf allure-report
allure generate
pytest -n 3 --browser=chrome --alluredir=allure-report/ --cov tests/step_definitions
# allure serve allure-report
deactivate