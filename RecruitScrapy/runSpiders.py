#!/usr/bin/python
# -*- coding: utf-8 -*-
from  scrapy import cmdline

#运行爬去首页的电影数据
cmd = 'scrapy  crawl {0} -o {1}'.format('getRecruitList','data\getRecruitList.csv')
cmdline.execute(cmd.split())