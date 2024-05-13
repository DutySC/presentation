import time

from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from BASE_PAGE import BasePage
from conftest import browser_RSO




class LocatorReestr:
    LOCATOR_UCHET = (By.XPATH, '//span[contains(text(), "Учет")]')
    LOCATOR_UCHET_2 = (By.XPATH, '//span[contains(text(), "ТФОМС ПК")]')
    LOCATOR_UCHET_3 = (By.XPATH, '//span[contains(text(), "Реестры счетов")]')
    LOCATOR_HEADER_REESTR = (By.XPATH, '//div[@name="GRID_GENERAL_REESTRS"]//div[@title="Показать меню"]')
    LOCATOR_FORM_REESTR = (By.XPATH, '//div[@name="PI_GR_CREATE"]//span')
    LOCATOR_TYPE = (By.XPATH, '//div[@name="REESTR_TITLE"]//div[@title="Выбрать из списка"]')
    LOCATOR_TYPE_2 = (By.XPATH, '(//span[contains(text(), "!!!АПП_БЕЗ_ПРОВЕРОК_ОМС_01.01.2023")])[3]')
    LOCATOR_VIEW = (By.XPATH, '//div[@name="REESTR_KIND"]//div[@title="Выбрать из списка"]')
    LOCATOR_VIEW_2 = (By.XPATH, '(//tr[@cmptype="ComboItem"]//span[contains(text(), "1. ОМС застрахованные")])[2]')
    LOCATOR_START_DATE = (By.XPATH, '(//div[@name="DATE_BEGIN"]//input)[2]')
    LOCATOR_END_DATE = (By.XPATH, '(//div[@name="DATE_END"]//input)[2]')
    LOCATOR_OK_BUTTON = (By.XPATH, '//div[@name="win_content"]//img')
    LOCATOR_OK_FIELD = (By.XPATH, '//div[@name="RNUMB"]//input')
    LOCATOR_UNIT = (By.XPATH, '//div[@name="DEPS"]//div[@title="Выбрать из справочника"]')
    LOCATOR_UNIT_2 = (By.XPATH, '//div[@name="DEPS_DEFAULT"]//span[contains(text(), "Показать фильтр")]')
    LOCATOR_UNIT_3 = (By.XPATH, '//table[@name="DS_DEPS_DEFAULT_DP_KIND_ID_FilterItem"]//img')
    LOCATOR_UNIT_4 = (By.XPATH, '//div[@name="ComboItemsList_DS_DEPS_DEFAULT_DP_KIND_ID_FilterItem"]//span[contains(text(), "Поликлиника")]')
    LOCATOR_UNIT_5 = (By.XPATH, '//div[@name="DEPS_DEFAULT_SelectList"]//img' )
    LOCATOR_OK = (By.XPATH, '//tr[@class="bt"]//td[contains(text(), "Ок")]')
    LOCATOR_ACCERT = (By.XPATH, '//div[@name="BUTTON_OK"]')
    LOCATOR_SEARCH = (By.XPATH, '//div[@name="DATE_BEGIN"]//input')
    LOCATOR_SEARCH_2 = (By.XPATH, '//div[@name="DATE_END"]//input')
    LOCATOR_SEARCH_3 = (By.XPATH, '//div[@name="BTN_SEARCH"]')
    LOCATOR_SEARCH_4 = (By.XPATH, '(//div[@class="toggleFilterSize"])[1]')
    LOCATOR_SEARCH_5 = (By.XPATH, '//div[@field="RNUMB"]//input')
    LOCATOR_SEARCH_6 = (By.XPATH, '//td[@cont="RNUMB"]//span[contains(text(), "666")]')
    LOCATOR_DELETE_REESTR = (By.XPATH, '//div[@name="PI_GR_UNLOAD"]')
    LOCATOR_DELETE_REESTR_2 = (By.XPATH, '//div[@name="PI_GR_DELETE"]')


