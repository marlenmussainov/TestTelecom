from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

# Данный тест проверяет ссылки футера и хедера сайта "telecom.kz"

browser = webdriver.Chrome()

# Проверка ссылки "Частным лицам"
browser.get("https://telecom.kz/ru/services/mobile")
browser.find_elements_by_class_name("toppanel__link")[0].click()
if browser.current_url == 'https://telecom.kz/ru/':
    print('Ссылка "Частным лицам" корректная')
else:
    print('Ссылка "Частным лицам" некорректная', browser.current_url)

# Проверка ссылки "Бизнесу"
browser.find_elements_by_class_name("toppanel__link")[1].click()
if browser.current_url == 'https://www.ismet.kz/ru/documents/telecom-services?utm_source=telecom&utm_medium=transfer_rus&utm_campaign=for_business':
    print('Ссылка "Бизнесу" корректная')
else:
    print('Ссылка "Бизнесу" некорректная')

# Проверка ссылки "О компании"
browser.get("https://telecom.kz/")
browser.find_elements_by_class_name("toppanel__link")[2].click()
if browser.current_url == 'https://telecom.kz/ru/about/list':
    print('Ссылка "О компании" корректная')
else:
    print('Ссылка "О компании" некорректная')

# Проверка ссылки "Инвесторам и акционерам"
browser.get("https://telecom.kz/")
browser.find_elements_by_class_name("toppanel__link")[3].click()
if browser.current_url == 'https://telecom.kz/ru/pages/11893/172452':
    print('Ссылка "Инвесторам и акционерам" корректная')
else:
    print('Ссылка "Инвесторам и акционерам" некорректная')

# Проверка ссылки "Контакты"
browser.get("https://telecom.kz/")
browser.find_elements_by_class_name("toppanel__link")[4].click()
if browser.current_url == 'https://telecom.kz/ru/contacts/list':
    print('Ссылка "Контакты" корректная')
else:
    print('Ссылка "Контакты" некорректная')

# Проверка ссылки "Мобильное приложение"
browser.get("https://telecom.kz/")
browser.find_elements_by_class_name("toppanel__link")[5].click()
if browser.current_url == 'https://telecom.kz/ru/services/mobile':
    print('Ссылка "Мобильное приложение" корректная')
else:
    print('Ссылка "Мобильное приложение" некорректная')    

# Проверка ссылки "Магазин"
browser.get("https://telecom.kz/")
element = browser.find_elements_by_class_name("main-menu__navigation-link")[0]
if element.get_attribute('href') == 'https://shop.telecom.kz/?utm_source=websitetelecomkz&utm_medium=shopbutton&utm_campaign=referral&utm_id=telecom':
    print('Ссылка "Магазин" корректная')
else:
    print('Ссылка "Магазин" некорректная') 

# Проверка ссылки "Интернет"
browser.get("https://telecom.kz/")
browser.find_elements_by_class_name("main-menu__navigation-link")[1].click()
if browser.current_url == 'https://telecom.kz/ru/common/internet':
    print('Ссылка "Интернет" корректная')
else:
    print('Ссылка "Интернет" некорректная')  

# Проверка ссылки "Телевидение"
browser.get("https://telecom.kz/")
browser.find_elements_by_class_name("main-menu__navigation-link")[2].click()
if browser.current_url == 'https://telecom.kz/ru/common/tvplus':
    print('Ссылка "Телевидение" корректная')
else:
    print('Ссылка "Телевидение" некорректная')  

# Проверка ссылки "Телефон"
browser.get("https://telecom.kz/")
browser.find_elements_by_class_name("main-menu__navigation-link")[3].click()
if browser.current_url == 'https://telecom.kz/ru/common/mobsvyaz-altel':
    print('Ссылка "Телефон" корректная')
else:
    print('Ссылка "Телефон" некорректная')  

