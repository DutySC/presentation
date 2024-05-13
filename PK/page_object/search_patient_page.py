import PK.parametrize as prm
import time
from BASE_PAGE import BasePage
from selenium.webdriver.common.by import By
# from conftest import browser_SNILS

class search_patient_locators:
    LOCATOR_SEARCH_PATIENT_1 = (By.XPATH, '//span[contains(text(), "Регистратура")]')
    LOCATOR_SEARCH_PATIENT_2 = (By.XPATH, '//span[contains(text(), "Поиск пациентов")]')
    LOCATOR_NEW_PATIENT = (By.XPATH, '//td[contains(text(), "Новый пациент")]')
    LOCATOR_FULL_WINDOW = (By.XPATH, '//div[@name="maximizedButton"]')
    LOCATOR_LAST_NAME = (By.XPATH, '//table[@name="SURNAME"]//input')
    LOCATOR_FIRST_NAME = (By.XPATH, '//table[@name="FIRSTNAME"]//input')
    LOCATOR_SURNAME = (By.XPATH, '//table[@name="LASTNAME"]//input')
    LOCATOR_BIRTHDAY = (By.XPATH, '//div[@name="BIRTHDATE"]//input')
    LOCATOR_CARD_NUMBER = (By.XPATH, '//table[@name="CARD_NUMB"]//img')
    LOCATOR_SNILS = (By.XPATH, '//table[@name="SNILS"]//input')
    LOCATOR_ENTER_POLIS = (By.XPATH, '//table[@name="POLIS_NUMB"]//input')
    LOCATOR_INSURANCE_COMPANY = (By.XPATH, '//table[@name="POLIS_WHO"]//img')
    LOCATOR_OBLASTI = (By.XPATH, '//table[@name="GEO_OMS"]//img')
    LOCATOR_OBLAST = (By.XPATH, '//tr[@comboboxname="GEO_OMS"]//span[text()="Все"]')
    LOCATOR_OBLAST_OK = (By.XPATH, '//td[contains(text(), "Ок")]')
    LOCATOR_TYPE_OF_POLIS = (By.XPATH, '//table[@name="POLIS_KIND"]//img')
    LOCATOR_CHOOSE_POLIS = (By.XPATH, '//span[contains(text(), "Временное свидетельство")]')
    LOCATOR_DATA_1 = (By.XPATH, '//div[@name="POLIS_WHEN"]//div[contains(@class, "img-calendar")]')
    LOCATOR_DATA_2 = (By.XPATH, '//div[contains(text(), "Сегодня")]')
    LOCATOR_TAB_STATUS = (By.XPATH, '//div[contains(text(), "Соц.")]')
    LOCATOR_STATUS_OPEN = (By.XPATH, '//table[@name="SOCIAL_STATE"]//img')
    LOCATOR_STATUS_OK = (By.XPATH, '//td[contains(text(), "Ок")]')
    LOCATOR_TAB_DOCUMENTS = (By.XPATH, '//div[contains(text(),"Документы")]')
    LOCATOR_TYPE_OF_DOCUMENTS = (By.XPATH, '//table[@name="PD_TYPE"]//img')
    LOCATOR_CHOOSE_DOCUMENT = (By.XPATH, '//span[contains(text(), "Вид на жительство")]')
    LOCATOR_DATA_3 = (By.XPATH, '//div[@name="PD_WHEN"]//div[contains(@class, "img-calendar")]')
    LOCATOR_DATA_4 = (By.XPATH, '//div[contains(text(), "Сегодня")]')
    LOCATOR_WHO_GAVE = (By.XPATH, '//table[@name="PD_WHO"]//textarea')
    LOCATOR_TAB_AREAS = (By.XPATH, '//table[@name="PMC_DocContactsPageControl"]//div[contains(text(),"Адреса")]')
    LOCATOR_AREA = (By.XPATH, '//table[@name="ADDRREAL_RAION"]//img')
    LOCATOR_AREA_OK = (By.XPATH, '//td[contains(text(), "Ок")]')
    LOCATOR_ENTER_AREA = (By.XPATH, '//table[@name="ADDRREAL_STREET"]//img')
    LOCATOR_CHOOSE_ANYCHINSKIY = (By.XPATH, '//a[contains(text(), "Анучинский")]')
    LOCATOR_CHOOSE_ABRICOSOVOE = (By.XPATH, '//a[contains(text(), "Абрикосовое")]')
    LOCATOR_HOME = (By.XPATH, '//table[@name="ADDRREAL_HOUSE"]//input')
    LOCATOR_OK = (By.XPATH, '//td[contains(text(), "ОК")]')
    LOCATOR_DICTIONARY_PATIENT_CARD_1 = (By.XPATH, '//span[contains(text(), "Словари")]')
    LOCATOR_DICTIONARY_PATIENT_CARD_2 = (By.XPATH, '//span[contains(text(), "Контрагенты")]')
    LOCATOR_DICTIONARY_PATIENT_CARD_3 = (By.XPATH, '//span[contains(text(), "Карты пациентов")]')
    LOCATOR_PATIENT_FILTER_1 = (By.XPATH, '(//span[text()="Показать фильтр"])[2]')
    LOCATOR_PATIENT_FILTER_2 = (By.XPATH, '//table[@field="LASTNAME"]//input')
    LOCATOR_PATIENT_FILTER_SEARCH_1 = (By.XPATH, '//div[contains(@class,"btn_actions searchFilter")]//span[text()="Найти"]')
    LOCATOR_LAST_NAME_NEWVERSION = (By.XPATH, '//span[contains(text(), "Новаяверсия")]')
    LOCATOR_DELETE_USER_1 = (By.XPATH, '//div[@id="PopUp_Menu_PERSMEDCARD_GRID_popup"]//td[text()="Удалить"]')
    LOCATOR_DICTIONARY_INDIVIDUAL_1 = (By.XPATH, '//span[contains(text(), "Словари")]')
    LOCATOR_DICTIONARY_INDIVIDUAL_2 = (By.XPATH, '//span[contains(text(), "Контрагенты")]')
    LOCATOR_DICTIONARY_INDIVIDUAL_3 = (By.XPATH, '//tr[1]//span[contains(text(), "Контрагенты")]')
    LOCATOR_PATIENT_FILTER_3 = (By.XPATH, '//div[@name="GRID_AGENTS"]//span[text()="Показать фильтр"]')
    LOCATOR_PATIENT_FILTER_4 = (By.XPATH, '//table[@field="LASTNAME"]//input')
    LOCATOR_CATALOGS_1 = (By.XPATH, '//div[@id="TreeArea_CATALOGS_DEFAULT"]')
    LOCATOR_CATALOGS_2 = (By.XPATH, '//td[contains(text(), "Список")]')
    LOCATOR_DELETE_USER_2 = (By.XPATH, '//div[@id="PopUp_Menu_pAGENTS"]//td[contains(text(), "Удалить")]')

