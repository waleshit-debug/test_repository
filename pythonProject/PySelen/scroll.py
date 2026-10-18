import datetime
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
actions = ActionChains(driver) # создание экземпляра класса для перемещения по окну браузера

login_url = 'https://html5css.ru/howto/howto_js_rangeslider.php'
driver.get(login_url)
slider = driver.find_element(By.XPATH, "//input[@class='slider-square']")

actions.click_and_hold(slider).move_by_offset(-50, 0).release().perform()