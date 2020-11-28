from locators import ProductPage as locatorsProduct
from .BasePage import BasePage


class ProductPage(BasePage):

    def open_page(self, url, product_id=49):
        product_page_url = url + locatorsProduct.ProductPage.PRODUCT_PAGE_URL + str(product_id)
        self.driver.get(product_page_url)

    def add_to_wishlist(self):
        self._click(locatorsProduct.ProductPage.ADD_TO_WISHLIST)
        return self

    def add_to_cart(self):
        self._click(locatorsProduct.ProductPage.ADD_TO_CART)
        return self

    def get_product_name(self):
        self._get_element_text(locatorsProduct.ProductPage.PRODUCT_NAME, 0)
        return self

    def get_cart_name_from_page(self):
        self._get_element_text(self.get_product_name(), 0)
        return self

    def click_review(self):
        self._wait_for_visible(locatorsProduct.ProductPage.CLICK_REVIEW)
        self._click(locatorsProduct.ProductPage.CLICK_REVIEW)
        return self

    def send_review(self):
        self._click(locatorsProduct.ProductPage.SEND_REVIEW)
        return self

    def get_product_price(self):
        self._get_element_text(locatorsProduct.ProductPage.PRODUCT_PRICE, 0)
        return self
