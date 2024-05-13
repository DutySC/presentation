import PK.parametrize as prm
import time
from BASE_PAGE import BasePage
from selenium.webdriver.common.by import By

class locators_schedule:
    LOCATOR_SCHEDULE_1 = (By.XPATH, '//span[contains(text(), "Регистратура")]')
    LOCATOR_SCHEDULE_2 = (By.XPATH, '//tbody//span[text()="Расписание"]')
    LOCATOR_FILTER = (By.XPATH, '//div[@name="REG_PARAMS_EXPANDER"]')
    LOCATOR_FILTER_DEPARTMENT = (By.XPATH, '//table[@name="searchDEP"]//input[@type = "text"]')
    LOCATOR_FILTER_CABINET = (By.XPATH, '//table[@name="searchCAB"]//input[@type = "text"]')
    LOCATOR_FILTER_DOCTOR = (By.XPATH, '//table[@name="searchEMP_SERV"]//input[@type = "text"]')
    LOCATOR_PRESS_DEPARTMENT = (By.XPATH, f'//a[text()="{prm.department}"]')
    LOCATOR_CHOOSE_DOCTOR = (By.XPATH, f'//a[text()="{prm.doctor}"]')
    LOCATOR_SEARCH_1 = (By.XPATH, '//div[@class="reg_header_gen"]//td[contains(text(), "Найти")]')
    LOCATOR_REG_CONTAINER = (By.XPATH, '//div[@id = "RegContainer"]')
    LOCATOR_NEXT_PAGE = (By.XPATH, '//table[@title="Вперёд"]//img')
    LOCATOR_WRITE_TO_DOCTOR = (By.XPATH, '//td[@name="tdTimeCito"]//a[contains(text(), "Записать")]')
    LOCATOR_CARD_NUMBER = (By.XPATH, '//div[@name="main_div_frm"]//input[@placeholder="Номер карты"]')
    LOCATOR_PATIENT_ON_WRITE = (By.XPATH, f'//a[contains(text(), "{prm.name_patient}")]')
    LOCATOR_SERVICES = (By.XPATH, '//table[@name="SERVICES" and @title="Выберите услугу"]//img')
    LOCATOR_SERVICE = (By.XPATH, '//span[contains(text(), "B01.047.001 Прием (осмотр, консультация) врача-тер")]')
    LOCATOR_SEARCH_2 = (By.XPATH, '//div[@name="main_div_frm"]//td[text()="Найти"]')
    LOCATOR_WRITE = (By.XPATH, '//td[text()="Записать"]')
    LOCATOR_ESC_1 = (By.XPATH, '(//div[@ name="closeButton"])[3]')
    LOCATOR_ESC_2 = (By.XPATH, '//div[@name="closeButton"]')
    LOCATOR_PATIENT = (By.XPATH, f'//a[contains(text(), "{prm.schedule_patient}")]')
    LOCATOR_DELETE_WRITE = (By.XPATH, '//span[contains(text(), "Удалить")]')

