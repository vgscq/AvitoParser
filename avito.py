from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import ctypes
import clipboard
import sys

link = 'https://www.avito.ru/sankt-peterburg/telefony/xiaomi?user=1&q=xiaomi+mi+max&s=104' #Введте в поиске авито все нужные параметры и скопируйте ссылку сюда.

def init():
    options = Options()
    options.add_argument('--headless') #Запуск в скрытом режиме
    options.add_argument('--start-maximized')
    options.add_argument('--ignore-certificate-errors') #Возможно понадобится при работе с ВПН
    options.add_argument('--disable-popup-blocking') # Не даем спрашивать сайтам разрешение на показ всплывающих окон
    #options.add_extension('D:/SOFT/program/avito_parse/ublock.crx') #Если в выдаче попадается реклама раскомментируйте строку и добавьте полный путь до блокировщика

    options.binary_location = "D:/SOFT/GoogleChromePortable/App/Chrome-bin/chrome.exe" #путь до хрома
    driver = webdriver.Chrome(options=options, executable_path="chromedriver.exe", ) #путь до хромдрайвера, поставляется с репозиторием, но может понадобиться более новая версия
    return driver

def main(driver):
    driver.get(link)

    elements = driver.find_elements_by_xpath('/html/body/div[4]/div[1]/div[5]/div[2]/div[2]/div[1]')[0]
    #elements = elements.text.strip('\n')
    name = elements.find_element_by_class_name('item-description-title-link').text
    price = elements.find_element_by_class_name('price').text
    metro = elements.find_element_by_class_name('data').text.split('\n')
    date = metro[1].split(' ')
    metro = metro[0]
    href = elements.find_element_by_class_name('item-description-title-link').get_attribute('href')

    if date[1].startswith('час') or date[1].startswith('день') or int(date[0]) > 5:
        print('Новых объявлений нет.')
        sys.exit()

    driver.get(href) #переходим на страницу заинтересовавшего нас товара

    #image_url = driver.find_element_by_class_name('gallery-img-cover').get_attribute('style')[25:-3]
    #description = driver.find_element_by_class_name('item-description-text') #получение картинки работает через раз, надо разбираться почему. !!!TODO!!!
    description = driver.find_element_by_xpath("//div[contains(@class, 'item-description-text')]/p").text

    print('{} | {}\n{}\n{}\n{}'.format(name, price, metro, date, description))
    if ctypes.windll.user32.MessageBoxW(0, '{} | {}\n{}\n{}\n{}'.format(name, price, metro, '{} {} {}'.format(date[0], date[1], date[2]), description), 'Парсер авито', 1):
        clipboard.copy(href)

    driver.close()

if __name__ == "__main__":
    main(init())