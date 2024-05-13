from PK import full_test_PK
# from conftest import browser_SNILS, browser_PK
import time, testit

class Test_PK:
    """Актуальный номер СНИЛСа"""
    # browser_SNILS() # получаем рандомное значение СНИЛСа
    # print(browser_SNILS()) # вывод полученного значения СНИЛС

    """Тест по модулям"""
    @testit.workItemIds(214536, 214537, 214538, 214539, 214540, 218960, 218961)
    @testit.displayName('Приморский край')
    @testit.title('Крит. модули')
    @testit.labels('AUTOTEST_SC')
    @testit.link('https://testit.bars.group//projects/214392/tests?isolatedSection=d00a4ca8-1d41-452a-8267-97aae6499ee3')
    def test_PK(self, browser_PK):
        start = time.time()  # начало отсчета
        full_test_PK.test_PK_login(browser_PK)  # тест модуля авторизации
        full_test_PK.test_PK_doctors_diary(browser_PK) # тест модуля "Дневник врача"
        full_test_PK.test_PK_schedule(browser_PK) # тест модуля "Расписание"
        full_test_PK.test_PK_hospitalization(browser_PK) # тест модуля "Госпитализация"
        full_test_PK.test_PK_search_patient(browser_PK)  # тест модуля "Поиск пациентов"
        full_test_PK.test_PK_reestrpk(browser_PK)
        full_test_PK.test_PK_reestrst(browser_PK)
        end = time.time()  # конец отсчета
        full_test = end - start  # полное время авторизации
        time_format = time.strftime("%H:%M:%S", time.gmtime(full_test))
        print('🏁 Затраченное время на тестирование: ', time_format, '~')  # вывод полного времени тестирования
