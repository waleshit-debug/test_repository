import datetime
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
action = ActionChains(driver)

login_url = 'https://demoqa.com/buttons'

driver.get(login_url)
double = driver.find_element(By.XPATH, '//button[@id="doubleClickBtn"]')
action.double_click(double).perform()
print("Даблклик прожат")

rclick = driver.find_element(By.XPATH, '//button[@id="rightClickBtn"]')
action.double_click(double).perform()
action.context_click(rclick).perform()
print("Правая кнопка мыши прожата")