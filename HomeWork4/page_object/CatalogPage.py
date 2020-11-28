from locators import CatalogPage as locatorCatalog
from .BasePage import BasePage


class CatalogPage(BasePage):

    def open_page(self, url, product_id=20):
        catalog_page_url = url + locatorCatalog.CATALOG_URL + str(product_id)
        self.driver.get(catalog_page_url)

    def get_catalog_section_name(self):
        self._get_element_text(locatorCatalog.SECTION_NAME)
        return self

    def add_to_compare(self):
        self._click(locatorCatalog.COMPARE_BUTTON)
        return self

    def go_to_compare_list(self):
        self._wait_for_visible(locatorCatalog.ALL_COMPARE_LIST)
        self._click(locatorCatalog.ALL_COMPARE_LIST)
        return self
