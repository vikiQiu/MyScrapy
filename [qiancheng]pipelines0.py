# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv

class QianchengPipeline(object):

	#def open_spider(self,spider):
	#	print '#######################################'
	#	self.f=open('data.csv','wb')
	#	self.ff=csv.writer(self.f)
#
	#def close_spider(self,spider):
	#	self.f.close()

    def process_item(self, item, spider):
    #	ff.writerow([item['job_name'],item['job_enterprise'],item['job_place'],item['job_url']])
        return item
