from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.common.exceptions import NoSuchElementException

# Негативная проверка поля "Номер телефона" на странице "Оставить заявку" 

# Предусловие для попадания на страницу 'Оставить заявку'
browser = webdriver.Chrome()
browser.get("https://telecom.kz/ru/technical-check")
time.sleep(2)
browser.find_element(By.NAME, 'town_state_id').send_keys("Астана")
browser.find_element(By.XPATH, "//*[@class='menu visible']").click()
browser.find_element(By.NAME, 'street').send_keys("753")
time.sleep(1)
browser.find_element(By.XPATH, "//*[@class='menu visible']").click()
browser.find_element(By.NAME, 'house').send_keys("1")
browser.find_element(By.XPATH, '//*[@class="btn btn-rounded btn-primary btn-lg btn-block"]').click()
time.sleep(1)
browser.find_element(By.XPATH, "//*[@class='btn btn-rounded btn-primary']").click()

# Кейс 1. Не вводить номер телефона и кликнуть по кнопке 'Далее'
time.sleep(1)
browser.find_element(By.XPATH, "//*[@class='btn btn-primary']").click()

# Проверка отображения ошибки 'Поле "Номер телефона:" обязательно для заполнения.'
try:    
    browser.find_element(By.XPATH, "//small[contains(text(), 'обязательно для заполнения')]")
    print('Ошибка "Поле "Номер телефона:" обязательно для заполнения." отображается')
except NoSuchElementException:
    print('Ошибка "Поле "Номер телефона:" обязательно для заполнения." не отображается')


# Кейс 2. Ввести неполный номер телефона
browser.find_element(By.ID, 'phone_number').send_keys("11111111")  

# Проверка отображения ошибки 'Поле "Номер телефона:" должно быть не менее 10 символов.'
try:    
    browser.find_element(By.XPATH, "//small[contains(text(), 'должно быть не менее 10 символов.')]")
    print('Ошибка "Поле "Номер телефона:" должно быть не менее 10 символов." отображается')
except NoSuchElementException:
    print('Ошибка "Поле "Номер телефона:" должно быть не менее 10 символов." не отображается')


# Кейс 3. Ввести некорректный номер телефона
browser.find_element(By.ID, 'phone_number').send_keys("1111111111")  

# Проверка отображения ошибки 'Введен некорректный мобильный номер'
try:    
    browser.find_element(By.XPATH, "//small[contains(text(), 'Введен некорректный мобильный номер')]")
    print('Ошибка "Введен некорректный мобильный номер" отображается')
except NoSuchElementException:
    print('Ошибка "Введен некорректный мобильный номер" не отображается')

browser.quit()     