# Проверка ссылки "Помощь"
browser.get("https://telecom.kz/")
browser.find_elements_by_class_name("main-menu__navigation-link")[4].click()
if browser.current_url == 'https://telecom.kz/ru/knowledge/14':
    print('Ссылка "Помощь" корректная')
else:
    print('Ссылка "Помощь" некорректная')          

# Проверка ссылки "Новые услуги"
browser.get("https://telecom.kz/")
browser.find_elements_by_class_name("main-menu__navigation-link")[5].click()
if browser.current_url == 'https://telecom.kz/ru/services/volte':
    print('Ссылка "Новые услуги" корректная')
else:
    print('Ссылка "Новые услуги" некорректная')     

# Проверка ссылки "Интернет"
browser.get("https://telecom.kz/")
time.sleep(5)
browser.find_element(By.XPATH, "(//*[@class='col-sm-6 col-lg-2']//a)[1]").click()
if browser.current_url == 'https://telecom.kz/ru/common/idnet':
    print('Ссылка "Интернет" корректная')
else:
    print('Ссылка "Интернет" некорректная')  

# Проверка ссылки "Телевидение"
browser.get("https://telecom.kz/")
time.sleep(5)
browser.find_element(By.XPATH, "(//*[@class='col-sm-6 col-lg-2']//a)[2]").click()
if browser.current_url == 'https://telecom.kz/ru/common/id-tv':
    print('Ссылка "Телевидение" корректная')
else:
    print('Ссылка "Телевидение" некорректная')  

# Проверка ссылки "Телефон"
browser.get("https://telecom.kz/")
time.sleep(5)
browser.find_element(By.XPATH, "(//*[@class='col-sm-6 col-lg-2']//a)[3]").click()
if browser.current_url == 'https://telecom.kz/ru/common/vugodnaya-mobil-svyazi':
    print('Ссылка "Телефон" корректная')
else:
    print('Ссылка "Телефон" некорректная') 

# Проверка ссылки "Новые услуги"
browser.get("https://telecom.kz/")
time.sleep(5)
browser.find_element(By.XPATH, "(//*[@class='col-sm-6 col-lg-2']//a)[4]").click()
if browser.current_url == 'https://telecom.kz/ru/services/cctv-home':
    print('Ссылка "Новые услуги" корректная')
else:
    print('Ссылка "Новые услуги" некорректная')     

# Проверка ссылки "Помощь"
browser.get("https://telecom.kz/")
time.sleep(5)
browser.find_element(By.XPATH, "(//*[@class='col-sm-6 col-lg-2']//a)[5]").click()
if browser.current_url == 'https://telecom.kz/ru/knowledge/14':
    print('Ссылка "Помощь" корректная')
else:
    print('Ссылка "Помощь" некорректная') 

# Проверка ссылки "Личный кабинет"
browser.get("https://telecom.kz/")
time.sleep(5)
browser.find_element(By.XPATH, "(//*[@class='col-sm-6 col-lg-2']//a)[6]").click()
if browser.current_url == 'https://telecom.kz/ru/customer/auth/login':
    print('Ссылка "Личный кабинет" корректная')
else:
    print('Ссылка "Личный кабинет" некорректная') 

# Проверка ссылки "Хостинг"
browser.get("https://telecom.kz/")
time.sleep(5)
browser.find_element(By.XPATH, "(//*[@class='col-sm-6 col-lg-2']//a)[7]").click()
if browser.current_url == 'https://www.ismet.kz/ru/id-host.html':
    print('Ссылка "Хостинг" корректная')
else:
    print('Ссылка "Хостинг" некорректная') 

# Проверка ссылки "Unibox"
browser.get("https://telecom.kz/")
time.sleep(5)
browser.find_element(By.XPATH, "(//*[@class='col-sm-6 col-lg-2']//a)[8]").click()
if browser.current_url == 'https://www.ismet.kz/ru/services/service-3762-unibox':
    print('Ссылка "Unibox" корректная')
