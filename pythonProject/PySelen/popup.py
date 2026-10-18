import datetime

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
# options.add_argument("--headless=") #запускает браузер в headless режиме, то есть без открытия окна
g = Service()
driver = webdriver.Chrome(options=options, service=g)

url = 'https://the-internet.herokuapp.com/javascript_alerts'
driver.get(url)
driver.maximize_window()
time.sleep(3)
new_alert_button = driver.find_element(By.XPATH, '//button[@onclick="jsAlert()"]')
new_alert_button.click()
driver.switch_to.alert.text # получение текста с попапа
driver.switch_to.alert.accept()  # подтверждение действия на попапе
# driver.switch_to.alert.dismiss()  # отклонение действия на попапе
# driver.switch_to.alert.send_keys("text") # ввод текста в попап 
