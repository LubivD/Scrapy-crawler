# -*- coding: utf-8 -*-

import scrapy
import json
import random
from scrapy import Request
from ..items import E27CoTechTaskItem


class E27_Spider(scrapy.Spider):
    name = 'e27_company'
    allowed_domains = ['e27.co']

    def start_requests(self):
        csv_file = 'e27.csv'
        amount_of_links = 250

        with open(csv_file, 'r') as file:
            rows = [row for row in file]
            rows_whithout_header = rows[1:]
            random_data = random.sample(rows_whithout_header, amount_of_links)

            for start_urls in random_data:
                profile_urls = start_urls.replace(',', '')
                slug = profile_urls.split('/')[-1]
                start_urls = 'https://e27.co/api/startups/get/?' \
                             'slug={}&data_type=general&get_badge=true'.format(slug)

                yield Request(start_urls, self.parse_first_part)

    def parse_first_part(self, response):
        item = E27CoTechTaskItem()

        data = json.loads(response.body)
        list_of_data = data['data']
        item['id'] = list_of_data.get('id')
        item['company_name'] = list_of_data.get('name')
        item['request_url'] = 'https://e27.co/startups/' + list_of_data.get('slug')
        item['request_company_url'] = list_of_data.get('metas').get('website')
        item['location'] = list_of_data.get('location')[0].get('text')
        item['tags'] = list_of_data.get('metas').get('market')
        item['founding_date'] = list_of_data.get('metas').get('found_month'), \
                                list_of_data.get('metas').get('found_year')
        item['founders'] = ''
        item['employee_range'] = ''
        item['urls'] = list_of_data.get('metas').get('facebook'), \
                       list_of_data.get('metas').get('linkedin'), \
                       list_of_data.get('metas').get('twitter')
        item['emails'] = ''
        item['phones'] = ''
        item['description_short'] = list_of_data.get('metas').get('short_description')
        item['description'] = list_of_data.get('metas').get('description')
        yield item
