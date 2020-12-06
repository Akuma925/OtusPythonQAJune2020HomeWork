import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# Базовый класс имплементирующий основные методы работы с элементами web-странички
class BasePage:
    # Конструктор класса
    #
    #  на вход нужно передать драйвер управления браузером
    def __init__(self, driver):
        self.driver = driver

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
        return self.driver.find_elements(by, selector)[index]

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

    # Метод для явного ожидания появления элемента на странице
    def _wait_for_visible(self, selector, link_text=None, index=0, wait=20):
        return WebDriverWait(self.driver, wait).until(EC.visibility_of(self._element(selector, index, link_text)))

    # Метод возвращает текст элемента
    def _get_element_text(self, selector, index):
        return self._element(selector, index).text

    def _go_to_element(self, selector, link_text=None, index=0):
        return self._element(selector, index, link_text).location_once_scrolled_into_view

    def _go_to_down_page(self):
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    def _go_up_page(self):
        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
