from peewee import *
from python_test.models.db_config import testModel,db
class Booksmodel(testModel):
	title = CharField()
	class Meta:
		db_table = 'DmozBooks'
tables = [Booksmodel]
print tables
db.connect()
db.create_tables(tables,safe=True)

class I4model(testModel):
	title = CharField()
	class Meta:
		db_table = 'iphone'
tables = [I4model]
print tables
db.connect()
db.create_tables(tables,safe=True)
