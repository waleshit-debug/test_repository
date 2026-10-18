# Явное ожидание
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PySelen.Calendar import driver

element = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "my_element")))

# WebDriverWait - это класс, используется для ожидания определенного условия в течения заданного времени.
# Используется для явного ожидания или выполнения определенного условия перед продолжением выполнения кода.
# Работает в сочетании с expected_conditions, которые определяют, какое условие должно быть выполнено, чтобы продолжить исполнение кода

# Неявное ожидание
driver.implicitly_wait(10)
element = driver.find_element(By.XPATH, "my_element")

# implicitly_wait(10) указывает Selenium WebDriver ожидать до 10 секунд при поиске элементов на странице.