class ReestrPoliclinic(BasePage):

    @classmethod
    def get_data(cls):
        date_start = datetime.today().strftime('%d%m%Y')
        date_end = (datetime.today() - timedelta(2)).strftime('%d%m%Y')
        return date_end, date_start
    def reestr(self):
        start_date, end_date = ReestrPoliclinic.get_data()
        try:
            print('🔽 Модуль: Формирование реестра (Поликлиника)')
            full_start = time.time()
            start = time.time()
            self.find_element(LocatorReestr.LOCATOR_UCHET).click() # Учет
            self.find_element(LocatorReestr.LOCATOR_UCHET_2).click() # Счета-реестры
            self.find_element(LocatorReestr.LOCATOR_UCHET_3).click()
            end = time.time()
            full = end - start
            if full <= 120:
                print('    ✅ Формирование окна - Реестры поликлиники: ', round(full, 2), 'c',)
            else:
                print('    ⚠️ Формирования окна - Реестры поликлиники: ', round(full, 2), 'c', '(> 120c)')
            start = time.time()
            self.find_element_pb()
            self.find_element(LocatorReestr.LOCATOR_HEADER_REESTR).click()
            self.find_element(LocatorReestr.LOCATOR_FORM_REESTR).click()
            self.find_element_pb()
            end = time.time()
            full = end - start
            if full <= 15:
                print('    ✅ Открытие окна "сформировать реестры": ', round(full, 2), 'c',)
            else:
                print('    ⚠️ Открытие окна "сформировать реестры": ', round(full, 2), 'c', '(> 15c)')
            time.sleep(2)
            start = time.time()
            self.find_element(LocatorReestr.LOCATOR_TYPE).click()
            self.find_element(LocatorReestr.LOCATOR_TYPE_2).click()
            self.find_element_pb()
            try:
                self.find_element(LocatorReestr.LOCATOR_VIEW).click()
            except:
                self.find_element(LocatorReestr.LOCATOR_VIEW).click()
            self.find_element(LocatorReestr.LOCATOR_VIEW_2).click()
            self.find_element_pb()
            start_d = self.find_element(LocatorReestr.LOCATOR_START_DATE)
            start_d.clear()
            start_d.send_keys(Keys.SHIFT + Keys.HOME)
            time.sleep(.5)
            start_d.send_keys(start_date)
            self.find_element_pb()
            end_d = self.find_element(LocatorReestr.LOCATOR_END_DATE)
            end_d.clear()
            end_d.send_keys(Keys.SHIFT + Keys.HOME)
            time.sleep(.5)
            end_d.send_keys(end_date)
            self.find_element_pb()
            try:
                self.find_element(LocatorReestr.LOCATOR_OK_BUTTON).click()
            except:
                self.find_element(LocatorReestr.LOCATOR_OK_BUTTON).click()
            self.find_element_pb()
            number = self.find_element(LocatorReestr.LOCATOR_OK_FIELD)
            result = number.get_attribute('value')
            if type(result) == str and len(result) > 0:
                print('    ✅ Номер реестра формируется автоматически')
            else:
                print('    ⚠️ Номер реестра не формируется автоматически')
                return False
            number.clear()
            number.send_keys('666')
            self.find_element_pb()
            self.find_element(LocatorReestr.LOCATOR_UNIT).click()
            self.find_element_pb()
            # self.find_element(LocatorReestr.LOCATOR_UNIT_2).click()
            time.sleep(1)
            self.find_element_pb()
            self.find_element(LocatorReestr.LOCATOR_UNIT_3).click()
            self.find_element_pb()
            self.find_element(LocatorReestr.LOCATOR_UNIT_4).click()
            self.find_element_pb()
            self.find_element(LocatorReestr.LOCATOR_UNIT_5).click()
            self.find_element_pb()
            self.find_element(LocatorReestr.LOCATOR_OK).click()
            self.find_element(LocatorReestr.LOCATOR_ACCERT).click()
            self.find_element_pb()
            end = time.time()
            full = end - start
            if full <= 120:
                print('    ✅ Формирование реестра: ', round(full, 2), 'c',)
            else:
                print('    ⚠️ Формирование реестра: ', round(full, 2), 'c', '(> 120c)')
            start = time.time()
            start_d = self.find_element(LocatorReestr.LOCATOR_SEARCH)
            start_d.clear()
            start_d.send_keys(Keys.SHIFT + Keys.HOME)
            start_d.send_keys(start_date)
            end_d = self.find_element(LocatorReestr.LOCATOR_SEARCH_2)
            end_d.clear()
            end_d.send_keys(Keys.SHIFT + Keys.HOME)
            end_d.send_keys(end_date)
            self.find_element_pb()
            self.find_element(LocatorReestr.LOCATOR_SEARCH_3).click()
            self.find_element_pb()
            self.find_element(LocatorReestr.LOCATOR_SEARCH_4).click()
            res = self.find_element(LocatorReestr.LOCATOR_SEARCH_5)
            res.send_keys('666')
            self.find_element_pb()
            self.actionchains(LocatorReestr.LOCATOR_SEARCH_6).perform()
            self.find_element(LocatorReestr.LOCATOR_DELETE_REESTR).click()
            self.find_element_pb()
            self.actionchains(LocatorReestr.LOCATOR_SEARCH_6).perform()
            self.find_element(LocatorReestr.LOCATOR_DELETE_REESTR_2).click()
            try:
                self.driver.switch_to.alert.accept()
            except:
                pass
            end = time.time()
            full = end - start
            if full <= 15:
                print('    ✅ Удаление созданного реестра: ', round(full, 2), 'c')
            else:
                print('    ⚠️ Удаление созданного реестра: ', round(full, 2), 'c', '(> 15c)')
            full_end = time.time()
            print('    🏁 Общее время модуля: ', round(full_end - full_start, 2), 'c')
            self.find_element_pb()
        except Exception as e:
            self.get_screenshots('Results/Results_sc/РеестрПоликлиники_Приморья.png')
            print('    ❗️ Возникла ошибка в модуле - "Реестры (Поликлиника)":', (str(e)[:100]))
            self.driver.refresh()
            pass
