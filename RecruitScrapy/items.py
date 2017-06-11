# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RecruitscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class RecruitItem(scrapy.Item):
    recruitName = scrapy.Field()    #职位名称
    respond = scrapy.Field()        #回应率
    companyName = scrapy.Field()    #公司名
    companyPlace = scrapy.Field()   #公司地点
    companyType = scrapy.Field()    #公司类别
    companySize =  scrapy.Field()   #公司大小
    experience = scrapy.Field()     #经验
    education = scrapy.Field()      #学历
    wages = scrapy.Field()           #工资
    releaseDate = scrapy.Field()     #发布简历日期

