# -*- coding: utf-8 -*-
import scrapy
from items import RecruitItem
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class GetrecruitlistSpider(scrapy.Spider):
    name = "getRecruitList"
    allowed_domains = ["http://sou.zhaopin.com","sou.zhaopin.com"]
    #start_urls = ['http://sou.zhaopin.com/']
    start_urls = ['']


    def __init__(self, region=u'选择地区', kw=u'爬虫', *args, **kwargs):
        super(GetrecruitlistSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://sou.zhaopin.com/jobs/searchresult.ashx?jl={0}&kw={1}'.format(region, kw)]
        self.kw = kw

    def parse(self, response):

        item = RecruitItem()
        # 解析获取数据
        for sel in response.css('table.newlist'):
            item['recruitName'] = self.kw.join(sel.xpath( 'tr[1]/td[1]/div/a/text()').extract())
            item['respond'] = sel.xpath('tr[1]/td[2]/span/text()').extract()
            item['companyName'] = sel.xpath('tr[1]/td[3]/a/text()').extract()
            item['companyPlace'] = sel.xpath('tr[2]/td/div/div/ul/li[1]/span[1]/text()').extract()
            item['companyType'] = sel.xpath('tr[2]/td/div/div/ul/li[1]/span[2]/text()').extract()
            item['companySize'] = sel.xpath('tr[2]/td/div/div/ul/li[1]/span[3]/text()').extract()
            item['education'] = sel.xpath('tr[2]/td/div/div/ul/li[1]/span[last()-1]/text()').extract()
            item['wages'] = sel.xpath('tr[1]/td[4]/text()').extract()
            item['releaseDate'] = sel.xpath('tr[1]/td[6]/span/text()').extract()

            if len(sel.xpath('tr[2]/td/div/div/ul/li[1]/span/text()').extract())>5:
                item['experience'] = sel.xpath('tr[2]/td/div/div/ul/li[1]/span[4]/text()').extract()

            yield item

        # 查询是否还有后面页
        next_page = response.css('a.next-page').xpath('@href').extract()
        if (next_page):
            yield scrapy.Request(next_page[0], callback=self.parse)