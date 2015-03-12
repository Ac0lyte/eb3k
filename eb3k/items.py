# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class eb3KItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    thumb = scrapy.Field()
    image = scrapy.Field()
    page = scrapy.Field()
    date = scrapy.Field()
    #pass
