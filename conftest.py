from selene import browser
import pytest

@pytest.fixture
def browser_settings():
    browser.config.window_width = 1920
    browser.config.window_height = 1080

@pytest.fixture
def browser_open():
    browser.open('https://ya.ru')
    yield
    browser.quit()
