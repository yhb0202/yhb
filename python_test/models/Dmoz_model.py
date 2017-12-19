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
