from python_test.items import *
from python_test.models.Dmoz_model import *
class Dmoz_pipelines(object):
	def process_item(self,item,spider):
		model = Booksmodel()
		for k,v in item.iteritems():
			print k
			print '------'
			print v[0]
			setattr(model, k, v[0])
			#print model
		model.save()
