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


class Product:
    def __init__(self, serial_number, name, price, add_to_cart_button):
        self.serial_number = serial_number
        self.name = name
        self.price = price
        self.add_to_cart_button = add_to_cart_button

    def provide_info(self):
        provide_info = (
            f' {self.serial_number} -- товар {self.name} стоимостью {self.price}')
        return provide_info

    def get_info(self):
        get_info = (
            f' Вы добавили в корзину товар {self.name} стоимостью {self.price}')
        return get_info

    def add_to_cart(self):
        add_to_cart_button = {self.add_to_cart_button}


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

# Карточка товара 1
product_1 = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
value_product_1 = product_1.text
price_product_1 = driver.find_element(By.XPATH, '//div[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div')
value_price_1 = price_product_1.text

# Добавление товара 1 в корзину
add_to_cart_1 = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')

# Карточка товара 2
product_2 = driver.find_element(By.XPATH, '//a[@id="item_0_title_link"]')
value_product_2 = product_2.text
price_product_2 = driver.find_element(By.XPATH, '//div[@id="inventory_container"]/div/div[2]/div[2]/div[2]/div')
value_price_2 = price_product_2.text

# Добавление товара 2 в корзину
add_to_cart_2 = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-bike-light"]')

# Карточка товара 3
product_3 = driver.find_element(By.XPATH, '//a[@id="item_1_title_link"]')
value_product_3 = product_3.text
price_product_3 = driver.find_element(By.XPATH, '//div[@id="inventory_container"]/div/div[3]/div[2]/div[2]/div')
value_price_3 = price_product_3.text

# Добавление товара 3 в корзину
add_to_cart_3 = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')

# Карточка товара 4
product_4 = driver.find_element(By.XPATH, '//a[@id="item_5_title_link"]')
value_product_4 = product_4.text
price_product_4 = driver.find_element(By.XPATH, '//div[@id="inventory_container"]/div/div[4]/div[2]/div[2]/div')
value_price_4 = price_product_4.text

# Добавление товара 4 в корзину
add_to_cart_4 = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-fleece-jacket"]')

# Карточка товара 5
product_5 = driver.find_element(By.XPATH, '//a[@id="item_2_title_link"]')
value_product_5 = product_5.text
price_product_5 = driver.find_element(By.XPATH, '//div[@id="inventory_container"]/div/div[5]/div[2]/div[2]/div')
value_price_5 = price_product_5.text

# Добавление товара 5 в корзину
add_to_cart_5 = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-onesie"]')

# Карточка товара 6
product_6 = driver.find_element(By.XPATH, '//a[@id="item_3_title_link"]')
value_product_6 = product_6.text
price_product_6 = driver.find_element(By.XPATH, '//div[@id="inventory_container"]/div/div[6]/div[2]/div[2]/div')
value_price_6 = price_product_6.text

# Добавление товара 6 в корзину
add_to_cart_6 = driver.find_element(By.XPATH, '//button[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]')

item_1 = Product("1", value_product_1, value_price_1, add_to_cart_1)
item_2 = Product("2", value_product_2, value_price_2, add_to_cart_2)
item_3 = Product("3", value_product_3, value_price_3, add_to_cart_3)
item_4 = Product("4", value_product_4, value_price_4, add_to_cart_4)
item_5 = Product("5", value_product_5, value_price_5, add_to_cart_5)
item_6 = Product("6", value_product_6, value_price_6, add_to_cart_6)
print(item_1.provide_info())
print(item_2.provide_info())
print(item_3.provide_info())
print(item_4.provide_info())
print(item_5.provide_info())
print(item_6.provide_info())

print("Укажите номер товара, который вы хотите добавить в корзину")
user_choice = int(input())

if user_choice == 1:
    print(f"Вы выбрали {item_1.provide_info()}")
    add_to_cart_1.click()
elif user_choice == 2:
    print(f"Вы выбрали {item_2.provide_info()}")
    add_to_cart_2.click()
elif user_choice == 3:
    print(f"Вы выбрали {item_3.provide_info()}")
    add_to_cart_3.click()
elif user_choice == 4:
    print(f"Вы выбрали {item_4.provide_info()}")
    add_to_cart_4.click()
elif user_choice == 5:
    print(f"Вы выбрали {item_5.provide_info()}")
    add_to_cart_5.click()
elif user_choice == 6:
    print(f"Вы выбрали {item_6.provide_info()}")
    add_to_cart_6.click()
else:
    print("Товар с таким номером не найден")

# Переход в корзину
go_to_cart = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
go_to_cart.click()
print(f'{current_date} cart icon pressed')
get_url = driver.current_url
assert cart_url == get_url
print(f'{current_date} redirected to {cart_url}')

# локатор цены в корзине вынесен в отдельную переменную
cart_price = driver.find_element(By.XPATH, '(//div[@class="inventory_item_price"])')

if user_choice == 1:
    # Проверка товара 1 в корзине
    cart_product_1 = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
    cart_value_product_1 = cart_product_1.text
    cart_price_1 = cart_price
    cart_value_price_1 = cart_price_1.text

    assert value_product_1 == cart_value_product_1
    print(f'Товары в корзине - {value_product_1}')
    assert value_price_1 == cart_value_price_1
    print(f'Стоимость товаров в корзине- {value_price_1}')

