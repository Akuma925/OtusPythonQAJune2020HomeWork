from page_object import LoginPage, MainPage, IPListWorkerPage, IPDocInfoSecPage, DocPanel, IP_ListWorker
import datetime
import time
import allure
from allure_commons.types import AttachmentType

def login(browser):
    assert LoginPage(browser) \
        .login_user("Autotest", "1qaz2wsX#",'SAOB-dev')


@allure.severity(allure.severity_level.MINOR)
@allure.description("""
Test call_list_worker
""")
def test_call_list_worker(browser):
     login(browser)
     assert MainPage(browser)\
           .call_IP_list()


# @allure.severity(allure.severity_level.MINOR)
# @allure.description("""
# create_new_worker
# """)
#
# def test_create_new_worker(browser):
#      login(browser)
#      MainPage(browser).call_IP_list()
#      browser.implicitly_wait(5)
#      assert IP_ListWorker(browser).click_create_new_worker()
#      browser.implicitly_wait(3)
#      assert IP_ListWorker(browser).set_data_worker("Стрельцов","Федот","Федотыч","Подразделение 2, СТД - ДСИ - ОРРАПУИБ - ГПиРСУИБ2 ","123321456654","Инженер")
#      assert IP_ListWorker(browser).click_approve_create()
#      browser.implicitly_wait(5)
#      assert  IP_ListWorker(browser).chcek_title_card_worker("Стрельцов Федот Федотыч")
