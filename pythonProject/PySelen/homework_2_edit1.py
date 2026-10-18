# 5.18 Тестовое задание по Selenium №3
# Получить от пользователя ID товара и по нему оформить покупку

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

# Поиск общих локаторов для наименований продуктов, цены, кнопки добавления в корзину
product_names = driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
product_prices = driver.find_elements(By.CLASS_NAME, 'inventory_item_price')
add_to_cart_buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory")

print("Укажите номер товара, который вы хотите добавить в корзину")
for n in range(len(product_names)):
    print(f"{n+1}. {product_names[n].text} - {product_prices[n].text}")

user_choice = int(input())

if user_choice in range(1, 7):
    print(f"Вы выбрали {product_names[user_choice-1].text} - {product_prices[user_choice-1].text}")
else:
    print("Товар с таким номером не найден")
    exit()

value_product = product_names[user_choice-1].text
value_price = product_prices[user_choice-1].text

add_to_cart_buttons[user_choice-1].click()

# Переход в корзину
go_to_cart = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
go_to_cart.click()
print(f'{current_date} cart icon pressed')
get_url = driver.current_url
assert cart_url == get_url
print(f'{current_date} redirected to {cart_url}')

# Проверка товаров в корзине
cart_value_product = driver.find_elements(By.CLASS_NAME, 'inventory_item_name')[0].text
cart_value_price = driver.find_elements(By.CLASS_NAME, 'inventory_item_price')[0].text

assert value_product == cart_value_product
print(f'Товары в корзине - {value_product}')
assert value_price == cart_value_price
print(f'Стоимость товаров в корзине- {value_price}')

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

# Проверка товара при оформлении заказа
checkout_value_product = driver.find_elements(By.CLASS_NAME, 'inventory_item_name')[0].text
checkout_value_price = driver.find_elements(By.CLASS_NAME, 'inventory_item_price')[0].text

assert checkout_value_product == cart_value_product
print(f'item {checkout_value_product} on checkout checked')
assert checkout_value_price == cart_value_price
print(f'price {checkout_value_price} on checkout checked')