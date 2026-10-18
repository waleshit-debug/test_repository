import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# login_url_1 = 'https://demoqa.com/checkbox'
#
# driver.get(login_url_1)
# chevron_1 = driver.find_element(By.XPATH, '//button[@aria-label="Toggle"]')
# chevron_1.click()
# check_box = driver.find_element(By.XPATH, '(//span[@class="rct-checkbox"])[2]')
# check_box.click()
# if check_box.is_selected():
#     print("Чек-бокс выбран")

login_url_2 = 'https://demoqa.com/radio-button'

driver.get(login_url_2)
radio_1 = driver.find_element(By.XPATH, '//input[@id="impressiveRadio"]')
radio_1.click()
if radio_1.is_selected():
    print("Радиокнопка прожата")
