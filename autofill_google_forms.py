from selenium import webdriver
from selenium.webdriver.common.by import By

# Все XPATH кнопок, которые нужно нажать
XPATH_all_buttons = []
# Все кнопки, которые нужно нажать
all_radio_buttons = []
# Указываем кол-во повторений заполнения формы
number = int(input('Введите кол-во повторений: '))
# Указываем url - адресс формы
url = input('Введите url: ')
# Указываем кол-во кнопок
input_button = int(input('Введите кол-во кнопок: '))


# Функция собирает все XPATH и кнопки которые нужны
def variables(count_button=input_button):
    for i in range(count_button):
        XPATH = input('Введите XPATH ' + str(i + 1) + ' кпопку:')
        XPATH_all_buttons.append(XPATH)
        # radio_button = XPATH#driver.find_element(By.XPATH, XPATH_all_buttons[i])
        # all_radio_buttons.append(radio_button)


# Функция принимает number - кол-во итераций и url ссылку на гугл форму
def autofill_google(number_number=number, url_forms=url):
    # Делаем счетчик и переменную для ввода url
    count = 0
    # Цикл накрутки n раз
    while count < number_number:
        # Открываем браузер Chrome
        driver = webdriver.Chrome()
        # Открывем страницу
        driver.get(url_forms)


        # Нажимаем на кнопки
        for i in range(len(XPATH_all_buttons)):
            driver.find_element(By.XPATH, XPATH_all_buttons[i]).click()

        # Закрывем браузер
        driver.quit()

        # Прибавляем счетчик
        count = count + 1


# Собираем кнопки
variables()
# Запускаем автозаполнение
autofill_google()