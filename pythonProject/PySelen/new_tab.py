import datetime

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
#options.add_argument("--headless=") #запускает браузер в headless режиме, то есть без открытия окна
g = Service()
driver = webdriver.Chrome(options=options, service=g)


url = 'https://demoqa.com/browser-windows'
driver.get(url)
driver.maximize_window()
new_tab_button = driver.find_element(By.XPATH, '//button[@id="tabButton"]')
new_window_button = driver.find_element(By.XPATH, '//button [@id="windowButton"]')
new_tab_button.click()
tab_0 = driver.window_handles[0]
tab_1 = driver.window_handles[1] # window_handles[1] - указатель на новую вкладку
driver.switch_to.window(tab_1)
driver.switch_to.window(tab_0)
new_window_button.click()
window_1 = driver.window_handles[2]
driver.switch_to.window(window_1)
driver.close()

