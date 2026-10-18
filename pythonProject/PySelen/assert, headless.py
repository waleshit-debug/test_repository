from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
#options.add_argument("--headless=") #запускает браузер в headless режиме, то есть без открытия окна
g = Service()
driver = webdriver.Chrome(options=options, service=g)


url = 'https://www.saucedemo.com/'
standard_user = 'standard_user'
standard_pwd = 'secret_sauce'
driver.get(url)
driver.maximize_window()
login_field = driver.find_element(By.XPATH, "//*[@id='user-name']")
login_field.send_keys(standard_user)
password_field = driver.find_element(By.XPATH,"//*[@id='password']")
password_field.send_keys(standard_pwd)
login_button = driver.find_element(By.XPATH, "//*[@id='login-button']")
login_button.click()
text_products = driver.find_element(By.XPATH, "//span[@class='title']")
value_text_products = text_products.text
print(value_text_products)
assert value_text_products == 'Products'

get_url = driver.current_url
print(get_url)
assert url == get_url
print()