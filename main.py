from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
from selenium.webdriver.common.by import By

# Указываем XPATH каждой кнопки на которую будем нажимать
# Example
XPATH_one = '//*[@id="i5"]/div[3]/div'
XPATH_two = '//*[@id="i16"]/div[2]'
XPATH_three = '//*[@id="i32"]/div[3]/div'
XPATH_four = '//*[@id="i42"]/div[3]/div'
XPATH_five = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div[2]/textarea'
XPATH_six = '//*[@id="i59"]/div[3]/div'
XPATH_seven = '//*[@id="i66"]/div[3]/div'
XPATH_submit = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div'


n = int(input('Введите кол-во итераций: '))
url = input('Введите url: ')

# Функция принимает n - кол-во итераций и url ссылку на гугл форму
def autofill_google(n=n, url=url):
    # Делаем счетчик и переменную для ввода url
    count = 0
    # Цикл накрутки n раз
    while count < n:


        # Открываем браузер Chrome
        driver = webdriver.Chrome()
        # Открывем страницу
        driver.get(url)
            #"https://docs.google.com/forms/d/e/1FAIpQLSes2WhQtgPqq4MChEG9fsKXXAJog2t-DxJFtcoV3QNCJ1KCeg/viewform?pli=1")

        # Создали переменную, которую будем указывать при нажатии
        # Example
        radio_buttons_one = driver.find_element(By.XPATH,XPATH_one)
        radio_buttons_two = driver.find_element(By.XPATH,XPATH_two)
        radio_buttons_three = driver.find_element(By.XPATH,XPATH_three)
        radio_buttons_four = driver.find_element(By.XPATH,XPATH_four)
        radio_buttons_five = driver.find_element(By.XPATH,XPATH_five)
        radio_buttons_six = driver.find_element(By.XPATH,XPATH_six)
        radio_buttons_seven = driver.find_element(By.XPATH,XPATH_seven)
        submit = driver.find_element(By.XPATH,XPATH_submit)

        # Нажимаем
        # Example
        radio_buttons_one.click()
        radio_buttons_two.click()
        radio_buttons_three.click()
        radio_buttons_four.click()
        radio_buttons_five.click()
        radio_buttons_six.click()
        radio_buttons_seven.click()
        submit.click()

        # Закрывем браузер
        driver.quit()

        # Прибавляем счетчик
        count = count + 1

# Example
autofill_google()