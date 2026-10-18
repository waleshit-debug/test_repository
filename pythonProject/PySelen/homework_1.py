# 5.18 Тестовое задание по Selenium №1
# Авторизоваться на сайте, Выбрать 2 товара, Сохранить в переменные названия и цены товаров, Оплатить товары

import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Данные для прохождения теста
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

# Авторизация пользователя в системе
print(f'{current_date} test started')
driver.get(login_url)
driver.maximize_window()
login_field = driver.find_element(By.XPATH, "//*[@id='user-name']")
login_field.send_keys(standard_user)
password_field = driver.find_element(By.XPATH, "//*[@id='password']")
password_field.send_keys(standard_pwd)
login_button = driver.find_element(By.XPATH, "//*[@id='login-button']")
login_button.click()

# Подтверждение успешной авторизации
get_url = driver.current_url
assert products_url == get_url
print(f'{current_date} Authorized and redirected to {products_url}')

# Товар 1 для покупки
product_1 = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
value_product_1 = product_1.text
price_1 = driver.find_element(By.XPATH, '//div[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div')
value_price_1 = price_1.text

# Товар 2 для покупки
product_2 = driver.find_element(By.XPATH, '//a[@id="item_5_title_link"]')
value_product_2 = product_2.text
price_2 = driver.find_element(By.XPATH, '//div[@id="inventory_container"]/div/div[4]/div[2]/div[2]/div')
value_price_2 = price_2.text

# Добавление товара 1 в корзину
add_to_cart_1 = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
add_to_cart_1.click()
print(f'{current_date} item {value_product_1} added to cart')

# Добавление товара 2 в корзину
add_to_cart_2 = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-fleece-jacket"]')
add_to_cart_2.click()
print(f'{current_date} item {value_product_2} added to cart')

# Переход в корзину
go_to_cart = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
go_to_cart.click()
print(f'{current_date} cart icon pressed')
get_url = driver.current_url
assert cart_url == get_url
print(f'{current_date} redirected to {cart_url}')

# Проверка товара 1 в корзине
cart_product_1 = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
cart_value_product_1 = cart_product_1.text
cart_price_1 = driver.find_element(By.XPATH, '(//div[@class="inventory_item_price"])[1]')
cart_value_price_1 = cart_price_1.text
# print(value_price_1, cart_value_price_1)

assert value_product_1 == cart_value_product_1
print(f'item {value_product_1} in cart checked')
assert value_price_1 == cart_value_price_1
print(f'price {value_price_1} in cart checked')

# Проверка товара 2 в корзине
cart_product_2 = driver.find_element(By.XPATH, '//a[@id="item_5_title_link"]')
cart_value_product_2 = cart_product_2.text
cart_price_2 = driver.find_element(By.XPATH, '(//div[@class="inventory_item_price"])')
cart_value_price_2 = cart_price_2.text
# print(value_price_2, cart_value_price_2)

assert value_product_2 == cart_value_product_2
print(f'item {value_product_2} in cart checked')
assert value_price_2 == cart_value_price_2
print(f'price {value_price_2} in cart checked')

# оформление заказа
checkout = driver.find_element(By.XPATH, '//button[@id="checkout"]')
checkout.click()
get_url = driver.current_url
assert checkout_1_url == get_url
print(f'{current_date} checkout')

# ввод данных для отправки заказа
first_name_field = driver.find_element(By.XPATH, '//input[@id="first-name"]')
first_name_field.send_keys(first_name)
print(f'first name - {first_name}')
last_name_field = driver.find_element(By.XPATH, '//input[@id="last-name"]')
last_name_field.send_keys(last_name)
print(f'last name - {last_name}')
zip_code_field = driver.find_element(By.XPATH, '//input[@id="postal-code"]')
zip_code_field.send_keys(zip_code)
print(f'zip code - {zip_code}')
continue_button = driver.find_element(By.XPATH, '//input[@id="continue"]')
continue_button.click()
print(f'{current_date} continue checkout')

# Проверка товара 1 при оформлении заказа
checkout_product_1 = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]/div')
checkout_value_product_1 = checkout_product_1.text
print(f'item {checkout_value_product_1} on checkout checked')

checkout_price_1 = driver.find_element(By.XPATH, '//div[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
checkout_value_price_1 = checkout_price_1.text
assert checkout_value_price_1 == cart_value_price_1
print(f'price {checkout_value_price_1} on checkout checked')

# Проверка товара 2 при оформлении заказа
checkout_product_2 = driver.find_element(By.XPATH, '//a[@id="item_5_title_link"]')
checkout_value_product_2 = checkout_product_2.text
print(f'item {checkout_value_product_2} on checkout checked')

checkout_price_2 = driver.find_element(By.XPATH, '(//div[@class="inventory_item_price"])[2]')
checkout_value_price_2 = checkout_price_2.text
assert checkout_value_price_2 == cart_value_price_2
print(f'price {checkout_value_price_2} on checkout checked')

# Расчет ожидаемой суммы всех товаров
price_1_digit = float(checkout_value_price_1[1:])
price_2_digit = float(checkout_value_price_2[1:])
price_summ = price_1_digit + price_2_digit
total_calculated = str(f'Item total: ${price_summ}')

# Сверка суммы всех товаров
total_fact = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[6]')
value_total = total_fact.text

assert value_total == total_calculated
print(f'{value_total} on checkout checked')