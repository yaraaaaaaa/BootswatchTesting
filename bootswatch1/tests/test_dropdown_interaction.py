import time
import pytest
import conftest


#  As a user I want to be able to interact with the dropdown element
#  So that I can choose any value from the options in different ways and close the dropdown after I finish
@pytest.mark.regression
@pytest.mark.dropdown
def test_dropdown_selecting_any_option():

    # Step 1: Given bootswatch page open
    page = conftest.browser.new_page()
    page.goto(conftest.c["urls"]["bootswatch_url"])

    # Step 2: When clicking dropdown element
    dropdown_field = page.locator(conftest.c["xpaths"]["dropdown"])
    dropdown_field.scroll_into_view_if_needed()

    # Step 3: Then I should be able to select any option from the shown list
    dropdown_options = ['1', '2', '3', '4', '5']
    for option_value in dropdown_options:
        # dropdown is client-side rendered element
        # (not exposed in the HTML source code hence not clickable with .click() function)
        conftest.select_dropdown_option(dropdown_field, option_value)
        # Step 4: And value selected should be the same value caught in runtime
        conftest.assert_expected_as_actual_print(option_value, conftest.return_selected_option_dropdown(dropdown_field,
                                                                                                        option_value))
    page.close()


#  As a user I want to be able to interact with the dropdown element
#  So that I can choose any value from the options in different ways and close the dropdown after I finish
@pytest.mark.regression
@pytest.mark.dropdown
def test_dropdown_selecting_any_option_keyboard_d_arrow():

    # Step 1: Given bootswatch page open
    page = conftest.browser.new_page()
    page.goto(conftest.c["urls"]["bootswatch_url"])

    # Step 2: When clicking dropdown element and clicking on down arrow key on keyboard
    dropdown_field = page.locator(conftest.c["xpaths"]["dropdown"])
    dropdown_field.scroll_into_view_if_needed()
    dropdown_field.click()
    # Step 3: Then I should be able to select any element from dropdown using down arrow
    dropdown_options = ['1', '2', '3', '4', '5']
    for option_value in dropdown_options:
        # No usage of down arrow if user reached option 5
        if option_value == '5':
            conftest.select_dropdown_option(dropdown_field, option_value)
        else:
            conftest.select_dropdown_option(dropdown_field, option_value)
            page.keyboard.press('ArrowDown')

    page.close()


#  As a user I want to be able to interact with the dropdown element
#  So that I can choose any value from the options in different ways and close the dropdown after I finish
@pytest.mark.regression
@pytest.mark.dropdown
def test_dropdown_responsive_onclick():

    # Step 1: Given bootswatch page open
    page = conftest.browser.new_page()
    page.goto(conftest.c["urls"]["bootswatch_url"])
    # Step 2: When clicking dropdown element
    dropdown_field = page.locator(conftest.c["xpaths"]["dropdown"])
    dropdown_field.scroll_into_view_if_needed()
    dropdown_field.click()
    # Step 4 + 5: Then taking a screenshot Then closing dropdown
    web_image_with_open_dropdown = page.screenshot()
    # Step 5: Then closing dropdown
    dropdown_field.click()
    time.sleep(2)
    dropdown_field.click()
    # Step 6: Then taking another screenshot and comparing screenshots
    web_image_with_closed_dropdown = page.screenshot()
    # Step 7: Then screenshot values should be different
    assert web_image_with_open_dropdown != web_image_with_closed_dropdown

    page.close()
