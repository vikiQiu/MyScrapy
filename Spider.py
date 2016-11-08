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

    DOWNLOAD_DELAY = 1
    COOKIES_ENABLED=False

    def start_requests(self):
    	page_num=10
        keyword='数据挖掘'
    	for page in range(10,10+page_num):
    		url='http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=000000%2C00&district=000000&funtype=0000&keyword='+keyword+'&keywordtype=2&curr_page='+str(page+1)+'&lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&list_type=0&fromType=14&dibiaoid=0&confirmdate=9'
    		print '######################  第%d页:%s  ###################' % (page+1,url)
    		yield scrapy.Request(url=url, callback=self.parse_page)
#
    def parse_page(self, response):
    	bodys=response.css('div.el')
    	for index,body in enumerate(bodys):
    	    url=body.css('p.t1 span a::attr(href)').extract_first()
    	    if url is None:
    	    	continue
    	    #print '＃＃＃＃第%d个岗位########## new new new' % index
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
            if index > -1: 
    	        yield scrapy.Request(url=url,callback=self.parse_content,meta=item)
                item['edu']=response.css('em.i2::text').extract_first()
            
    def parse_content(self,response):
        item=response.meta
        temp=response.css('span.sp4')
        # education
        edu=temp.re(r'<em class="i2"></em>\s*(.*)</span>')
        item['edu']=edu if len(edu)==1 else 'Null'
        # 招聘人数
        num=temp.re(r'<em class="i3"></em>\s*(.*)</span>')
        item['job_num']=num if len(num)==1 else 'Null'
        # 工作经验
        exp=temp.re(r'<em class="i1"></em>\s*(.*)</span>')
        item['job_exp']=exp if len(exp)==1 else 'Null'
        # 具体信息
        temp=response.xpath('//div[@class="bmsg job_msg inbox"]/text()').extract()
        info=''
        for i in temp:
            info=info+i.strip()
        item['job_info']=info
        # 公司信息
        temp=response.xpath('//p[@class="msg ltype"]/text()').extract_first().split()
        item['enterprise_attr']=temp[0]
        item['enterprise_scale']=temp[2]
        item['enterprise_industry']=temp[4]

        yield item





