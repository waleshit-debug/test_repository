import datetime
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)

url = 'https://www.saucedemo.com/'
standard_user = 'standard_user'
standard_pwd = 'secret_sauce'
# current_date = datetime.datetime.now().strftime('%d.%m.%Y-.%H.%M.%S')
# screenshot_name = 'scr ' + current_date + '.png'
# screenshot_dir = '/Users/apetrova/PycharmProjects/pythonProject/PySelen/scr/'
driver.get(url)
driver.maximize_window()
login_field = driver.find_element(By.XPATH, "//*[@id='user-name']")
login_field.send_keys(standard_user)
password_field = driver.find_element(By.XPATH,"//*[@id='password']")
password_field.send_keys(standard_pwd)
login_button = driver.find_element(By.XPATH, "//*[@id='login-button']")
login_button.click()
print('user logged in')

driver.refresh()

menu = driver.find_element(By.XPATH,"//button[@id='react-burger-menu-btn']")
menu.click()
time.sleep(10)
print('menu opens')
menu_about = driver.find_element(By.XPATH,'//a[@id="about_sidebar_link"]')
menu_about.click()
print('about clicked')