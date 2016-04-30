# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GalgameSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    link  = scrapy.Field()
    desc  = scrapy.Field()
    pwd   = scrapy.Field()
    addr  = scrapy.Field()
    title = scrapy.Field()
