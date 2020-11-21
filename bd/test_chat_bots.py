from bd.models import ChatBot, Category
from bd.logik import ChatBotApi

class TestDBChatBots:

	def setup(self):
		self.chat_bot_api = ChatBotApi()
		self.ufa_category = Category.create(name='UfaBot', description='That bots from ufa')
		self.dataset = {
			'name': 'ufa',
			'url': '@ufa',
			'description': 'ufa',
			'priority': 5,
			'category': self.ufa_category,
			'author': '123',
			'admin': '123'
		}
		self.list_chatbots = []
		for i in range(5):
			now_dataset = self.dataset
			now_dataset['name'] = 'ufa' + str(i)
			now_chatbot = ChatBot.create(**self.dataset)	
			self.list_chatbots.append(now_chatbot)

	def teardown(self):
		self.ufa_category.delete_instance()
		for chat_bot in self.list_chatbots:
			chat_bot.delete_instance()

	def test_backref(self):
		pass

	def test_is_exist(self):
		exist_chat_bot_id = self.list_chatbots[0].id
		assert self.chat_bot_api.is_exist(exist_chat_bot_id)

	def test_is_not_exist(self):
		assert not self.chat_bot_api.is_exist(10)

	def test_delete_by_id(self):
		assert self.chat_bot_api.is_exist(5)
		self.chat_bot_api.delete_by_id(5)
		assert not self.chat_bot_api.is_exist(5)

	def test_make(self):
		assert not self.chat_bot_api.is_exist(5)
		self.chat_bot_api.make(**self.dataset)
		assert self.chat_bot_api.is_exist(5)
		
