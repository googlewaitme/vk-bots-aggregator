from peewee import *


db = SqliteDatabase('bots.db')

def create_tables():
    with db:
        db.create_tables([Category, ChatBot])


class BaseModel(Model):
	class Meta:
		database = db


class Category(BaseModel):
	id = AutoField()
	name = CharField(unique=True)
	description = TextField()


class ChatBot(BaseModel):
	id = AutoField()	
	name = CharField()
	url = CharField()
	description = CharField(max_length=80)
	priority = IntegerField(default=5)
	category = ForeignKeyField(Category, backref='chatbots')
	author = CharField(max_length=15)
	admin = CharField(max_length=15)
