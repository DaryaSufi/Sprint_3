from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from selenium import webdriver
from consants import Constants
@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get(*Constants.URL_FOR_TEST)
    yield browser
    browser.quit()