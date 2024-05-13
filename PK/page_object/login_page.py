from selenium.webdriver import Keys

import PK.parametrize as prm
import time
from BASE_PAGE import BasePage
from selenium.webdriver.common.by import By

class login_locators:
    LOCATOR_BODY = (By.XPATH, '//body')
    LOCATOR_USER = (By.XPATH, '//div[@name="DBLogin"]//input')
    LOCATOR_PASWD = (By.XPATH, '//div[@name="DBPassword"]//input')
    LOCATOR_ENTER = (By.XPATH, '//div[contains(text(), "Войти")]')
    LOCATOR_LPU_1 = (By.XPATH, '//div[@class="cmbb-button"]')
    LOCATOR_LPU_2 = (By.XPATH, '//span[contains(text(), "250000 -")]')
    LOCATOR_LC_1 = (By.XPATH, '//div[@name="CABLAB"]/div[@class="cmbb-button"]')
    LOCATOR_LC_2 = (By.XPATH, '//span[contains(text(), "кабинет 2")]')
    LOCATOR_ENTERLPU = (By.XPATH, '//div[@name="Btn"]/div[contains(text(), "Выбор")]')

class login(BasePage):
    def auth(self):
        try:
            print('=================\n[Приморский край]')
            print('🔽 Модуль - "Авторизация"')
            minimize = self.find_element(login_locators.LOCATOR_BODY)
            minimize.send_keys(Keys.CONTROL + Keys.SUBTRACT)
            user = self.find_element(login_locators.LOCATOR_USER) # логин
            user.send_keys(prm.login) # ввод логина
            paswd = self.find_element(login_locators.LOCATOR_PASWD) # пароль
            paswd.send_keys(prm.password) # ввод пароля
            self.find_element(login_locators.LOCATOR_ENTER).click() # кнопка "Войти"
            start_auth_1 = time.time() # начало отсчета
            self.find_element_pb()  # прогрессбар
            end_auth_1 = time.time() # конец отсчета
            full_auth_1 = end_auth_1 - start_auth_1 # полное время авторизации
            if full_auth_1 <= 2: # условие
                print('    ✅ Авторизация: ', round(full_auth_1, 2), 'с')
            else:
                print('    ⚠️ Авторизация: ', round(full_auth_1, 2), 'с', '(> 2 с)')
            time.sleep(1) # ожидание
            self.find_element(login_locators.LOCATOR_LPU_1).click() # открыть вкладку ЛПУ
            self.find_element(login_locators.LOCATOR_LPU_2).click() # выбор ЛПУ
            self.find_element_pb()  # прогрессбар
            self.find_element(login_locators.LOCATOR_ENTERLPU).click() # продолжить
            start_auth_2 = time.time() # начало отсчета
            self.find_element_pb()  # прогрессбар
            end_auth_2 = time.time() # начало отсчета
            full_auth_2 = end_auth_2 - start_auth_2 # полное время выбора ЛПУ
            if full_auth_2 <= 5: # условие
                print('    ✅ Выбор ЛПУ: ', round(full_auth_2, 2), 'с')
            else:
                print('    ⚠️ Выбор ЛПУ: ', round(full_auth_2, 2), 'с', '(> 5 с)')
            full_auth = full_auth_1 + full_auth_2 # полное время модуля авторизации
            print('    🏁 Общее время модуля: ', round(full_auth, 2), 'с') # вывод полного времени модуля авторизации
        except Exception as error:
            self.get_screenshots('Results/Results_sc/Авторизация_Приморья.png')
            print('    ❗️ Возникла ошибка в модуле - "Авторизация":', (str(error)[:100]))
            self.driver.quit()
