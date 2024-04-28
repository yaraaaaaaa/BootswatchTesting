import time
import pytest
import conftest


#  As a user I want to be able to write an email address in the email field box
#  So that I can later on submit the form with my correct personal details
@pytest.mark.smoke
@pytest.mark.email
@pytest.mark.regression
def test_email_field_value_integrity():
    # Step 1: Given bootswatch page open
    page = conftest.browser.new_page()
    page.goto(conftest.c["urls"]["bootswatch_url"])

    # Step 2: When I click on the email field box
    email_field = page.locator(conftest.c["xpaths"]["email_address"])
    email_field.scroll_into_view_if_needed()
    email_field.click()

    # Step 3: Then I should be able to write an email address value
    testing_email_address = "example@email.com"
    email_field.fill(testing_email_address)
    time.sleep(1)

    # Step 4: And it should be the same value caught in runtime
    email_value = conftest.retrive_element_value_by_id_js('exampleInputEmail1', page)
    conftest.assert_expected_as_actual_print(testing_email_address, email_value)

    page.close()
