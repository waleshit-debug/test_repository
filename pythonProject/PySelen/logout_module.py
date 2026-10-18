from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager

login_url = 'https://www.saucedemo.com/'
products_url = 'https://www.saucedemo.com/inventory.html'

class LogOut():
    """Класс описывающий выход из системы"""

    def __init__(self):
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    #     конструктор класса, который выполняет инициализацию экземпляра класса при его создании

    def test_log_out(self, standard_user, standard_password):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()

        self.driver.get(login_url)
        self.driver.maximize_window()
        login_field = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='user-name']")))
        login_field.send_keys(standard_user)
        print('enter login')
        password_field = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='password']")))
        password_field.send_keys(standard_password)
        print('enter password')
        login_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='login-button']")))
        login_button.click()
        print('press login button')


test = LogIn()
test.test_authorisation('standard_user', 'secret_sauce')  # Вызов метода с тестом