class search_patient(BasePage):
    def create_patient(self):
        try:
            print('🔽 Модуль - "Поиск пациентов"')
            self.driver.refresh()
            start_search_patient = time.time()
            self.find_element(search_patient_locators.LOCATOR_SEARCH_PATIENT_1).click()  # вкладка "Регистратура"
            self.find_element(search_patient_locators.LOCATOR_SEARCH_PATIENT_2).click()  # вкладка "Поиск пациентов"
            self.find_element_pb()  # прогрессбар
            time.sleep(3)  # ожидание
            self.find_element(search_patient_locators.LOCATOR_NEW_PATIENT).click()  # создание нового пациента
            self.find_element_pb()  # прогрессбар
            self.find_element_pb()  # прогрессбар
            time.sleep(5) # ожидание
            self.find_element(search_patient_locators.LOCATOR_FULL_WINDOW).click()
            search_string_1 = self.find_element(search_patient_locators.LOCATOR_LAST_NAME)  # ввод фамилии
            search_string_1.send_keys(prm.last_name)  # указывается фамилия
            search_string_2 = self.find_element(search_patient_locators.LOCATOR_FIRST_NAME)  # ввод имени
            search_string_2.send_keys(prm.first_name)  # указывается имя
            search_string_3 = self.find_element(search_patient_locators.LOCATOR_SURNAME)  # ввод отчетсва
            search_string_3.send_keys(prm.surname)  # указывается отчетсво
            self.find_element(search_patient_locators.LOCATOR_BIRTHDAY).click() # дата рождения
            search_string_4 = self.find_element(search_patient_locators.LOCATOR_BIRTHDAY)  # дата рождения
            search_string_4.send_keys(prm.data) # указывается дата рождения
            self.find_element(search_patient_locators.LOCATOR_CARD_NUMBER).click()  # кнопка для выдачи номера карты
            self.find_element_pb()  # прогрессбар
            self.find_element(search_patient_locators.LOCATOR_SNILS).click()  # ввод СНИЛС
            search_string_5 = self.find_element(search_patient_locators.LOCATOR_SNILS)  # ввод СНИЛС
            search_string_5.send_keys(prm.snils) # указывается СНИЛС
            search_string_6 = self.find_element(search_patient_locators.LOCATOR_ENTER_POLIS)  # ввод номера полиса
            search_string_6.send_keys(prm.rand)  # указывается номер полиса
            self.find_element(search_patient_locators.LOCATOR_INSURANCE_COMPANY).click()  # окно для указания страховой компании
            self.find_element_pb()  # прогрессбар
            self.find_element_pb()  # прогрессбар
            time.sleep(2)  # ожидание
            self.find_element(search_patient_locators.LOCATOR_OBLASTI).click()  # выкидное окно для указания областей
            self.find_element(search_patient_locators.LOCATOR_OBLAST).click()  # выбор всех областей
            self.find_element_pb()  # прогрессбар
            self.find_element(search_patient_locators.LOCATOR_OBLAST_OK).click()  # кнопка "Ок"
            self.find_element_pb()  # прогрессбар
            self.find_element(search_patient_locators.LOCATOR_TYPE_OF_POLIS).click()  # выбор вида полиса
            self.find_element(search_patient_locators.LOCATOR_TYPE_OF_POLIS).click()  # выбор вида полиса
            self.find_element(search_patient_locators.LOCATOR_CHOOSE_POLIS).click()  # указать временное свидетельство
            self.find_element(search_patient_locators.LOCATOR_DATA_1).click()  # дата выдачи
            self.find_element(search_patient_locators.LOCATOR_DATA_2).click()  # указать дату выдачи
            self.find_element(search_patient_locators.LOCATOR_TAB_STATUS).click() # вкладка Соц. статус
            self.find_element(search_patient_locators.LOCATOR_STATUS_OPEN).click() # окно выбора соц. статуса
            self.find_element_pb()  # прогрессбар
            self.find_element(search_patient_locators.LOCATOR_STATUS_OK).click()  # подтверждения соц. статуса
            self.find_element_pb()  # прогрессбар
            self.find_element(search_patient_locators.LOCATOR_TAB_DOCUMENTS).click()  # вкладка Документы/Адреса
            self.find_element(search_patient_locators.LOCATOR_TAB_DOCUMENTS).click()  # вкладка Документы/Адреса
            self.find_element(search_patient_locators.LOCATOR_TYPE_OF_DOCUMENTS).click()  # тип документа
            self.find_element(search_patient_locators.LOCATOR_CHOOSE_DOCUMENT).click()  # указать тип документа "Вид на жительство"
            self.find_element(search_patient_locators.LOCATOR_DATA_3).click()  # дата выдачи
            self.find_element(search_patient_locators.LOCATOR_DATA_4).click()  # указать дату выдачи
            search_string_7 = self.find_element(search_patient_locators.LOCATOR_WHO_GAVE)  # кем выдан
            search_string_7.send_keys(prm.mvd) # указать кем выдан - "МВД"
            self.find_element(search_patient_locators.LOCATOR_TAB_AREAS).click()  # подвкладка "Адреса"
            self.find_element(search_patient_locators.LOCATOR_AREA).click()  # ввод района
            self.find_element_pb()  # прогрессбар
            self.find_element(search_patient_locators.LOCATOR_AREA_OK).click()  # кнопка "Ок"
            self.find_element_pb()  # прогрессбар
            self.find_element(search_patient_locators.LOCATOR_ENTER_AREA).click()  # ввод адреса
            self.find_element_pb()  # прогрессбар
            self.find_element(search_patient_locators.LOCATOR_CHOOSE_ANYCHINSKIY).click()  # выбрать Анучинский
            self.find_element_pb()  # прогрессбар
            self.find_element(search_patient_locators.LOCATOR_CHOOSE_ABRICOSOVOE).click()  # выбрать Абрикосовое
            self.find_element_pb()  # прогрессбар
            search_string_8 = self.find_element(search_patient_locators.LOCATOR_HOME)  # выбрать дом
            search_string_8.send_keys(prm.home) # указать номер дома
            self.find_element(search_patient_locators.LOCATOR_OK).click()  # кнопка "ОК"
            self.find_element_pb()  # прогрессбар
            print('    ✅ Тестовый пациент - создан') # вывод
            ###########след.этап########################################################################################
            self.find_element(search_patient_locators.LOCATOR_DICTIONARY_PATIENT_CARD_1).click() # вкладка "Словари"
            self.find_element(search_patient_locators.LOCATOR_DICTIONARY_PATIENT_CARD_2).click() # вкладка "Контрагенты"
            self.find_element(search_patient_locators.LOCATOR_DICTIONARY_PATIENT_CARD_3).click() # вкладка "Карты пациентов"
            self.find_element_pb()
            try:
                self.find_element(search_patient_locators.LOCATOR_PATIENT_FILTER_1).click()  # включить поиск по фильтрам
            except:
                pass
            search_string_9 = self.find_element(search_patient_locators.LOCATOR_PATIENT_FILTER_2)   # поиск по отчеству
            search_string_9.send_keys(prm.surname)   # ввод отчества пациента
            self.find_element(search_patient_locators.LOCATOR_PATIENT_FILTER_SEARCH_1).click()  # кнопка "Найти"
            self.actionchains(search_patient_locators.LOCATOR_LAST_NAME_NEWVERSION).perform()  # ПКМ по имени созданного пациента
            self.find_element(search_patient_locators.LOCATOR_DELETE_USER_1).click() # кнопка "Удалить"
            self.driver.switch_to.alert.accept()  # принятие всплывающего окна
            self.find_element_pb()  # прогрессбар
            self.find_element(search_patient_locators.LOCATOR_DICTIONARY_INDIVIDUAL_1).click() # вкладка "Словари"
            self.find_element(search_patient_locators.LOCATOR_DICTIONARY_INDIVIDUAL_2).click() # вкладка "Контрагенты"
            self.find_element(search_patient_locators.LOCATOR_DICTIONARY_INDIVIDUAL_3).click() # вкладка "Контрагенты"
            self.find_element_pb()  # прогрессбар
            self.find_element(search_patient_locators.LOCATOR_PATIENT_FILTER_3).click()  # включить поиск по фильтрам
            search_string_10 = self.find_element(search_patient_locators.LOCATOR_PATIENT_FILTER_4)   # поиск по отчеству
            search_string_10.send_keys(prm.surname)   # ввод отчества пациента
            self.actionchains(search_patient_locators.LOCATOR_CATALOGS_1).perform()  # ПКМ по каталогу
            self.find_element(search_patient_locators.LOCATOR_CATALOGS_2).click()  # поиск по списку
            self.actionchains(search_patient_locators.LOCATOR_LAST_NAME_NEWVERSION).perform()  # ПКМ по имени созданного пациента
            self.find_element(search_patient_locators.LOCATOR_DELETE_USER_2).click() # кнопка "Удалить"
            self.driver.switch_to.alert.accept()  # принятие всплывающего окна
            self.find_element_pb()  # прогрессбар
            print('    ✅ Тестовый пациент - удален') # вывод
            end_search_patient = time.time()
            full_search_patient = end_search_patient - start_search_patient
            print('    🏁 Общее время модуля: ', round(full_search_patient, 2), 'с')
        except Exception as error:
            self.get_screenshots('Results/Results_sc/Поиск_Приморья.png')
            self.driver.refresh()

