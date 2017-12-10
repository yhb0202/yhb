from python_test.items import *
from python_test.models.Dmoz_model import *
class Dmoz_pipelines(object):
	def process_item(self,item,spider):
		model = testModel()
		for k,v in item.iteritems():
			setattr(model, k, v)
		model.save()
