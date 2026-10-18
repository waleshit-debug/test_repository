from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)

url = 'https://www.lambdatest.com/selenium-playground/iframe-demo/'
driver.get(url)
iframe = driver.find_element(By.XPATH, "//iframe[@id='iFrame1']")
driver.switch_to.frame(iframe)
input_field_bold = driver.find_element(By.XPATH, "//button[@title='Bold']")
input_field_bold.click()
input_field = driver.find_element(By.XPATH, "//div[@id='__next']/div/div[2]")
input_field.send_keys(Keys.COMMAND + 'a')
input_field.send_keys(Keys.DELETE)
message = 'message text'
input_field.send_keys(message)
value_input_field = input_field.text
