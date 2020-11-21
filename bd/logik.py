from bd.models import ChatBot, Category 


class BaseApi:
	def __init__(self, obj):
		self.obj = obj

	def make(self, **kwargs):
		self.obj.create(**kwargs)

	def is_exist(self, instance_id):
		query = self.obj.select(self.obj.id == instance_id)
		data = list(query)
		return len(data) == 1

	def delete_by_id(self, instance_id):
		instance = self.obj.get(self.obj.id == instance_id)
		instance.delete_instance()



class ChatBotApi(BaseApi):
	def __init__(self):
		self.obj = ChatBot


class CategoryApi:
	def __init__(self):
		self.obj = Category
