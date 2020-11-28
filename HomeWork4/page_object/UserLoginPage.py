from locators import UserLoginPage as locatorUserLogin
from .BasePage import BasePage


class UserLoginPage(BasePage):

    def open_page(self, url):
        user_login_url = url + locatorUserLogin.USER_LOGIN_URL
        self.driver.get(user_login_url)

    def log_in_as_user(self):
        self._wait_for_visible(locatorUserLogin.LOGIN_FORM)
        self._input(locatorUserLogin.INPUT_EMAIL, locatorUserLogin.USER_EMAIL)
        self._input(locatorUserLogin.INPUT_PASSWORD, locatorUserLogin.USER_PASSWORD)
        self._click(locatorUserLogin.LOGIN_BUTTON)
        return self

    def edit_account(self):
        self._click(locatorUserLogin.EDIT_ACCOUNT_BUTTON)
        return self

    def go_to_wish_list_from_account(self):
        self._click(locatorUserLogin.WISH_LIST)
        return self

    def register_user(self):
        self._wait_for_visible(locatorUserLogin.REGISTER_FORM)
        self._click(locatorUserLogin.REGISTER_CONTINUE)
        self._input(locatorUserLogin.INPUT_EMAIL, locatorUserLogin.USER_EMAIL)
        self._input(locatorUserLogin.INPUT_TEL, locatorUserLogin.USER_TEL)
        self._input(locatorUserLogin.INPUT_FIRST_NAME, locatorUserLogin.USER_FIRST_NAME)
        self._input(locatorUserLogin.INPUT_LAST_NAME, locatorUserLogin.USER_LAST_NAME)
        self._input(locatorUserLogin.INPUT_PASSWORD, locatorUserLogin.USER_PASSWORD)
        self._input(locatorUserLogin.INPUT_CONFIRM_PASSWORD, locatorUserLogin.USER_PASSWORD)
        self._click(locatorUserLogin.NEWSLETTER_CHECKBOX)
        self._click(locatorUserLogin.SUBMIT_BUTTON)
        return self
