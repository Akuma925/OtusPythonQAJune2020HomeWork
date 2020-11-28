from locators import Main as locatorMain
from .BasePage import BasePage


class MainPage(BasePage):

    def open_main_page(self, url):
        self.driver.get(url)

    def get_main_product_name(self, index=0):
        self._get_element_text(locatorMain.MAIN_PRODUCT_NAME, index)
        return self

    def get_main_product_price(self, index=0):
        price_element = self._get_element_text(locatorMain.MAIN_PRODUCT_PRICE, index)
        price_element = price_element.split('\n')[0]
        price_element = price_element.split(' ')[0]
        return price_element

    def click_main_product_name(self, index=0):
        self._click(locatorMain.MAIN_PRODUCT_NAME, False, index)
        return self

    def click_main_product_picture(self, index=0):
        self._click(locatorMain.MAIN_PRODUCT_PICTURE, False, index)
        return self

    def click_slider_button_next(self):
        self._click(locatorMain.MAIN_SLIDER_BUTTON_NEXT)
        return self
