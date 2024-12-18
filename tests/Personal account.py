from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/register")

driver.find_element(By.XPATH, "/html/body/div/div/header/nav/a/p").click()
driver.find_element(By.XPATH, "/html/body/div/div/header/nav/ul/li[1]/a/p").click()

