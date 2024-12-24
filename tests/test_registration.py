from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Locators import Locators
from consants import Constants
from faker import Faker
faker = Faker()
class TestRegistration:
    def test_resistration_true(self, driver):
        email = faker.email()
        driver.find_element(*Locators.BUTTON_PERS_ACC).click()
        driver.find_element(*Locators.LINK_REG).click()
        driver.find_element(*Locators.INPUT_NAME).send_keys(*Constants.NAME)
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(*Constants.PASSWORD)
        driver.find_element(*Locators.BUTTON_REG).click()
        assert driver.find_element(*Locators.BUTTON_ENTRANCE)
    def tets_entering_an_incorrect_password(self,driver):
        email = faker.email()
        driver.find_element(*Locators.BUTTON_PERS_ACC).click()
        driver.find_element(*Locators.LINK_REG).click()
        driver.find_element(*Locators.INPUT_NAME).send_keys(*Constants.NAME)
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(*Constants.INCORRECT_PASSWORD)
        driver.find_element(*Locators.BUTTON_REG).click()
        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(*Locators.ERROR_TEXT))