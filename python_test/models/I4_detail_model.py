from peewee import *
from python_test.models.db_config import testModel,db

class I4_detail_model(testModel):
	title = CharField()
	source = CharField()
	read_num = CharField()
	report_date = CharField()
	class Meta:
		db_table = 'iphone2'
tables = [I4_detail_model]
#db.connect()
db.create_tables(tables,safe=True)
