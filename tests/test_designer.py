from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Locators import Locators
from consants import Constants
class TestDesigner:
    def test_go_to_the_Roll_section(self, driver):
        driver.find_element(*Locators.BUTTON_ROLLS).click()
        assert driver.find_element(*Locators.LIST_OF_ROLLS)
    def test_go_to_the_Sauces_section(self,driver):
        driver.find_element(*Locators.BUTTON_SAUCES).click()
        assert driver.find_element(*Locators.LIST_OF_SAUCES)
    def test_go_to_the_Filling_section(self,driver):
        driver.find_element(*Locators.BUTTON_FILLINGS).click()
        assert driver.find_element(*Locators.LIST_OF_FILLINGS)