else:
    print('Ссылка "Unibox" некорректная') 

# Проверка ссылки "Интернет"
browser.get("https://telecom.kz/")
time.sleep(5)
browser.find_element(By.XPATH, "(//*[@class='col-sm-6 col-lg-2']//a)[9]").click()
if browser.current_url == 'https://www.ismet.kz/content/ocp/ru/documents/internet-dlya-biznesa.html':
    print('Ссылка "Интернет" корректная')
else:
    print('Ссылка "Интернет" некорректная') 

# Проверка ссылки "Телефония"
browser.get("https://telecom.kz/")
time.sleep(5)
browser.find_element(By.XPATH, "(//*[@class='col-sm-6 col-lg-2']//a)[10]").click()
if browser.current_url == 'https://www.ismet.kz/ru/services/service-3717-siptelefonija.html':
    print('Ссылка "Телефония" корректная')
else:
    print('Ссылка "Телефония" некорректная') 

# Проверка ссылки "Телевидение"
browser.get("https://telecom.kz/")
time.sleep(5)
browser.find_element(By.XPATH, "(//*[@class='col-sm-6 col-lg-2']//a)[11]").click()
if browser.current_url == 'https://www.ismet.kz/ru/services/service-3353-id_tvdljaofisa':
    print('Ссылка "Телевидение" корректная')
else:
    print('Ссылка "Телевидение" некорректная') 

# Проверка ссылки "Видеонаблюдение"
browser.get("https://telecom.kz/")
time.sleep(5)
browser.find_element(By.XPATH, "(//*[@class='col-sm-6 col-lg-2']//a)[12]").click()
if browser.current_url == 'https://www.ismet.kz/ru/documents/cctv':
    print('Ссылка "Видеонаблюдение" корректная')
else:
    print('Ссылка "Видеонаблюдение" некорректная') 

# Проверка ссылки "Wi-Fi Target"
browser.get("https://telecom.kz/")
time.sleep(5)
browser.find_element(By.XPATH, "(//*[@class='col-sm-6 col-lg-2']//a)[13]").click()
if browser.current_url == 'https://www.ismet.kz/ru/documents/wi-fi-target':
    print('Ссылка "Wi-Fi Target" корректная')
else:
    print('Ссылка "Wi-Fi Target" некорректная') 

# Проверка ссылки "IoT Интернет вещей"
browser.get("https://telecom.kz/")
time.sleep(5)
browser.find_element(By.XPATH, "(//*[@class='col-sm-6 col-lg-2']//a)[14]").click()
if browser.current_url == 'https://www.ismet.kz/ru/documents/IoT':
    print('Ссылка "IoT Интернет вещей" корректная')
else:
    print('Ссылка "IoT Интернет вещей" некорректная') 

# Проверка ссылки "Блокчейн"
browser.get("https://telecom.kz/")
time.sleep(5)
browser.find_element(By.XPATH, "(//*[@class='col-sm-6 col-lg-2']//a)[15]").click()
if browser.current_url == 'https://www.ismet.kz/ru/documents/blockchain':
    print('Ссылка "Блокчейн" корректная')
else:
    print('Ссылка "Блокчейн" некорректная') 
    
 # Проверка ссылки "Операторам"
browser.get("https://telecom.kz/")
time.sleep(5)
browser.find_element(By.XPATH, "(//*[@class='col-sm-6 col-lg-2']//a)[16]").click()
if browser.current_url == 'https://telecom.kz/ru/operators/12219/172065':
    print('Ссылка "Операторам" корректная')
else:
    print('Ссылка "Операторам" некорректная')    
    
# Проверка ссылки "Новости компании"
browser.get("https://telecom.kz/")
time.sleep(5)
browser.find_element(By.XPATH, "(//*[@class='col-sm-6 col-lg-2']//a)[17]").click()
if browser.current_url == 'https://telecom.kz/ru/news/list/1?utm_source=footer&utm_medium=org&utm_campaign=newlink':
    print('Ссылка "Новости компании" корректная')
