# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class E27CoTechTaskItem(scrapy.Item):
    # define the fields for your item here like:
    link = scrapy.Field()
    id = scrapy.Field()
    company_name = scrapy.Field()
    request_url = scrapy.Field()
    request_company_url = scrapy.Field()
    location = scrapy.Field()
    tags = scrapy.Field()
    founding_date = scrapy.Field()
    founders = scrapy.Field()
    employee_range = scrapy.Field()
    urls = scrapy.Field()
    emails = scrapy.Field()
    phones = scrapy.Field()
    description_short = scrapy.Field()
    description = scrapy.Field()
    # pass
