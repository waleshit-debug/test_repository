import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from faker import Faker
fake = Faker("en_US")

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

url = 'https://www.saucedemo.com/'
standard_user = 'standard_user'
standard_pwd = 'secret_sauce'
fake_user = fake.first_name()
print(fake_user)

driver.get(url)
login_field = driver.find_element(By.XPATH, "//*[@id='user-name']")
login_field.send_keys(fake_user)