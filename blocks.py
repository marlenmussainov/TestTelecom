from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time 

# Данный тест проверяет наличие основных блоков на сайте "telecom.kz"

# переход на страницу "telecom.kz"
browser = webdriver.Chrome()
browser.get("https://telecom.kz/")

# тайм-аут для загрузки элементов страницы
time.sleep(2)

# счетчик для финального вердикта о наличии всех блоков
count = 0

# проверка наличия шапки сайта
try:
    browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/header')
    print("Шапка сайта присутствует")
    count += 1
except NoSuchElementException:
    print("Шапка сайта отсутствует")

# проверка наличия блока со слайдами   
try:    
    browser.find_element(By.CLASS_NAME, 'one-carusel-slide')
    print("Блок со слайдами присутствует")
    count += 1
except NoSuchElementException:
    print("Блок со слайдами отсутствует")

# проверка наличия блока "Онлайн каналы связи" 
try:
    browser.find_element(By.XPATH, "//div[@class='col-12']")
    print('Блок "Онлайн каналы связи" присутствует')
    count += 1
except NoSuchElementException:
    print('Блок "Онлайн каналы связи" отсутствует')

# проверка наличия блока "Пакеты услуг" 
try:
    browser.find_element(By.XPATH, "//section[@class='new-service-package']")
    print('Блок "Пакеты услуг" присутствует')
    count += 1
except NoSuchElementException:
    print('Блок "Пакеты услуг" отсутствует')

# проверка наличия блока "В магазин" 
try:
    browser.find_element(By.XPATH, "//*[@id='app']/div[2]/main/div[1]/section[4]")
    print('Блок "В магазин" присутствует')
    count += 1
except NoSuchElementException:
    print('Блок "В магазин" отсутствует')

# проверка наличия блока "Сервисы наших партнёров" 
try:
    browser.find_element(By.XPATH, "//div[@class='latest-wrap partner-block']")
    print('Блок "Сервисы наших партнёров" присутствует')
    count += 1
except NoSuchElementException:
    print('Блок "Сервисы наших партнёров" отсутствует')

# проверка наличия блока "Новости компании" 
try:
    browser.find_element(By.XPATH, "//div[@class='py-5']")
    print('Блок "Новости компании" присутствует')
    count += 1
except NoSuchElementException:
    print('Блок "Новости компании" отсутствует')

# проверка наличия блока "Часто задаваемые вопросы" 
try:
    browser.find_element(By.XPATH, "//div[@class='knowledge-wrap']")
    print('Блок "Часто задаваемые вопросы" присутствует')
    count += 1
except NoSuchElementException:
    print('Блок "Часто задаваемые вопросы" отсутствует')

# проверка наличия подвала сайта
try:
    browser.find_element(By.CLASS_NAME, "footer")
    print('Подвал сайта присутствует')
    count += 1
except NoSuchElementException:
    print('Подвал сайта отсутствует')

# отображение результата выполнения теста
if count == 9:
    print('Ура! На сайте присутствуют все основные блоки')
else:
    print('Хьюстон, у нас проблемы! На сайте присутствует только', count, 'блока(-ов) из 9')    

# закрытие браузера
browser.quit()