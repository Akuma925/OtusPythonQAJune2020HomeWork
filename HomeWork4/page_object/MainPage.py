from locators import Common, Main, IPListWorker, IP_List_Workers
from.BasePage import BasePage
from .common.CommonTool import CommonTool
import time
class MainPage(BasePage):

	def call_IP_doc(self):
		self._click(Main.left_panel_mini.expend_panel,True)
		time.sleep(self.small_sleep)
		self._click(Main.left_panel_mini.SAOB,True)
		time.sleep(self.small_sleep)
		self._click(Main.left_panel_mini.IP_SAOB,True)
		time.sleep(self.small_sleep)
		self._click(Main.left_panel_mini.UDIB_doc,True)
		time.sleep(self.small_sleep)
		return True

	def call_IP_list(self):
		self._click(Main.left_panel_mini.expend_panel, True)
		#time.sleep(self.small_sleep)
		self._click(Main.left_panel_mini.SAOB, True)
		#time.sleep(self.small_sleep)
		self._click(Main.left_panel_mini.UDIB_list,True)
		#time.sleep(self.small_sleep)
		self._click(Main.left_panel_mini.UDIB_list_worker,True)
		return True
