from playwright.sync_api import sync_playwright

# Constants
c = {
  "xpaths": {
      "email_address": "//*[@id=\"exampleInputEmail1\"]",
      "password": "//*[@id=\"exampleInputPassword1\"]",
      "dropdown": "//*[@id=\"exampleSelect1\"]"
  },
  "urls": {
      "bootswatch_url": "https://bootswatch.com/default/",
  }
}


# ______Helping functions_______ #
def retrive_element_value_by_id_js(id, page):
    _value = page.evaluate('(elementId) => document.getElementById(elementId).value', id)
    print(f"\nValue of the element retrived from function: {_value}")
    return page.evaluate('(elementId) => document.getElementById(elementId).value', id)


def select_dropdown_option(dropdown_field, option_value):
    selected_option = dropdown_field.select_option(option_value)[0]
    print(f"\noption_{option_value}: {selected_option}")


def return_selected_option_dropdown(dropdown_field, option_value):
    selected_option = dropdown_field.select_option(option_value)[0]
    return selected_option


# This function is only for the convenience of the code reviewer.
# The function prints the assertion result in an organized way
# in a "real" QA project, I would have a simple assertion with logger.
def assert_expected_as_actual_print(expected, actual):
    print(f"\nExpected value to be caught in runtime is:- {expected} \nActual value caught in runtime is:--------- {actual}")
    assert expected == actual


pw = sync_playwright().start()
browser = pw.chromium.launch(headless=False, slow_mo=3 * 1000)
