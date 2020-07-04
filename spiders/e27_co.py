# -*- coding: utf-8 -*-

import json
import scrapy
from scrapy import Request
from ..items import E27CoTechTaskItem


class E27_Spider(scrapy.Spider):
    name = 'e27'
    allowed_domains = ['e27.co']
    start = 0
    start_urls = [
        "https://e27.co/api/startups/?all_fundraising=&pro=0&tab_name=recentlyupdated&start={}&length=10".format(start)
    ]

    def parse(self, response):
        data = json.loads(response.body)
        item = E27CoTechTaskItem()
        # start = 0
        list_of_data = data['data']['list']
        total_startup_count = int(data['data']['totalstartupcount'])

        for link in list_of_data:
            item['link'] = 'https://e27.co/startups/' + link.get('slug')
            yield item

        if item:
            self.start += 10
            print(f'You are on {self.start} page')
            url = 'https://e27.co/api/startups/?all_fundraising=&pro=0&tab_name=recentlyupdated&start={}&length=10'.format(self.start)
            yield Request(url=url, callback=self.parse, priority=1)
