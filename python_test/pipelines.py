from python_test.items import *
from python_test.models.Dmoz_model import I4model
from python_test.models.I4_detail_model import *
#class Dmoz_pipelines(object):
#	def process_item(self,item,spider):
#		model = Booksmodel()
#		for k,v in item.iteritems():
#			print k
#			print '------'
#			print v[0]
#			setattr(model, k, v[0])
#			#print model
#		model.save()

class I4_pipelines(object):
	print  "ppppppppppp"
	def process_item(self,item,spider):
		if isinstance(item,I4Item):

			model = I4model()
			for k,v in item.iteritems():
				print k
				print '------'
				print v
				setattr(model, k, v)
			model.save()
		return item

class I4_detail_pipelines(object):
	print "hhhhhhhhhh"
	def process_item(self,item,spider):
		if isinstance(item,I4_detailItem):
			model = I4_detail_model()
			for k,v in item,iteritems():
				print k
				print "**************"
				print v
				setattr(model,k,v)
			model.save()
	
		return item
