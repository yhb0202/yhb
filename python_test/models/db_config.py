from peewee import *
db = MySQLDatabase(
	host = "127.0.0.1",
	database = "test",
	user = "root",
	passwd = "yuan0202",
	charset = "utf8"
)
class testModel(Model):
	class Meta:
		database = db
