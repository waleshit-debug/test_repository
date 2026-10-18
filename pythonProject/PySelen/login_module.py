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
