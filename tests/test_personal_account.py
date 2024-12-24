from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Locators import Locators
from consants import Constants

class TestPersonalAccount:
    def test_click_through_to_the_Personal_account(self, driver):
        driver.find_element(*Locators.BUTTON_PERS_ACC).click()
        assert driver.find_element(*Locators.CHECKOUT_BUTTON)
    def test_click_through_to_the_designer(self, driver):
        driver.find_element(*Locators.BUTTON_DESIGNER).click()
        assert driver.find_element(*Locators.TEXT_DESIGN_BURGER)
    def test_click_through_to_the_Stellar_Burgers_logo(self,driver):
        driver.find_element(*Locators.LOGO).click()
        assert driver.find_element(*Locators.TEXT_DESIGN_BURGER)
    def test_log_out_of_your_account(self, driver):
        driver.find_element(*Locators.BUTTON_PERS_ACC).click()
        driver.find_element(*Locators.BUTTON_EXIT).click()
        assert driver.find_element(*Locators.BUTTON_ENTRANCE)

