import datetime
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager

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


class TestBuyProduct():
    """Класс включающий сценарий покупки товара"""

    def test_login(self):
        """Тест по покупке товара включает:
         в себя авторизацию, выбор товара, заполнение данных получателя, подтверждение покупки."""

        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()

        print('Start test')

        print(f'{current_date} test started')
        driver.get(login_url)
        driver.maximize_window()
        login_field = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='user-name']")))
        login_field.send_keys(standard_user)
        print('enter login')
        password_field = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='password']")))
        password_field.send_keys(standard_pwd)
        print('enter password')
        login_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='login-button']")))
        login_button.click()
        print('press login button')
        time.sleep(10)

        select_product = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')))
        select_product.click()
        print('press add to cart button')

        go_to_cart = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="shopping_cart_link"]')))
        go_to_cart.click()
        print('press cart button')

        success_test = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//span[@class="title"]')))
        value_success_test = success_test.text
        print(value_success_test)
        assert value_success_test == "Your Cart"
        print('test completed')
    # явное ожидание 30 секунд и условие, что элемент будет кликабельным
    # WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//buttomn[id='visibleAfter']")))
        # ввод Логина
        # ввод Пароля
        # клик для входа в систему
        #
        # выбор товара
        # проверка товара в корзине
        # .......
        # подтверждение успешной покупки
        #
        # закрытие браузера


test = TestBuyProduct()  # Создание экземпляра класса
test.test_login()  # Вызов метода с тестом
