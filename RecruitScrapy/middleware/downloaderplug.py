# -*- coding: utf-8 -*-
import scrapy
import random
import base64
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware
#from ..proxylists import PROXIES
from ..config.user_agents import user_agent_list

"""
避免被ban策略之一：使用useragent池。
使用注意：需在settings.py中进行相应的设置。
"""

class RandomUserAgent(UserAgentMiddleware):

    def __init__(self,user_agent=''):
        self.user_agent = user_agent
        self.user_agent_list = user_agent_list

    def process_request(self, request, spider):
        ua = random.choice(self.user_agent_list)
        if ua:
            # 记录
            #scrapy.log.msg('Current UserAgent: ' + ua, level='INFO')
            print '------UserAgent------[' + ua +']'
            request.headers.setdefault('User-Agent', ua)


