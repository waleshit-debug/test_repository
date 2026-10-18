import datetime
import glob
import os  # импортируем в проект библиотеку OS для работы с директориями и файлами системы

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

path_upload = "/Users/apetrova/PycharmProjects/pythonProject/PySelen/smoke.py"
path_download = "/Users/apetrova/Documents"

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
# options.add_argument("--headless=") #запускает браузер в headless режиме, то есть без открытия окна
prefs = {'download.default_directory': path_download}
options.add_experimental_option('prefs', prefs)
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)

url_upload = 'https://www.lambdatest.com/selenium-playground/upload-file-demo'
url_download = 'https://www.lambdatest.com/selenium-playground/download-file-demo'
# driver.get(url_upload)
driver.get(url_download)
driver.maximize_window()
time.sleep(3)

# upload_button = driver.find_element(By.XPATH, '//input[@id="file"]')
download_button = driver.find_element(By.XPATH, '//button[@class="btn btn-primary"]')
# upload_button.send_keys(path_upload)
download_button.click()
print('click button')

file_name = 'LambdaTest.pdf'
file_path = path_download + file_name
assert os.access(file_path, os.F_OK) == True  # проведение проверки на наличие файла
print("Файл в директории")

# проверка на то, что файл не пуст
files = glob.glob(os.path.join(path_download, '*.*'))

for file in files:
    a = os.path.getsize(file_name)
    if a > 10:
        print('file not empty')
    else:
        print('file empty')

# удаление файла
files = glob.glob(os.path.join(path_download,'*.*'))
for file in files:
        os.remove(file)