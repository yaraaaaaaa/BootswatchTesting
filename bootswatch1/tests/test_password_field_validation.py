import time
import pytest
import conftest


#  As a user I want to be able to write a password in the password field box
#  So that I can later on submit the form with my correct personal details
@pytest.mark.smoke
@pytest.mark.password
@pytest.mark.regression
def test_password_field_value_integrity():

    # Step 1: Given bootswatch page open
    page = conftest.browser.new_page()
    page.goto(conftest.c["urls"]["bootswatch_url"])

    # Step 2: When I click on password field box
    password_field = page.locator(conftest.c["xpaths"]["password"])
    password_field.scroll_into_view_if_needed()
    password_field.click()

    # Step 3: Then I should be able to write a password value
    testing_password = "eeeeeeeeeeee"
    password_field.fill(testing_password)
    time.sleep(1)

    # Step 4: And  it will be the same value caught in runtime
    password_value = conftest.retrive_element_value_by_id_js('exampleInputPassword1', page)
    conftest.assert_expected_as_actual_print(testing_password, password_value)
    
    page.close()
