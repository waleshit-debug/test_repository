import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select # импортирование класса Select
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Данные для прохождения теста
login_url = 'https://www.saucedemo.com/'

standard_user = 'standard_user'
standard_pwd = 'secret_sauce'

# Авторизация пользователя в системе
driver.get(login_url)
driver.maximize_window()
login_field = driver.find_element(By.XPATH, "//*[@id='user-name']")
login_field.send_keys(standard_user)
password_field = driver.find_element(By.XPATH, "//*[@id='password']")
password_field.send_keys(standard_pwd)
login_button = driver.find_element(By.XPATH, "//*[@id='login-button']")
login_button.click()

select = Select(driver.find_element(By.XPATH, "//select[@class='product_sort_container']"))  # создание экземпляра класса Select
select.select_by_visible_text('Name (Z to A)')    # обращение к экземпляру класса Select
select.select_by_v
# https://stepik.org/lesson/1179222/step/2?unit=1191703