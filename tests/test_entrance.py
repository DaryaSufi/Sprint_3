from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Locators import Locators
from consants import Constants
class TestEntrance:
    def test_log_in_using_the_Log_in_to_account_button_on_the_main_page_true(self,driver):
        driver.find_element(*Locators.BUTTON_ENTRANCE_TO_ACC).click()
        driver.find_element(*Locators.INPUT_EMAIL_ENTRANCE).send_keys(*Constants.EMAIL)
        driver.find_element(*Locators.INPUT_PASWWORD_ENTRANCE).send_keys(*Constants.PASSWORD)
        driver.find_element(*Locators.BUTTON_ENTRANCE).click()
        assert driver.find_element(*Locators.CHECKOUT_BUTTON)
    def test_log_in_via_the_Personal_account_button_true(self,driver):
        driver.find_element(Locators.BUTTON_PERS_ACC).click()
        driver.find_element(*Locators.INPUT_EMAIL_ENTRANCE).send_keys(*Constants.EMAIL)
        driver.find_element(*Locators.INPUT_PASWWORD_ENTRANCE).send_keys(*Constants.PASSWORD)
        driver.find_element(*Locators.BUTTON_ENTRANCE).click()
        assert driver.find_element(*Locators.CHECKOUT_BUTTON)
    def test_log_in_via_the_button_in_the_registration_form_true(self,driver):
        driver.find_element(*Locators.BUTTON_PERS_ACC).click()
        driver.find_element(*Locators.LINK_REG).click()
        driver.find_element(*Locators.INPUT_NAME).send_keys(*Constants.NAME)
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(*Constants.EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(*Constants.PASSWORD)
        driver.find_element(*Locators.BUTTON_REG).click()
        driver.find_element(*Locators.BUTTON_ENTRANCE).click()
        assert driver.find_element(*Locators.CHECKOUT_BUTTON)
    def login_via_the_button_in_the_password_recovery_form_true(self,driver):
        driver.find_element(*Locators.BUTTON_PERS_ACC).click()
        driver.find_element(*Locators.BUTTON_PASSWORD_RECOVERY).click()
        driver.find_element(*Locators.INPUT_EMAIL_FOR_PASS_RECOV).send_keys(*Constants.EMAIL)
        driver.find_element(Locators.BUTTON_RECOVERY).click()
        assert driver.find_element(*Locators.CHECKOUT_BUTTON)
