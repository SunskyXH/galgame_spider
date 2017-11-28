# -*- coding: utf-8 -*-
import scrapy

class GalgameSpiderItem(scrapy.Item):
    link  = scrapy.Field()
    desc  = scrapy.Field()
    pwd   = scrapy.Field()
    addr  = scrapy.Field()
    title = scrapy.Field()
    date  = scrapy.Field()