else:
    print('Ссылка "Новости компании" некорректная') 

# Проверка ссылки "Новости телевидения"
browser.get("https://telecom.kz/")
time.sleep(5)
browser.find_element(By.XPATH, "(//*[@class='col-sm-6 col-lg-2']//a)[18]").click()
if browser.current_url == 'https://telecom.kz/ru/news/list/11?utm_source=footer&utm_medium=org&utm_campaign=newlink':
    print('Ссылка "Новости телевидения" корректная')
else:
    print('Ссылка "Новости телевидения" некорректная') 
    
# Проверка ссылки "Публикации"
browser.get("https://telecom.kz/")
time.sleep(5)
browser.find_element(By.XPATH, "(//*[@class='col-sm-6 col-lg-2']//a)[19]").click()
if browser.current_url == 'https://telecom.kz/ru/news/list/3?utm_source=footer&utm_medium=org&utm_campaign=newlink':
    print('Ссылка "Публикации" корректная')
else:
    print('Ссылка "Публикации" некорректная') 

# Проверка ссылки "Видеоархив"
browser.get("https://telecom.kz/")
time.sleep(5)
browser.find_element(By.XPATH, "(//*[@class='col-sm-6 col-lg-2']//a)[20]").click()
if browser.current_url == 'https://telecom.kz/ru/news/list/6?utm_source=footer&utm_medium=org&utm_campaign=newlink':
    print('Ссылка "Видеоархив" корректная')
else:
    print('Ссылка "Видеоархив" некорректная') 

# Проверка ссылки "Фотоархив"
browser.get("https://telecom.kz/")
time.sleep(5)
browser.find_element(By.XPATH, "(//*[@class='col-sm-6 col-lg-2']//a)[21]").click()
if browser.current_url == 'https://telecom.kz/ru/news/list/7?utm_source=footer&utm_medium=org&utm_campaign=newlink':
    print('Ссылка "Фотоархив" корректная')
else:
    print('Ссылка "Фотоархив" некорректная') 

# Проверка ссылки "Операторам связи"
browser.get("https://telecom.kz/")
time.sleep(5)
browser.find_element(By.XPATH, "(//*[@class='col-sm-6 col-lg-2']//a)[22]").click()
if browser.current_url == 'https://telecom.kz/ru/news/list/9?utm_source=footer&utm_medium=org&utm_campaign=newlink':
    print('Ссылка "Операторам связи" корректная')
else:
    print('Ссылка "Операторам связи" некорректная') 

# Проверка ссылки "Оповещения о проведении технических работ"
browser.get("https://telecom.kz/")
time.sleep(5)
browser.find_element(By.XPATH, "(//*[@class='col-sm-6 col-lg-2']//a)[23]").click()
if browser.current_url == 'https://telecom.kz/ru/news/list/12?utm_source=footer&utm_medium=org&utm_campaign=newlink':
    print('Ссылка "Оповещения о проведении технических работ" корректная')
else:
    print('Ссылка "Оповещения о проведении технических работ" некорректная') 

# Проверка ссылки "Контакты для СМИ"
browser.get("https://telecom.kz/")
time.sleep(5)
browser.find_element(By.XPATH, "(//*[@class='col-sm-6 col-lg-2']//a)[24]").click()
if browser.current_url == 'https://telecom.kz/ru/pages/11853/171985':
    print('Ссылка "Контакты для СМИ" корректная')
else:
    print('Ссылка "Контакты для СМИ" некорректная') 

# Проверка ссылки "О компании"
browser.get("https://telecom.kz/")
time.sleep(5)
browser.find_element(By.XPATH, "(//*[@class='col-sm-6 col-lg-2']//a)[25]").click()
if browser.current_url == 'https://telecom.kz/ru/about/list?utm_source=footer&utm_medium=org&utm_campaign=newlink':
    print('Ссылка "О компании" корректная')
