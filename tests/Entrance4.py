from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/register")

driver.find_element(By.XPATH, "/html/body/div/div/header/nav/a/p").click()
driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/p[2]/a").click()
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset/div/div").send_keys("DaryaSufiyarova12A984@yandex.ru")
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button").click()