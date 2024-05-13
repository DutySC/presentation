import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

p_link = 'http://172.17.0.2:4444/wd/hub' # адрес для инициализации драйвера

@pytest.fixture(scope='function')
def browser_PK():
    # service = Service(executable_path='chromedriver.exe') # путь до драйвера
    chrome_options = ChromeOptions() # объект для опций
    # chrome_options.add_argument('--headless') # фоновый режим
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging']) # включение экспериментальных функций
    chrome_options.add_argument('--ignore-certificate-errors') # игнорирование проверки сертификата
    chrome_options.add_argument('--ignore-ssl-errors') # игнорирование проверки сертификата
    chrome_options.add_argument('--start-maximized')  # полный экран
    # driver = webdriver.Chrome(service=service, options=chrome_options) # настройка драйвера
    driver = webdriver.Remote(command_executor=f'{p_link}', options=chrome_options)  # настройка драйвера
    link_1 = 'https://192.168.1.1/'  # адрес для подключения
    driver.get(link_1) # подключение по указанному адресу
    # r = requests.get(link_1)
    # res = r.status_code
    # if res == 200:
    #     pass
    # else:
    #     print('Код страницы:', res)
    #     pass
    yield driver # возврат из функции с сохранением состояния ее переменных
    driver.quit() # выход из браузера