
class CommonTool:

	def get_key(self, d:dict, value:str):
		for k, v in d.items():
			if v == value:
				return k

	def create_name_func(my_function):
		return my_function.__name__
