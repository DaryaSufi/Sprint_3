from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site")
driver.find_element(By.XPATH, "/html/body/div/div/main/section[2]/div/button").click()
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys("DaryaSufiyarova12A984@yandex.ru")
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys("100863")
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button").click()
WebDriverWait(driver,3).until(expected_conditions.presence_of_all_elements_located((By.TAG_NAME, "body")))
driver.find_element(By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[2]/span").click()
driver.find_element(By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[3]/span").click()
driver.find_element(By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[1]/span").click()

