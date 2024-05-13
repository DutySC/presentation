import testit
from PK.page_object.login_page import login
from PK.page_object.doctors_diary_page import doctors_diary
from PK.page_object.schedule_page import schedule
from PK.page_object.hospitalization_page import hospitalization
from PK.page_object.search_patient_page import search_patient
from PK.page_object.reestr import ReestrPoliclinic
from PK.page_object.reestr_st import ReestrSt


@testit.step('Модуль: Авторизация', 'Проверка авторизации на продуктивном стенде')
def test_PK_login(browser_PK):
    start_page = login(browser_PK)
    start_page.auth()


@testit.step('Модуль: Дневник врача', 'Запись пациента, оказание услуги и ее отмена')
def test_PK_doctors_diary(browser_PK):
    # test_PK_login(browser_PK)  # тест авторизации
    doctors_diary_test = doctors_diary(browser_PK)
    doctors_diary_test.diary()


@testit.step('Модуль: Расписание', 'Проверка записи пациента к врачу')
def test_PK_schedule(browser_PK):
    # test_PK_login(browser_PK)  # тест авторизации
    patient_schedule_test = schedule(browser_PK)
    patient_schedule_test.patient_schedule()


@testit.step('Модуль: Госпитализация', 'Госпитализация пользователя')
def test_PK_hospitalization(browser_PK):
    # test_PK_login(browser_PK)  # тест авторизации
    patient_hospitalization_test = hospitalization(browser_PK)
    patient_hospitalization_test.register_patient()


@testit.step('Модуль: Поиск пациента', 'Создание и удаление тестового пациента')
def test_PK_search_patient(browser_PK):
    # test_PK_login(browser_PK)  # тест авторизации
    search_patient_test = search_patient(browser_PK)
    search_patient_test.create_patient()

@testit.step('Модуль: Формирование реестра (Поликлиника)', 'Создание и удаление реестра поликлиники')
def test_PK_reestrpk(browser_PK):
    reestr = ReestrPoliclinic(browser_PK)
    reestr.reestr()

@testit.step('Модуль: Формирование реестра (Стационар)', 'Создание и удаление реестра стационара')
def test_PK_reestrst(browser_PK):
    reestr = ReestrSt(browser_PK)
    reestr.reestr()

# def test_PK_full(self, browser_PK):
#     start = time.time()  # начало отсчета
#     start_page = login(browser_PK)  # тест модуля авторизации
#     start_page.auth()
#     start_doctors_diary = time.time()
#     doctors_diary_test = doctors_diary(browser_PK)  # тест модуля "Дневник врача"
#     doctors_diary_test.diary()
#     doctors_diary_test.diary_provide_service()
#     doctors_diary_test.diary_delite()
#     end_doctors_diary = time.time()
#     full_doctors_diary = end_doctors_diary - start_doctors_diary
#     print(' ▶️ Модуль - "Дневник врача", выполнен за: ', round(full_doctors_diary, 2),
#           'с')  # вывод полного времени тестирования
#     start_patient_schedule = time.time()
#     patient_schedule_test = schedule(browser_PK)  # тест модуля "Расписание"
#     patient_schedule_test.patient_schedule()
#     patient_schedule_test.patient_schedule_delete()
#     end_patient_schedule = time.time()
#     full_patient_schedule = end_patient_schedule - start_patient_schedule
#     print(' ▶️ Модуль - "Расписание", выполнен за: ', round(full_patient_schedule, 2),
#           'с')  # вывод полного времени тестирования
#     start_patient_hospitalization = time.time()
#     patient_hospitalization_test = hospitalization(browser_PK)  # тест модуля "Госпитализация"
#     patient_hospitalization_test.register_patient()
#     patient_hospitalization_test.patient_hospitalization()
#     patient_hospitalization_test.patient_cancel_hospitalization()
#     patient_hospitalization_test.patient_delete_hospitalization()
#     end_patient_hospitalization = time.time()
#     full_patient_hospitalization = end_patient_hospitalization - start_patient_hospitalization
#     print(' ▶️ Модуль - "Госпитализация", выполнен за: ', round(full_patient_hospitalization, 2),
#           'с')  # вывод полного времени тестирования
#     start_search_patient = time.time()
#     search_patient_test = search_patient(browser_PK)  # тест модуля "Поиск пациента"
#     search_patient_test.create_patient()
#     search_patient_test.delete_patient()
#     end_search_patient = time.time()
#     full_search_patient = end_search_patient - start_search_patient
#     print(' ▶️ Модуль - "Поиск пациентов", выполнен за: ', round(full_search_patient, 2),
#           'с')  # вывод полного времени тестирования
#     end = time.time()  # конец отсчета
#     full_test = end - start  # полное время авторизации
#     print(' ▶️ Затраченное время на тестирование: ', round(full_test, 2), 'с')  # вывод полного времени тестирования