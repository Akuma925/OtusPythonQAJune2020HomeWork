import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from allure_commons.types import AttachmentType
import allure


# Базовый класс имплементирующий основные методы работы с элементами web-странички
class BasePage:
    # Конструктор класса
    #
    #  на вход нужно передать драйвер управления браузером
    def __init__(self, driver):
        self.driver = driver
    small_sleep = 2
    mid_sleep = 10
    big_sleep = 20
    # self.read_config_json()

    # Словарь для получения id и подписи в xpath
    # dict_elem = {}

    # Метод для поиска элеменат в DOM
    def _element(self, selector: dict, index: int, link_text: str = None):
        by = None
        if link_text:
            by = By.LINK_TEXT
        elif 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']
        elif 'xpath' in selector.keys():
            by = By.XPATH
            selector = selector['xpath']
        elif 'id' in selector.keys():
            by = By.ID
            selector = selector['id']
        print("\n", selector)
        return self.driver.find_elements(by, selector)[
            index]  # WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((by, selector)))#

    # Метод для клика по указанному элементу
    def _click(self, selector, screen: bool = False, index=0):
        if screen:
            allure.attach(self.driver.get_screenshot_as_png(), name="_click_Screenshot1",
                          attachment_type=AttachmentType.PNG)
        ActionChains(self.driver).move_to_element(self._element(selector, index)).click().perform()
        if screen:
            allure.attach(self.driver.get_screenshot_as_png(), name="_click_Screenshot1",
                          attachment_type=AttachmentType.PNG)

    # Метод для двойного клика по указанному элементу
    def _double_click(self, selector, screen: bool = False, index=0):
        if screen:
            allure.attach(self.driver.get_screenshot_as_png(), name="_input_Screenshot1",
                          attachment_type=AttachmentType.PNG)
        ActionChains(self.driver).double_click(self._element(selector, index)).perform()
        if screen:
            allure.attach(self.driver.get_screenshot_as_png(), name="_input_Screenshot1",
                          attachment_type=AttachmentType.PNG)

    # Метод для ввода данных в указанное поле
    def _input(self, selector, value, screen: bool = False, index=0):
        element = self._element(selector, index)
        if screen:
            allure.attach(self.driver.get_screenshot_as_png(), name="_input_Screenshot0",
                          attachment_type=AttachmentType.PNG)
        element.clear()
        if screen:
            allure.attach(self.driver.get_screenshot_as_png(), name="_input_Screenshot1",
                          attachment_type=AttachmentType.PNG)
        element.send_keys(value)
        if screen:
            allure.attach(self.driver.get_screenshot_as_png(), name="_input_Screenshot2",
                          attachment_type=AttachmentType.PNG)

    # Метод для выбора элемента в выпадающем списке (класс списка list_form_control)
    def _select_element_on_list_form_control(self, selector, value, screen: bool = False, index=0):
        element = self._element(selector, index)
        print(element)
        element.click()
        html_list = self.driver.find_element_by_class_name('form-control')
        items = html_list.find_elements_by_tag_name("option")
        for item in items:
            if item.text in value:
                item.click()
                if screen:
                    allure.attach(self.driver.get_screenshot_as_png(),
                                  name="_select_element_on_list_form_control_Screenshot1",
                                  attachment_type=AttachmentType.PNG)
                break

    # Метод для выбора элемента в выпадающем списке (класс списка select2-result)
    def _select_element_on_list_select2_results(self, selector, value, screen: bool = False, index=0):
        element = self._element(selector, index)
        print(element)
        element.click()
        time.sleep(self.small_sleep)
        html_list = self.driver.find_elements_by_class_name('select2-result')
        if len(html_list) != 0:
            for item in html_list:
                if item.text in value:
                    print("item text:", item.text)
                    item.click()
                    if screen:
                        allure.attach(self.driver.get_screenshot_as_png(),
                                      name="_select_element_on_list_select2_results_Screenshot1",
                                      attachment_type=AttachmentType.PNG)
                    return True
        else:
            return False

    # Метод для выбора элемента в выпадающем списке (класс списка list_dx_list_item)
    def _select_element_on_list_dx_list_item(self, selector, value, screen: bool = False, index=0):

        element = self._element(selector, index)
        print(element)
        element.click()
        self.driver.execute_script("window.scrollTo(0,0)")
        items = self.driver.find_elements(By.CLASS_NAME, "dx-item.dx-list-item")
        items[value].click()
        if screen:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="_select_element_on_list_dx_list_item_Screenshot1",
                          attachment_type=AttachmentType.PNG)

    # Метод для выбора элемента в выпадающем списке (класс списка list_dx_menu_items_containe)
    def _select_element_on_list_dx_menu_items_container(self, selector, value, screen: bool = False, index=0):
        try:
            element = self._element(selector, index)
            print(element)
            element.click()
            html_list = self.driver.find_element_by_class_name('dx-submenu')
            items = html_list.find_elements_by_tag_name("li")
            for item in items:
                if item.text in value:
                    item.click()
                    if screen:
                        allure.attach(self.driver.get_screenshot_as_png(),
                                      name="_select_element_on_list_dx_menu_items_containerScreenshot1",
                                      attachment_type=AttachmentType.PNG)
                    break
        except Exception as e:
            print(e.args)

    # Метод для явного ожидания появления элемента на странице
    def _wait_for_visible(self, selector, link_text=None, index=0, wait=20):
        return WebDriverWait(self.driver, wait).until(EC.visibility_of(self._element(selector, index, link_text)))

    # Метод возвращает текст элемента
    def _get_element_text(self, selector, index):
        return self._element(selector, index).text

# TODO
# def _upload_file  Загрузка файла в форму
