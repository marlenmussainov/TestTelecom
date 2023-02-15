from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.common.exceptions import NoSuchElementException

# Данный тест проверяет модалку "К сожалению, у вас нет технической возможности подключения оптоволоконного интернет" и поле 'Дробь дома'

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

# Ввод несуществующего дома
browser.find_element(By.NAME, 'house').send_keys("11")

# Клик по кнопке "Проверить"
browser.find_element(By.XPATH, '//*[@class="btn btn-rounded btn-primary btn-lg btn-block"]').click()
time.sleep(1)

# Проверка наличия ошибочного модального окна 'К сожалению, у вас нет технической возможности подключения оптоволоконного интернет'
try:    
    browser.find_element(By.ID, "resultStatusCanceled___BV_modal_content_")
    print("Модальное окно об отсутствии технической возможности подключения отображается для неподходящего адреса")
except NoSuchElementException:
    print("Модальное окно об отсутствии технической возможности подключения не отображается для неподходящего адреса")

# Проверка ссылки 'Megaline'
element = browser.find_element(By.XPATH, "//*[@class='btn btn-rounded mr-3 btn-primary']")
if element.get_attribute('href') == 'https://telecom.kz/ru/common/ultra?adsl=1':
    print('Ссылка "Megaline" корректная')
else:
    print('Ссылка "Megaline" некорректная') 

# Проверка ссылки 'Altel 4G'
element = browser.find_element(By.XPATH, "//*[@class='btn btn-rounded ml-3 btn-primary']")
if element.get_attribute('href') == 'https://telecom.kz/ru/common/altel4g':
    print('Ссылка "Altel 4G" корректная')
else:
    print('Ссылка "Altel 4G" некорректная') 

#Закрытие модального окна
browser.find_element_by_xpath("//*[.='×']").click()

#Ввод специальных символов в поле "Дробь дома"
browser.find_element(By.NAME, 'sub_house').send_keys("$#%^&*")

# Клик по кнопке "Проверить"
browser.find_element(By.XPATH, '//*[@class="btn btn-rounded btn-primary btn-lg btn-block"]').click()

# Проверка отсутствия отображения модального окна
try:    
    browser.find_element(By.ID, "resultStatusCanceled___BV_modal_content_") or browser.find_element(By.ID, "resultStatus___BV_modal_content_")
    print("Модальное окно отображается при вводе спец. символов в поле 'Дробь дома'")
except NoSuchElementException:
    print("Модальное окно не отображается при вводе спец. символов в поле 'Дробь дома'")

browser.quit()     