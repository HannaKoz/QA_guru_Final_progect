import pytest
from selene import browser
from selene.support.shared import browser


@pytest.fixture()
def browser_size_w1920_h1080():
    # browser.config.browser_name = "Firefox"
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#RightSide_Advertisement').execute_script('element.remove()')
    # webelement = browser.element('#RightSide_Advertisement').locate()
    # browser.driver.execute_script('arguments[0].remove()', webelement)
    yield browser_size_w1920_h1080
    # browser.config.hold_browser_open = True
    print(' Good job, dude! 👍')
    print('Have a nice day! 😎')


@pytest.fixture()
def browser_size_w1280_h720():
    # browser.config.browser_name = "Firefox"
    browser.config.window_width = 1280
    browser.config.window_height = 720
    browser.open('https://demoqa.com/automation-practice-form')
    yield browser_size_w1920_h1080
    browser.config.hold_browser_open = True
