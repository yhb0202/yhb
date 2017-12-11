from peewee import *
from python_test.models.db_config import testModel,db
class Booksmodel(testModel):
	title = CharField(null=True)
	class Meta:
		db_table = 'DmozBooks'
tables = [testModel]
db.connect()
db.create_tables(tables,safe=True)
