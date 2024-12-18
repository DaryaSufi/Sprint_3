from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/register")

driver.find_element(By.XPATH, "/html/body/div/div/header/nav/a/p").click()
driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/p[1]/a").click()
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys("Дарина")
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys("DaryaSufiyarova12A983@yandex.ru")
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/div/input").send_keys("1008")
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button").click()
assert WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/div/div/main/div/form/fieldset[3]/div/p" )))


