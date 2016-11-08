# MyScrapy
## 1. Item
设置要爬去的内容
```python
#### items.py
from scrapy.item import Item, Field
class QianchengItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 岗位名称
    job_name=Field()
    # 对应链接
    job_url=Field()
    # 公司名称
    job_enterprise=Field()
    # 公司工作地点
    job_place=Field()
    # 工资
    salary=Field()
    # date
    date=Field()
    pass  
```
## 2. Spider
需要加载的包：
``` python
import scrapy
from qiancheng.items import QianchengItem # 在item=QianchengItem()会用到
```
设置必要的变量：
``` python
name = "qiancheng" #爬虫名称
DOWNLOAD_DELAY = 2 # 延长时间
```
如果设置了start_urls会自动遍历所有urls并调用parse函数。
**start_requests**函数
```python
def start_requests(self):
	page_num=10
	for page in range(page_num):
		url='http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=000000%2C00&district=000000&funtype=0000&keyword=数据挖掘&keywordtype=2&curr_page='+str(page+1)+'&lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&list_type=0&fromType=14&dibiaoid=0&confirmdate=9'
	  print '第%d页:%s' % (page+1,url)
  	yield scrapy.Request(url=url, callback=self.parse_page)
```
