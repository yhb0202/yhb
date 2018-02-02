from peewee import *
from python_test.models.db_config import testModel,db

class qiubaimodel(testModel):
    author = CharField()
    title = CharField()
    content = CharField()
    class Meta:
         db_table = 'qiubais'
tables = [qiubaimodel]
db.connect()
db.create_tables(tables,safe=True)

class ajkmodel(object):
	title = CharField()
	link = CharField()
	address = CharField()
	house_type = CharField()
	info = CharField()
	price = CharField()
	home = CharField()
	class Meta:
		db_table = 'ajk_info'
tables = [ajkmodel]
db.connect()
db.create_tables(tables,safe=True)
