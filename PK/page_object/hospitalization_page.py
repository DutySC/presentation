from selenium.common import ElementClickInterceptedException
import PK.parametrize as prm
import time
from BASE_PAGE import BasePage
from selenium.webdriver.common.by import By

class locators_hospitalization:
    LOCATOR_HOSPITALIZATION_1 = (By.XPATH, '//span[contains(text(), "Регистратура")]')
    LOCATOR_HOSPITALIZATION_2 = (By.XPATH, '//span[contains(text(), "Приемный покой")]')
    LOCATOR_HOSPITALIZATION_3 = (By.XPATH, '//span[contains(text(),"Журнал госпитализации")]')
    LOCATOR_PATIENT_REG_CONTAINER = (By.XPATH, '//div[@class="grid_data box-sizing-force"]')
    LOCATOR_WINDOW_RCM_1 = (By.XPATH, '(//td[@name="HEAD_COL_SIGNAL_INFO"])[2]')
    LOCATOR_WINDOW_RCM_2 = (By.XPATH, '//td[contains(text(), "Добавить")]')
    LOCATOR_SEARCH_PATIENT_1 = (By.XPATH, '//table[@name="modal_win"]//table[@name="PERSMEDCARD"]//img')
    LOCATOR_SEARCH_PATIENT_2 = (By.XPATH, '//div[@name="search"]//input[@placeholder="Номер карты"]')
    LOCATOR_SEARCH_PATIENT_3 = (By.XPATH, '//td[contains(text(), "Найти")]')
    LOCATOR_SEARCH_PATIENT_4 = (By.XPATH, f'//a[contains(text(), "{prm.name_patient}")]')
    LOCATOR_JORNAL_1 = (By.XPATH, '//table[@name="C_HOSP_PLAN_KINDS"]//img')
    LOCATOR_JORNAL_2 = (By.XPATH, '//div[@name="ComboItemsList_C_HOSP_PLAN_KINDS"]//span[contains(text(), "Планирование госпитализации")]')
    LOCATOR_DIAGNOSIS_1 = (By.XPATH, '//table[@name="MKB10"]//img')
    LOCATOR_DIAGNOSIS_2 = (By.XPATH, '//table[@name="SEARCH_CODE"]//input')
    LOCATOR_DIAGNOSIS_3 = (By.XPATH, '//div[@formname="MKB10/mkb10"]//td[contains(text(), "Поиск")]')
    LOCATOR_DIAGNOSIS_4 = (By.XPATH, '//td[contains(text(), "Ок")]')
    LOCATOR_CREATE_DIRECTION = (By.XPATH, '//td[contains(text(), "ОК")]')
    LOCATOR_CHOOSE_PATIENT_PCM = (By.XPATH, f'//a[contains(text(), "{prm.name_patient}")]')
    LOCATOR_HOSPITALIZATION_PATIENT_1 = (By.XPATH, '//td[text()="Госпитализировать"]')
    LOCATOR_HOSPITALIZATION_PATIENT_2 = (By.XPATH, '//td[contains(text(), "Далее")]')
    LOCATOR_HOSPITALIZATION_PATIENT_3 = (By.XPATH, '//td[contains(text(), "ОК")]')
    LOCATOR_CANCEL_HOSPITALIZATION = (By.XPATH, '//td[contains(text(), "Отменить госпитализацию")]')
    LOCATOR_DELETE_HOSPITALIZATION = (By.XPATH, '//td[contains(text(), "Удалить")]')


