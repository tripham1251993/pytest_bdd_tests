from pytest_bdd import scenarios, then, parsers


scenarios("../features/login.feature")


@then("User should be navigate to Dashboard page")
def verify_user_not_in_login_page(login_page):
    login_page.wait_until_page_does_not_contain_username_input()


@then("User should see an error message")
def verify_error_message_is_visible(login_page):
    login_page.wait_until_validate_message_is_visible()


@then(parsers.parse("Error message should be {error_message}"))
def error_message_text_should_be(login_page, error_message):
    actual_message = login_page.get_validate_message_text()
    assert actual_message == error_message
