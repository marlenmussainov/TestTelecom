from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.common.exceptions import NoSuchElementException

# Данный тест проверяет весь путь для успешного оставления заявки 

# Переход на страницу "telecom.kz/ru/technical-check"
browser = webdriver.Chrome()
browser.get("https://telecom.kz/ru/technical-check")

# Тайм-аут для загрузки элементов страницы
time.sleep(2)

# Заполнение полей страницы
browser.find_element(By.NAME, 'town_state_id').send_keys("Астана")
browser.find_element(By.XPATH, "//*[@class='menu visible']").click()
browser.find_element(By.NAME, 'street').send_keys("753")
time.sleep(1)
browser.find_element(By.XPATH, "//*[@class='menu visible']").click()
browser.find_element(By.NAME, 'house').send_keys("1")

# Клик по кнопке "Проверить"
browser.find_element(By.XPATH, '//*[@class="btn btn-rounded btn-primary btn-lg btn-block"]').click()
time.sleep(1)

# Проверка наличия успешного модального окна 'У вас есть техническая возможность'
try:    
    browser.find_element(By.ID, "resultStatus___BV_modal_content_")
    print("Модальное окно о наличии технической возможности отображается")
except NoSuchElementException:
    print("Модальное окно о наличии технической возможности не отображается")

# Клик по кнопке "Подключить"
browser.find_element(By.XPATH, "//*[@class='btn btn-rounded btn-primary']").click()

# Проверка наличия модального окна 'Оставить заявку'
try:    
    browser.find_element(By.ID, "potential___BV_modal_content_")
    print("Модальное окно 'Оставить заявку' отображается")
except NoSuchElementException:
    print("Модальное окно 'Оставить заявку' не отображается")

# Ввод номера телефона
browser.find_element(By.ID, 'phone_number').send_keys("7078709076")  

# Проверка наличия ошибок с номером телефона
try:    
    browser.find_element(By.XPATH, "//small[@class='text-danger form-text']")
    print("Ошибок с номером телефона нет")
except NoSuchElementException:
    print("Ошибки с номером телефона есть")

browser.quit()     