elif user_choice == 2:
    # Проверка товара 2 в корзине
    cart_product_2 = driver.find_element(By.XPATH, '//a[@id="item_0_title_link"]')
    cart_value_product_2 = cart_product_2.text
    cart_price_2 = cart_price
    cart_value_price_2 = cart_price_2.text

    assert value_product_2 == cart_value_product_2
    print(f'Товары в корзине - {value_product_2}')
    assert value_price_2 == cart_value_price_2
    print(f'Стоимость товаров в корзине- {value_price_2}')

elif user_choice == 3:
    # Проверка товара 3 в корзине
    cart_product_3 = driver.find_element(By.XPATH, '//a[@id="item_1_title_link"]')
    cart_value_product_3 = cart_product_3.text
    cart_price_3 = cart_price
    cart_value_price_3 = cart_price_3.text

    assert value_product_3 == cart_value_product_3
    print(f'Товары в корзине - {value_product_3}')
    assert value_price_3 == cart_value_price_3
    print(f'Стоимость товаров в корзине- {value_price_3}')

elif user_choice == 4:
    # Проверка товара 4 в корзине
    cart_product_4 = driver.find_element(By.XPATH, '//a[@id="item_5_title_link"]')
    cart_value_product_4 = cart_product_4.text
    cart_price_4 = cart_price
    cart_value_price_4 = cart_price_4.text

    assert value_product_4 == cart_value_product_4
    print(f'Товары в корзине - {value_product_4}')
    assert value_price_4 == cart_value_price_4
    print(f'Стоимость товаров в корзине- {value_price_4}')

elif user_choice == 5:
    # Проверка товара 5 в корзине
    cart_product_5 = driver.find_element(By.XPATH, '//a[@id="item_2_title_link"]')
    cart_value_product_5 = cart_product_5.text
    cart_price_5 = cart_price
    cart_value_price_5 = cart_price_5.text

    assert value_product_5 == cart_value_product_5
    print(f'Товары в корзине - {value_product_5}')
    assert value_price_5 == cart_value_price_5
    print(f'Стоимость товаров в корзине- {value_price_5}')

elif user_choice == 6:
    # Проверка товара 6 в корзине
    cart_product_6 = driver.find_element(By.XPATH, '//a[@id="item_3_title_link"]')
    cart_value_product_6 = cart_product_6.text
    cart_price_6 = cart_price
    cart_value_price_6 = cart_price_6.text

    assert value_product_6 == cart_value_product_6
    print(f'Товары в корзине - {value_product_6}')
    assert value_price_6 == cart_value_price_6
    print(f'Стоимость товаров в корзине- {value_price_6}')

# оформление заказа
checkout = driver.find_element(By.XPATH, '//button[@id="checkout"]')
checkout.click()
get_url = driver.current_url
assert checkout_1_url == get_url
print(f'{current_date} checkout')

# ввод данных для отправки заказа - запросить у пользователя
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

# локатор цены при оформлении заказа вынесен в отдельную переменную
checkout_price = driver.find_element(By.XPATH,
                                           '//div[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
# Проверка товара 1 при оформлении заказа
if user_choice == 1:
    checkout_product_1 = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
    checkout_value_product_1 = checkout_product_1.text
    checkout_price_1 = checkout_price
    checkout_value_price_1 = checkout_price_1.text
    assert checkout_value_price_1 == cart_value_price_1
    print(f'item {checkout_value_product_1} on checkout checked')

# Проверка товара 2 при оформлении заказа
elif user_choice == 2:
    checkout_product_2 = driver.find_element(By.XPATH, '//a[@id="item_0_title_link"]')
    checkout_value_product_2 = checkout_product_2.text
    checkout_price_2 = checkout_price
    checkout_value_price_2 = checkout_price_2.text
    assert checkout_value_price_2 == cart_value_price_2
    print(f'item {checkout_value_product_2} on checkout checked')

# Проверка товара 3 при оформлении заказа
elif user_choice == 3:
    checkout_product_3 = driver.find_element(By.XPATH, '//a[@id="item_1_title_link"]')
    checkout_value_product_3 = checkout_product_3.text
    checkout_price_3 = checkout_price
    checkout_value_price_3 = checkout_price_3.text
    assert checkout_value_price_3 == cart_value_price_3
    print(f'item {checkout_value_product_3} on checkout checked')

# Проверка товара 4 при оформлении заказа
elif user_choice == 4:
    checkout_product_4 = driver.find_element(By.XPATH, '//a[@id="item_5_title_link"]')
    checkout_value_product_4 = checkout_product_4.text
    checkout_price_4 = checkout_price
    checkout_value_price_4 = checkout_price_4.text
    assert checkout_value_price_4 == cart_value_price_4
    print(f'item {checkout_value_product_4} on checkout checked')

# Проверка товара 5 при оформлении заказа
elif user_choice == 5:
    checkout_product_5 = driver.find_element(By.XPATH, '//a[@id="item_2_title_link"]')
    checkout_value_product_5 = checkout_product_5.text
    checkout_price_5 = checkout_price
    checkout_value_price_5 = checkout_price_5.text
    assert checkout_value_price_5 == cart_value_price_5
    print(f'item {checkout_value_product_5} on checkout checked')

# Проверка товара 6 при оформлении заказа
elif user_choice == 6:
    checkout_product_6 = driver.find_element(By.XPATH, '//a[@id="item_3_title_link"]')
    checkout_value_product_6 = checkout_product_6.text
    checkout_price_6 = checkout_price
    checkout_value_price_6 = checkout_price_6.text

    assert checkout_value_price_6 == cart_value_price_6
    print(f'item {checkout_value_product_6} on checkout checked')