class hospitalization(BasePage):
    def register_patient(self):
        try:
            print('🔽 Модуль - "Госпитализация"')
            start_patient_hospitalization = time.time()
            self.find_element(locators_hospitalization.LOCATOR_HOSPITALIZATION_1).click() # вкладка "Регистратура"
            self.find_element(locators_hospitalization.LOCATOR_HOSPITALIZATION_2).click() # вкладка "Приемный покой"
            self.find_element(locators_hospitalization.LOCATOR_HOSPITALIZATION_3).click() # вкладка "Журнал госпитализации"
            self.find_element_pb()  # прогрессбар
            self.find_element_pb()  # прогрессбар
            self.find_element(locators_hospitalization.LOCATOR_PATIENT_REG_CONTAINER) # полная прогрузка элементов страницы
            time.sleep(3)  # ожидание
            self.actionchains(locators_hospitalization.LOCATOR_WINDOW_RCM_1).perform() # ПКМ по области окна
            self.find_element(locators_hospitalization.LOCATOR_WINDOW_RCM_2).click() # добавить пациента для создания направления
            self.find_element_pb()  # прогрессбар
            self.find_element_pb()  # прогрессбар
            time.sleep(2)
            self.find_element(locators_hospitalization.LOCATOR_SEARCH_PATIENT_1).click() # открытие окна для выбора пациента
            self.find_element_pb()  # прогрессбар
            search_string_1 = self.find_element(locators_hospitalization.LOCATOR_SEARCH_PATIENT_2)  # окно ввода
            search_string_1.send_keys(prm.patient) # указать карту пользователя
            self.find_element(locators_hospitalization.LOCATOR_SEARCH_PATIENT_3).click()  # кнопка "Найти"
            self.find_element_pb()  # прогрессбар
            self.find_element(locators_hospitalization.LOCATOR_SEARCH_PATIENT_4).click()  # выбор пользователя "Тест Берем Карта"
            self.find_element_pb()  # прогрессбар
            self.find_element(locators_hospitalization.LOCATOR_JORNAL_1).click() # открытие выпадающего таблицы
            self.find_element(locators_hospitalization.LOCATOR_JORNAL_2).click() # выбор журнала
            self.find_element_pb()  # прогрессбар
            self.find_element(locators_hospitalization.LOCATOR_DIAGNOSIS_1).click() # окно выбора диагноза
            self.find_element_pb()  # прогрессбар
            search_string_2 = self.find_element(locators_hospitalization.LOCATOR_DIAGNOSIS_2) # поиск диагноза J10.0
            search_string_2.send_keys(prm.g_disease) # ввод диагноза J10.0
            self.find_element(locators_hospitalization.LOCATOR_DIAGNOSIS_3).click() # кнопка "Поиск"
            self.find_element_pb()  # прогрессбар
            self.find_element(locators_hospitalization.LOCATOR_DIAGNOSIS_4).click() # кнопка "ОК"
            self.find_element_pb()  # прогрессбар
            self.find_element(locators_hospitalization.LOCATOR_CREATE_DIRECTION).click() # кнопка "ОК"
            self.find_element_pb()  # прогрессбар
            print('    ✅ Пациент записан на госпитализацию') # вывод
            ###########след.этап########################################################################################
            self.actionchains(locators_hospitalization.LOCATOR_CHOOSE_PATIENT_PCM).perform() # ПКМ по имени пациента
            self.find_element(locators_hospitalization.LOCATOR_HOSPITALIZATION_PATIENT_1).click() # госпитализация пациента
            self.find_element_pb()  # прогрессбар
            self.find_element_pb()  # прогрессбар
            self.find_element(locators_hospitalization.LOCATOR_HOSPITALIZATION_PATIENT_2).click() # кнопка "Далее"
            self.find_element_pb()  # прогрессбар
            self.find_element(locators_hospitalization.LOCATOR_HOSPITALIZATION_PATIENT_3).click() # кнопка "ОК"
            self.find_element_pb()  # прогрессбар
            print('    ✅ Пациент госпитализирован') # вывод
            ###########след.этап########################################################################################
            try:
                self.actionchains(locators_hospitalization.LOCATOR_CHOOSE_PATIENT_PCM).perform() # ПКМ по имени пациента
                self.find_element(locators_hospitalization.LOCATOR_CANCEL_HOSPITALIZATION).click() # отмена госпитализации пациента
                self.driver.switch_to.alert.accept()  # принятие всплывающего окна
            except ElementClickInterceptedException:
                self.actionchains(locators_hospitalization.LOCATOR_WINDOW_RCM_1).click() # ЛКМ по области окна
                self.actionchains(locators_hospitalization.LOCATOR_CHOOSE_PATIENT_PCM).perform()  # ПКМ по имени пациента
                self.find_element(locators_hospitalization.LOCATOR_CANCEL_HOSPITALIZATION).click()  # отмена госпитализации пациента
                self.driver.switch_to.alert.accept()  # принятие всплывающего окна
            self.find_element_pb()  # прогрессбар
            print('    ✅ Госпитализация отменена') # вывод
            ###########след.этап########################################################################################
            self.actionchains(locators_hospitalization.LOCATOR_CHOOSE_PATIENT_PCM).perform() # ПКМ по имени пациента
            self.find_element(locators_hospitalization.LOCATOR_DELETE_HOSPITALIZATION).click() # удаление записи на госпитализацию
            self.driver.switch_to.alert.accept()  # принятие всплывающего окна
            self.find_element_pb()  # прогрессбар
            print('    ✅ Запись на госпитализацию удалена') # вывод
            end_patient_hospitalization = time.time()
            full_patient_hospitalization = end_patient_hospitalization - start_patient_hospitalization
            print('    🏁 Общее время модуля: ', round(full_patient_hospitalization, 2), 'с')
        except Exception as error:
            self.get_screenshots('Results/Results_sc/Госпитализация_Приморья.png')
            print('    ❗️ Возникла ошибка в модуле - "Госпитализация":', (str(error)[:100]))
            self.driver.refresh()
            pass



