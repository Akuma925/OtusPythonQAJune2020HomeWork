class IP_List_Workers:

	btn_create = {'xpath': '//*[@id="dashboardContent"]/div/div[3]/div/button'}
	btn_log_change = {'xpath':'//*[@id="dashboardContent"]/div/div[4]/div/button'}

	class Card_Create_Worker:
		name = {'xpath':'//*[@id="current_133108"]'}
		last_name = {'xpath':'//*[@id="current_133117"]'}
		sure_name = {'xpath':'//*[@id="current_133126"]'}
		subdivision = {'xpath':'//*[@id="select2-chosen-2"]'}
		personnel_number ={'xpath':'//*[@id="current_133090"]'}
		position = {'xpath':'//*[@id="select2-chosen-1"]'}
		btn_create = {'xpath':'//*[@id="dashboardContent"]/div/div[1]/div/button'}
		btn_close_cross={'xpath':'//*[@id="formPopup_132972_127"]/div/div/div/div[1]/button'}

	class Card_Worker:
		title_page = {'xpath':'//*[@id="dashboardContent"]/div/div[9]/label'}