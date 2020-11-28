from locators import  CatalogPage, IP_List_Workers
from.BasePage import BasePage
from .common.CommonTool import CommonTool
import time

class IP_ListWorker(BasePage):

	def click_create_new_worker(self):
		self._click(CatalogPage.IP_List_Workers.btn_create, True)
		return True

	def set_data_worker(self,last_name,name_worker,sure_name,subdivision,pesr_number,position):
		self._input(IP_List_Workers.Card_Create_Worker.last_name,last_name,True)
		self._input(IP_List_Workers.Card_Create_Worker.name,name_worker, True)
		self._input(IP_List_Workers.Card_Create_Worker.sure_name, sure_name, True)
		self._select_element_on_list_select2_results(IP_List_Workers.Card_Create_Worker.subdivision,subdivision,True)
		self._input(IP_List_Workers.Card_Create_Worker.personnel_number, pesr_number, True)
		self._select_element_on_list_select2_results(IP_List_Workers.Card_Create_Worker.position,position,True)
		time.sleep(self.small_sleep)
		return True

	def click_approve_create(self):
		self._click(IP_List_Workers.Card_Create_Worker.btn_create,True)
		return True
	def chcek_title_card_worker(self,value):
		elem = self._element(IP_List_Workers.Card_Worker.title_page,0)
		if elem.text == value:
			return True
		else:
			return False