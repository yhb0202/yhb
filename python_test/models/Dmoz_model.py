from peewee import *
from python_test.models.db_config import testModel,db
class Booksmodel(testModel):
	title = CharField(null=True)
	class Meta:
		db_table = 'DmozBooks'
tables = [Booksmodel]
db.connect()
db.create_tables(tables,safe=True)
