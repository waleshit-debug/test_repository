# Файл 1. Описание класса LogInOut

import self
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

login_url = 'https://www.saucedemo.com/'
current_date = datetime.datetime.now().strftime('%d.%m.%Y-%H.%M.%S')


# Инициализация класса
class LogInOut:
    def __init__(self, user, password):
        self.user = user
        self.password = password

    # Метод, описывающий авторизацию на сайте
    def test_authorisation(self):
        login_field = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='user-name']")))
        login_field.send_keys(self.user)
        print(f'{current_date} Enter login "{self.user}"')
        password_field = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='password']")))
        password_field.send_keys(self.password)
        print(f'{current_date} Enter password "{self.password}"')
        login_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='login-button']")))
        login_button.click()
        print(f'{current_date} Press login button')

    # Метод, описывающий разлогинивание на сайте
    def test_log_out(self):
        burger_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='react-burger-menu-btn']")))
        burger_button.click()
        log_out_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='logout_sidebar_link']")))
        log_out_button.click()
        print(f'{current_date} User "{self.user}" logged out')


# Файл 2. Список с пользователями, вызов метода авторизации и разлогина для каждого пользователя
from selenium.webdriver.common.by import By
from PySelen.login_module import LogInOut, login_url, driver, current_date

products_url = 'https://www.saucedemo.com/inventory.html'

driver.get("https://www.saucedemo.com/")
driver.maximize_window()
user_list = {'standard_user': 'secret_sauce', 'locked_out_user': 'secret_sauce', 'problem_user': 'secret_sauce',
             'performance_glitch_user': 'secret_sauce'}
for l, p in user_list.items():
    LogInOut(l, p).test_authorisation()
    get_url = driver.current_url
    if products_url == get_url:
        print(f'{current_date} User "{l}" authorized and redirected to {products_url}')
        LogInOut(l, p).test_log_out()
    elif get_url == login_url:
        print(f'{current_date} User "{l}" failed to log in')
        login_field = driver.find_element(By.XPATH, "//*[@id='user-name']")
        login_field.clear()
        password_field = driver.find_element(By.XPATH, "//*[@id='password']")
        password_field.clear()
        print(f'{current_date} Input fields cleared')
        continue
    else:
        print(get_url)
        break
