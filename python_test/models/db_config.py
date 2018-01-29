from peewee import *
db = MySQLDatabase(
	host = "127.0.0.1",
	database = "test_01",
	user = "root",
	passwd = "password",
	charset = "utf8"
)
class testModel(Model):
	class Meta:
		database = db
