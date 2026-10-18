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


url = 'https://www.saucedemo.com/'
standard_user = 'standard_user'
standard_pwd = 'secret_sauce'
current_date = datetime.datetime.now().strftime('%d.%m.%Y-.%H.%M.%S')
screenshot_name = 'scr ' + current_date + '.png'
screenshot_dir = '/Users/apetrova/PycharmProjects/pythonProject/PySelen/scr/'
driver.get(url)
driver.maximize_window()
login_field = driver.find_element(By.XPATH, "//*[@id='user-name']")
login_field.send_keys(standard_user)
password_field = driver.find_element(By.XPATH,"//*[@id='password']")
password_field.send_keys(standard_pwd)
login_button = driver.find_element(By.XPATH, "//*[@id='login-button']")
login_button.click()

driver.execute_script('window.scrollTo(0, 200)')
actions = ActionChains(driver) #создание экземпляра класса для перемещения по окну браузера
item_3 = driver.find_element(By.ID, 'item_3_title_link')
actions.move_to_element(item_3).perform()

screenshot_name = 'scr ' + current_date + '.png'
driver.save_screenshot(screenshot_dir + screenshot_name)