else:
    print('Ссылка "О компании" некорректная') 

# Проверка ссылки "О нас"
browser.get("https://telecom.kz/")
time.sleep(5)
browser.find_element(By.XPATH, "(//*[@class='col-sm-6 col-lg-2']//a)[26]").click()
if browser.current_url == 'https://telecom.kz/ru/pages/12090/171731?utm_source=footer&utm_medium=org&utm_campaign=newlink':
    print('Ссылка "О нас" корректная')
else:
    print('Ссылка "О нас" некорректная') 

# Проверка ссылки "Бизнес"
browser.get("https://telecom.kz/")
time.sleep(5)
browser.find_element(By.XPATH, "(//*[@class='col-sm-6 col-lg-2']//a)[27]").click()
if browser.current_url == 'https://telecom.kz/ru/pages/11843/160211?utm_source=footer&utm_medium=org&utm_campaign=newlink':
    print('Ссылка "Бизнес" корректная')
else:
    print('Ссылка "Бизнес" некорректная') 

# Проверка ссылки "Кадровая политика"
browser.get("https://telecom.kz/")
time.sleep(5)
browser.find_element(By.XPATH, "(//*[@class='col-sm-6 col-lg-2']//a)[28]").click()
if browser.current_url == 'https://telecom.kz/ru/pages/11859/172331?utm_source=footer&utm_medium=org&utm_campaign=newlink':
    print('Ссылка "Кадровая политика" корректная')
else:
    print('Ссылка "Кадровая политика" некорректная') 

# Проверка ссылки "Инвесторам и акционерам"
browser.get("https://telecom.kz/")
time.sleep(5)
browser.find_element(By.XPATH, "(//*[@class='col-sm-6 col-lg-2']//a)[29]").click()
if browser.current_url == 'https://telecom.kz/ru/pages/11893/172452?utm_source=footer&utm_medium=org&utm_campaign=newlink':
    print('Ссылка "Инвесторам и акционерам" корректная')
else:
    print('Ссылка "Инвесторам и акционерам" некорректная') 

# Проверка ссылки "Комплаенс"
browser.get("https://telecom.kz/")
time.sleep(5)
browser.find_element(By.XPATH, "(//*[@class='col-sm-6 col-lg-2']//a)[30]").click()
if browser.current_url == 'https://telecom.kz/ru/pages/13695/172465?utm_source=footer&utm_medium=org&utm_campaign=newlink':
    print('Ссылка "Комплаенс" корректная')
else:
    print('Ссылка "Комплаенс" некорректная') 

# Проверка ссылки "Контакты"
browser.get("https://telecom.kz/")
time.sleep(5)
browser.find_element(By.XPATH, "(//*[@class='col-sm-6 col-lg-2']//a)[31]").click()
if browser.current_url == 'https://telecom.kz/ru/contacts/list':
    print('Ссылка "Контакты" корректная')
else:
    print('Ссылка "Контакты" некорректная') 

# Проверка ссылки "Закупки"
browser.get("https://telecom.kz/")
time.sleep(5)
browser.find_element(By.XPATH, "(//*[@class='col-sm-6 col-lg-2']//a)[32]").click()
if browser.current_url == 'https://telecom.kz/ru/purchases?utm_source=footer&utm_medium=org&utm_campaign=newlink':
    print('Ссылка "Закупки" корректная')
else:
    print('Ссылка "Закупки" некорректная') 

# Проверка ссылки "Аукционы"
browser.get("https://telecom.kz/")
time.sleep(5)
browser.find_element(By.XPATH, "(//*[@class='col-sm-6 col-lg-2']//a)[33]").click()
if browser.current_url == 'https://telecom.kz/ru/auction?utm_source=footer&utm_medium=org&utm_campaign=newlink':
    print('Ссылка "Аукционы" корректная')
else:
    print('Ссылка "Аукционы" некорректная') 

