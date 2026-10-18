import datetime
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)

# Data for testing
url = 'https://demoqa.com/date-picker'
current_date = datetime.datetime.now()
add_days = datetime.timedelta(days=10)
future_date = (str(current_date + add_days))[:10]

# Enter current date+10 days into Select Date field
driver.get(url)
date_field = driver.find_element(By.XPATH, '//input[@id="datePickerMonthYearInput"]')
date_field.send_keys(Keys.COMMAND + "a")
date_field.send_keys(Keys.DELETE)
date_field.send_keys(future_date)
date_field.send_keys(Keys.ENTER)
print(f'Date {future_date } entered in Select Date field')