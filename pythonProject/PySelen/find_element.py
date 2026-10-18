import click
from selenium import webdriver
from time import sleep
# from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Initialize Chrome WebDriver
options = webdriver.ChromeOptions()
'''чтобы браузер не закрывался'''
options.add_experimental_option('detach', True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)


driver.get('https://www.lambdatest.com/selenium-playground/checkbox-demo')
driver.maximize_window()

#sleep(30)
#driver.close()

'''устаревший способ'''
#name_input = driver.find_element_by_id("user-name")
#name_input = driver.find_element_by_name("q")

'''актуальный способ'''
#user_name = driver.find_element(By.ID, 'user-name') #ID
# user_name = driver.find_element(By.NAME, ) #Name
# user_name = driver.find_element(By.TAG_NAME, ) #Tag name
user_name = driver.find_element(By.XPATH, '(//input[@class="cb-element mr-10"])[3]').click
#user_name = driver.find_element((By.XPATH, ''))

# send keys
#user_name.send_keys('standard_user')
