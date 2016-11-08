# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

#import scrapy
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