# Проверка ссылки "Архив"
browser.get("https://telecom.kz/")
time.sleep(5)
browser.find_element(By.XPATH, "(//*[@class='col-sm-6 col-lg-2']//a)[34]").click()
if browser.current_url == 'https://telecom.kz/ru/pages/12463/172279?utm_source=footer&utm_medium=org&utm_campaign=newlink':
    print('Ссылка "Архив" корректная')
else:
    print('Ссылка "Архив" некорректная') 

# Проверка ссылки "База знаний"
browser.get("https://telecom.kz/")
time.sleep(5)
browser.find_element(By.XPATH, "(//*[@class='col-sm-6 col-lg-2']//a)[35]").click()
if browser.current_url == 'https://telecom.kz/ru/knowledge/14?utm_source=footer&utm_medium=org&utm_campaign=newlink':
    print('Ссылка "База знаний" корректная')
else:
    print('Ссылка "База знаний" некорректная') 

# Проверка ссылки "Бланки и документы"
browser.get("https://telecom.kz/")
time.sleep(5)
browser.find_element(By.XPATH, "(//*[@class='col-sm-6 col-lg-2']//a)[36]").click()
if browser.current_url == 'https://telecom.kz/ru/knowledge/13?utm_source=footer&utm_medium=org&utm_campaign=newlink':
    print('Ссылка "Бланки и документы" корректная')
else:
    print('Ссылка "Бланки и документы" некорректная') 

# Проверка ссылки "Справочник"
browser.get("https://telecom.kz/")
time.sleep(5)
browser.find_element(By.XPATH, "(//*[@class='col-sm-6 col-lg-2']//a)[37]").click()
if browser.current_url == 'https://telecom.kz/ru/catalog/11590/171757?utm_source=footer&utm_medium=org&utm_campaign=newlink':
    print('Ссылка "Справочник" корректная')
else:
    print('Ссылка "Справочник" некорректная')         

# Проверка ссылки "Контакты и адреса"
browser.get("https://telecom.kz/")
time.sleep(5)
browser.find_element(By.XPATH, "(//*[@class='col-sm-6 col-lg-2']//a)[38]").click()
if browser.current_url == 'https://telecom.kz/ru/pages/12263/172099?utm_source=footer&utm_medium=org&utm_campaign=newlink':
    print('Ссылка "Контакты и адреса" корректная')
else:
    print('Ссылка "Контакты и адреса" некорректная') 

# Проверка ссылки "Публичный договор"
browser.get("https://telecom.kz/")
time.sleep(5)
browser.find_element(By.XPATH, "(//*[@class='col-sm-6 col-lg-2']//a)[39]").click()
if browser.current_url == 'https://telecom.kz/ru/publications/172460?utm_source=footer&utm_medium=org&utm_campaign=newlink':
    print('Ссылка "Публичный договор" корректная')
else:
    print('Ссылка "Публичный договор" некорректная') 
    
# Проверка ссылки "Договора для ИП и ЮЛ"
browser.get("https://telecom.kz/")
time.sleep(5)
browser.find_element(By.XPATH, "(//*[@class='col-sm-6 col-lg-2']//a)[40]").click()
if browser.current_url == 'https://telecom.kz/ru/publication/172456':
    print('Ссылка "Договора для ИП и ЮЛ" корректная')
else:
    print('Ссылка "Договора для ИП и ЮЛ" некорректная') 
    
    
# Проверка ссылки "Сертификат безопасности"
browser.get("https://telecom.kz/")
time.sleep(5)
browser.find_element(By.XPATH, "(//*[@class='col-sm-6 col-lg-2']//a)[41]").click()
if browser.current_url == 'https://telecom.kz/ru/publication/172469':
    print('Ссылка "Сертификат безопасности" корректная')
else:
    print('Ссылка "Сертификат безопасности" некорректная') 
    
# Закрытие браузера
browser.quit()