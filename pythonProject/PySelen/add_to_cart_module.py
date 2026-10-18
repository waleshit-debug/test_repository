import datetime
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager

from PySelen.login_module import LogIn

login_url = 'https://www.saucedemo.com/'
products_url = 'https://www.saucedemo.com/inventory.html'
cart_url = 'https://www.saucedemo.com/cart.html'
checkout_1_url = 'https://www.saucedemo.com/checkout-step-one.html'
checkout_2_url = 'https://www.saucedemo.com/checkout-step-two.html'
checkout_complete_url = 'https://www.saucedemo.com/checkout-complete.html'
standard_user = 'standard_user'
standard_pwd = 'secret_sauce'
first_name = 'Ivan'
last_name = 'Ivanov'
zip_code = '123456'
current_date = datetime.datetime.now().strftime('%d.%m.%Y-%H.%M.%S')


class BuyProduct():
    """Класс включающий сценарий покупки товара"""

    def test_buy_product(self):  # метод
        """Тест по покупке товара включает:
         в себя авторизацию, выбор товара, заполнение данных получателя, подтверждение покупки."""

        login = "standard_user"
        password = 'secret_sauce'

        test = LogIn()
        test.test_authorisation(login, password)  # Вызов метода авторизации


start_test = BuyProduct
start_test.test_buy_product()  # Вызов метода с тестом
