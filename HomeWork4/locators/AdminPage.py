class IPDocInfoSec:

	class doc_panel_tab:
		all = {'xpath':'//*[@id="dashboardContent"]/div/div[1]/div/ul/li[1]/a'}
		reference = {'xpath':'//*[@id="dashboardContent"]/div/div[1]/div/ul/li[2]/a'}
		for_chek = {'xpath' : '//*[@id="dashboardContent"]/div/div[1]/div/ul/li[3]/a'}
		for_exec = {'xpath' : '//*[@id="dashboardContent"]/div/div[1]/div/ul/li[4]/a'}

	class tab_all:

		global_checkbox = {'xpath':'//*[@id="grid_70977"]/div/table/tbody/tr[2]/td[2]/div/div[5]/div/table/tbody/tr['
		                           '1]/td[1]/div/div/span'} #120158

		class filter:
			name_doc={'xpath': '//*[@id="grid_70977"]/div/table/tbody/tr[2]/td[2]/div/div[5]/div/table/tbody/tr['
			                   '2]/td[2]/div/div[2]/div/div/input'}
			type_doc={'xpath':'//*[@id="grid_70977"]/div/table/tbody/tr[2]/td[2]/div/div[5]/div/table/tbody/tr[2]/td[3]/div/div[2]/div/div[1]/div/div[2]/div/div/div'}

			area = {'xpath':'//*[@id="grid_70977"]/div/table/tbody/tr[2]/td[2]/div/div[5]/div/table/tbody/tr[2]/td['
			                '4]/div/div[2]/div/div/div/div[1]'}
			status = {'xpath': '//*[@id="grid_70977"]/div/table/tbody/tr[2]/td[2]/div/div[5]/div/table/tbody/tr['
			                   '2]/td[6]/div/div/div/div/div/input'}

			name_doc_search_btn = {'xpath': '//*[@id="grid_70977"]/div/table/tbody/tr[2]/td[2]/div/div['
			                                '5]/div/table/tbody/tr[2]/td[2]/div/div[1]/div/ul/li/div/div[1]/span'}

			type_doc_search_btn = {'xpath': '//*[@id="grid_70977"]/div/table/tbody/tr[2]/td[2]/div/div['
			                                '5]/div/table/tbody/tr[2]/td[3]/div/div[1]/div/ul/li/div/div[1]/span'}

			area_search_btn = {'xpath': '//*[@id="grid_70977"]/div/table/tbody/tr[2]/td[2]/div/div['
			                            '5]/div/table/tbody/tr[2]/td[4]/div/div[1]/div/ul/li/div/div[1]/span'}

			type_sort_name_doc = {'xpath':'//*[@id="dx-03331cf7-502b-31eb-428b-4876bab3fc7b"]/div[1]'}
			type_sort_type_doc = {'xpath': '//*[@id="dx-164d5824-65e8-e63d-be3c-381464ee28ab"]/div[1]'}
			type_sort_area = {'xpath': '//*[@id="dx-2cee5409-227d-d76d-b5d3-01b7dd3353e5"]/div[1]'}

		class workspace:
			send_to_archive_btn = {'xpath':'//*[@id="dashboardContent"]/div/div[1]/div/div/div[1]/div/div/div[4]/div/button'}
			delete_btn = {'xpath':'//*[@id="dashboardContent"]/div/div[1]/div/div/div[1]/div/div/div[3]/div/button'}
			create_btn = {'xpath' : '//*[@id="dashboardContent"]/div/div[1]/div/div/div[1]/div/div/div[2]/div/button'}
			search_edit = {'xpath' : '//*[@id="grid_120158"]/div/table/tbody/tr[2]/td[2]/div/div[4]/div/div/div['
			                         '3]/div/div/div/div/input'}

	class tab_reference:
		global_checkbox = {'xpath': '//*[@id="grid_120158"]/div/table/tbody/tr[2]/td[2]/div/div[5]/div/table/tbody/tr['
		                            '1]/td[1]/div/div/span'}
		class filter:

			name_doc = {'xpath': '//*[@id="grid_120202"]/div/table/tbody/tr[2]/td[2]/div/div[5]/div/table/tbody/tr[2]/td[2]/div/div[2]/div/div/input'}

			kind_doc = {'xpath': '//*[@id="grid_120202"]/div/table/tbody/tr[2]/td[2]/div/div[5]/div/table/tbody/tr[2]/td[3]/div/div[2]/div/div/input'}

			area = {'xpath': '//*[@id="grid_120202"]/div/table/tbody/tr[2]/td[2]/div/div[5]/div/table/tbody/tr[2]/td[4]/div/div[2]/div/div[1]/div/div[2]/div/div/div'}

			status = {'xpath': '//*[@id="grid_120202"]/div/table/tbody/tr[2]/td[2]/div/div[5]/div/table/tbody/tr[2]/td[7]/div/div/div/div/div/div[2]/div/div/div'}

			link = {'xpath':'//*[@id="grid_120202"]/div/table/tbody/tr[2]/td[2]/div/div[5]/div/table/tbody/tr[2]/td[5]/div/div[2]/div/div/input'}

			author_record = {'xpath':'//*[@id="grid_120202"]/div/table/tbody/tr[2]/td[2]/div/div[5]/div/table/tbody/tr[2]/td[6]/div/div[2]/div/div/input'}

			name_doc_search_btn = {'xpath': '//*[@id="grid_120202"]/div/table/tbody/tr[2]/td[2]/div/div[5]/div/table/tbody/tr[2]/td[2]/div/div[1]/div/ul/li/div/div[1]/span'}

			kind_doc_search_btn = {'xpath': '//*[@id="grid_120202"]/div/table/tbody/tr[2]/td[2]/div/div[5]/div/table/tbody/tr[2]/td[3]/div/div[1]/div/ul/li/div/div[1]/span'}

			area_search_btn = {'xpath': '//*[@id="grid_120202"]/div/table/tbody/tr[2]/td[2]/div/div[5]/div/table/tbody/tr[2]/td[4]/div/div[1]/div/ul/li/div/div[1]/span'}

			link_search_btn = {'xpath': '//*[@id="grid_120202"]/div/table/tbody/tr[2]/td[2]/div/div[5]/div/table/tbody/tr[2]/td[5]/div/div[1]/div/ul/li/div/div[1]/span'}

			author_record_search_btn = {'xpath': '//*[@id="grid_120202"]/div/table/tbody/tr[2]/td[2]/div/div[5]/div/table/tbody/tr[2]/td[6]/div/div[1]/div/ul/li/div/div[1]/span'}

		class workspace:

			send_to_archive_btn = {'xpath':'//*[@id="dashboardContent"]/div/div[1]/div/div/div[2]/div/div/div[4]/div/button'}

			delete_btn = {'xpath':'//*[@id="dashboardContent"]/div/div[1]/div/div/div[2]/div/div/div[3]/div/button'}

			create_btn = {'xpath' : '//*[@id="dashboardContent"]/div/div[1]/div/div/div[2]/div/div/div[2]/div/button'}

			search_edit = {'xpath' : '//*[@id="grid_120202"]/div/table/tbody/tr[2]/td[2]/div/div[4]/div/div/div[3]/div/div/div/div/input'}