class schedule(BasePage):
    def patient_schedule(self):
        try:
            print('🔽 Модуль - "Расписание"')
            start_patient_schedule = time.time()
            self.find_element(locators_schedule.LOCATOR_SCHEDULE_1).click() # вкладка "Регистратура"
            self.find_element(locators_schedule.LOCATOR_SCHEDULE_2).click() # вкладка "Расписание"
            start_open_schedule = time.time() # отчет времени
            self.find_element_pb() # прогрессбар
            self.find_element_pb() # прогрессбар
            self.find_element(locators_schedule.LOCATOR_REG_CONTAINER) # полная прогрузка элементов страницы
            end_open_schedule = time.time() # отчет времени
            full_time_schedule = end_open_schedule - start_open_schedule # затраченное время
            if full_time_schedule <= 15: # условие
                print('    ✅ Формирование окна - Расписание: ', round(full_time_schedule, 2), 'с') # вывод затраченного времени
            else:
                print('    ⚠️️ Формирование окна - Расписание: ', round(full_time_schedule, 2), 'с', '(> 15 с)') # вывод затраченного времени
            self.find_element(locators_schedule.LOCATOR_FILTER).click() # шторка вниз
            search_string_1 = self.find_element(locators_schedule.LOCATOR_FILTER_DEPARTMENT) # ввод отделения
            search_string_1.send_keys(prm.department) # указать отделение
            search_string_2 = self.find_element(locators_schedule.LOCATOR_FILTER_CABINET) # ввод кабинета
            search_string_2.send_keys(prm.polyclinic) # указать кабинет
            search_string_3 = self.find_element(locators_schedule.LOCATOR_FILTER_DOCTOR) # ввод врача
            search_string_3.send_keys(prm.doctor) # указать врача
            self.find_element(locators_schedule.LOCATOR_SEARCH_1).click() # кнопка "Найти"
            self.find_element_pb() # прогрессбар
            self.find_element(locators_schedule.LOCATOR_PRESS_DEPARTMENT).click() # раскрытия списка отделения
            self.find_element(locators_schedule.LOCATOR_CHOOSE_DOCTOR).click() # выбор врача Тестирование П.
            self.find_element_pb() # прогрессбар
            self.find_element(locators_schedule.LOCATOR_NEXT_PAGE).click() # выбор следующей недели
            self.find_element_pb() # прогрессбар
            self.find_element(locators_schedule.LOCATOR_WRITE_TO_DOCTOR).click() # запись на назнаначенную дату
            self.find_element_pb() # прогрессбар
            self.find_element_pb() # прогрессбар
            search_string_4 = self.find_element(locators_schedule.LOCATOR_CARD_NUMBER) # ввод значения поля "Номер карты"
            search_string_4.send_keys(prm.patient) # вввод К002489
            time.sleep(3)  # ожидание
            self.find_element(locators_schedule.LOCATOR_SEARCH_2).click() # кнопка "Найти"
            self.find_element_pb() # прогрессбар
            self.find_element(locators_schedule.LOCATOR_PATIENT_ON_WRITE).click() # выбор пациента
            self.find_element_pb() # прогрессбар
            self.find_element(locators_schedule.LOCATOR_SERVICES).click() # выпадающее окно услуг
            self.find_element(locators_schedule.LOCATOR_SERVICE).click() # выбор услуги
            self.find_element_pb() # прогрессбар
            self.find_element(locators_schedule.LOCATOR_WRITE).click() # запись к врачу
            self.find_element_pb() # прогрессбар
            self.find_element(locators_schedule.LOCATOR_ESC_1).click() # закрыть окно
            print('    ✅ Пациент записан к врачу') # вывод
            ###########след.этап########################################################################################
            time.sleep(2)  # ожидание
            self.find_element(locators_schedule.LOCATOR_PRESS_DEPARTMENT).click()  # раскрытия списка отделения
            self.find_element(locators_schedule.LOCATOR_CHOOSE_DOCTOR).click()  # выбор врача Тестирование П.
            self.find_element_pb()  # прогрессбар
            self.find_element(locators_schedule.LOCATOR_NEXT_PAGE).click()  # выбор следующей недели
            self.find_element_pb()  # прогрессбар
            self.find_element(locators_schedule.LOCATOR_PATIENT).click()
            self.find_element(locators_schedule.LOCATOR_DELETE_WRITE).click()
            self.driver.switch_to.alert.accept()  # принятие всплывающего окна
            self.find_element_pb()  # прогрессбар
            self.find_element(locators_schedule.LOCATOR_ESC_2).click() # закрыть окно
            self.find_element_pb()  # прогрессбар
            print('    ✅ Запись удалена') # вывод
            end_patient_schedule = time.time()
            full_patient_schedule = end_patient_schedule - start_patient_schedule
            print('    🏁 Общее время модуля: ', round(full_patient_schedule, 2), 'с')
        except Exception as error:
            self.get_screenshots('Results/Results_sc/Расписание_Приморья.png')
            print('    ❗️ Возникла ошибка в модуле - "Расписание":', (str(error)[:100]))
            self.driver.refresh()
            pass



