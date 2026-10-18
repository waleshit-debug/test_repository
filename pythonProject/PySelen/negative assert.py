from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)


url = 'https://www.saucedemo.com/'
standard_user = 'standard_user'
standard_pwd = 'secret_sauce'
wrong_pwd = 'brbr'
driver.get(url)
driver.maximize_window()
login_field = driver.find_element(By.XPATH, "//*[@id='user-name']")
login_field.send_keys(standard_user)
password_field = driver.find_element(By.XPATH,"//*[@id='password']")
password_field.send_keys(wrong_pwd)
login_button = driver.find_element(By.XPATH, "//*[@id='login-button']")
login_button.click()

warning = driver.find_element(By.XPATH,"//h3[@data-test='error']")
warning_text = warning.text
assert warning_text == 'Epic sadface: Username and password do not match any user in this service'

driver.refresh()