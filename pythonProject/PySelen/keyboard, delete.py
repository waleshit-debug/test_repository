from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

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
login_field.send_keys(Keys.BACKSPACE)
login_field.send_keys(Keys.ENTER) #(Keys.RETURN)
login_field.send_keys(Keys.COMMAND + 'a')
login_field.send_keys(Keys.DELETE)
password_field = driver.find_element(By.XPATH,"//*[@id='password']")
password_field.clear()
