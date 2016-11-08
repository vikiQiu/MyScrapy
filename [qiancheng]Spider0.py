# coding=utf-8
#import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")

#from scrapy.spider import BaseSpider
#from scrapy.http import Request
#from scrapy.selector import HtmlXPathSelector
#from qiancheng.items import QianchengItem
#import re
#
#class QianchengSpider(BaseSpider):
#	name='qiancheng'
#	allowed_domains=['51job.com']
#	start_urls=[http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=000000%2C00&funtype=0000&industrytype=00&keyword=%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98&keywordtype=2&lang=c&stype=2&postchannel=0000&fromType=1&confirmdate=9]
#
#	def start_requests(self):abs
#	http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=000000%2C00&district=000000&funtype=0000&industrytype=00&issuedate=9&providesalary=99&keyword=%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98&keywordtype=2&curr_page=3&lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&list_type=0&fromType=14&dibiaoid=0&confirmdate=9
#	http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=000000%2C00&district=000000&funtype=0000&industrytype=00&issuedate=9&providesalary=99&keyword=%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98&keywordtype=2&curr_page=5&lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&list_type=0&fromType=14&dibiaoid=0&confirmdate=9
#import sys 
#reload (sys)   
#sys.setdefaultencoding('gb2312')    

import scrapy
from qiancheng.items import QianchengItem


class QianchengSpider(scrapy.Spider):
    name = "qiancheng"

    DOWNLOAD_DELAY = 2

    def start_requests(self):
    	page_num=10
    	for page in range(page_num):
    		url='http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=000000%2C00&district=000000&funtype=0000&keyword=数据挖掘&keywordtype=2&curr_page='+str(page+1)+'&lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&list_type=0&fromType=14&dibiaoid=0&confirmdate=9'
    		print '第%d页:%s' % (page+1,url)
    		yield scrapy.Request(url=url, callback=self.parse_page)
#
    def parse_page(self, response):
    	bodys=response.css('div.el')
    	for index,body in enumerate(bodys):
    		url=body.css('p.t1 span a::attr(href)').extract_first()
    		if url is None:
    			continue
    		#print '＃＃＃＃第%d个岗位' % index
    		item=QianchengItem()
    		item['job_name']=body.css('p.t1 span a::attr(title)').extract_first()
    		item['job_url']=url
    		item['job_enterprise']=body.css('span.t2 a::attr(title)').extract_first()
    		item['job_place']=body.css('span.t3::text').extract_first()
    		if body.css('span.t4::text'):
    			item['salary']=body.css('span.t4::text').extract_first()
    		else:
    			item['salary']='Null'
    		item['date']=body.css('span.t5::text').extract_first()
    		print item
    		yield item





