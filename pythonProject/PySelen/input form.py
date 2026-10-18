import datetime

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)

url = 'https://www.lambdatest.com/selenium-playground/simple-form-demo'
driver.get(url)
input_field = driver.find_element(By.XPATH, '//input[@id="user-message"]')
message = 'message text'
input_field.send_keys(message)
send_button = driver.find_element(By.XPATH, '//button[@id="showInput"]')
send_button.click()