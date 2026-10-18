import time

from selenium.common.exceptions import NoSuchElementException
import datetime

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)


url = 'https://demoqa.com/browser-windows'
driver.get(url)
driver.maximize_window()

try:
    element = driver.find_element(By.XPATH, "my_element")
    element.click()
except NoSuchElementException:
    print('NoSuchElementException')
    time.sleep(5)
    driver.refresh()
    time.sleep(5)
    element = driver.find_element(By.XPATH, 'my_element')
    element.click()
# exeptions list https://www.geeksforgeeks.org/python/exceptions-selenium-python/