from locators import ProductPage
from .BasePage import BasePage


class ProductPage(BasePage):

    def open_page(self, url, product_id=49):
        product_page_url = url + self.PRODUCT_PAGE_URL + str(product_id)
        self.browser.get(product_page_url)

    def add_to_wishlist(self):
        self._click(self.ProductPage.ADD_TO_WISHLIST)
        return self

    def add_to_cart(self):
        self._click(self.ProductPage.ADD_TO_CART)
        return self

    def get_product_name(self):
        self._get_element_text(self.ProductPage.PRODUCT_NAME)
        return self

    def get_cart_name_from_page(self):
        self._get_element_text(self.ProductPage.get_product_name())
        return self

    def click_review(self):
        self._wait_for_visible(self.ProductPage.CLICK_REVIEW)
        self._click(self.ProductPage.CLICK_REVIEW)
        return self

    def send_review(self):
        self._click(self.ProductPage.SEND_REVIEW)
        return self

    def get_product_price(self):
        self._get_element_text(self.ProductPage.PRODUCT_PRICE)
        return self
