from locators import Alert as locatorAlert
from .BasePage import BasePage


class Alert(BasePage):
    def wait_success_alert(self):
        self._wait_for_visible(locatorAlert.SUCCESS_ALERT)
        return self

    def click_login(self):
        self._click(locatorAlert.Alert.SUCCESS_ALERT_LOGIN)

    def click_to_cart(self):
        self._click(locatorAlert.Alert.SUCCESS_ALERT_TO_CART)

    def click_to_wish_list(self):
        self._click(locatorAlert.Alert.SUCCESS_ALERT_TO_WISH_LIST)

    def wait_danger_alert(self):
        self._wait_for_visible(locatorAlert.Alert.DANGER_ALERT)
        return self
