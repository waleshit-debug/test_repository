import datetime
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from faker import Faker

fake = Faker('en_US')
name = fake.first_name()
address = fake.address()
email = fake.email()

print(name, address, email)

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
actions = ActionChains(driver) # создание экземпляра класса для перемещения по окну браузера

login_url = 'https://www.saucedemo.com/'
driver.get(login_url)

driver.maximize_window()
login_field = driver.find_element(By.XPATH, "//*[@id='user-name']")
login_field.send_keys(name)