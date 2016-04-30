# -*- coding:utf-8 -*-

import scrapy
from scrapy.selector import Selector
from scrapy import log
from galgame_spider.items import GalgameSpiderItem

class MyGalgameSpider(scrapy.Spider):
    name = "MGS"
    start_urls = [
        "http://www.mygalgame.com",
        "http://www.mygalgame.com/page/2/",
        "http://www.mygalgame.com/page/3/",
        "http://www.mygalgame.com/page/4/",
        "http://www.mygalgame.com/page/5/",
        "http://www.mygalgame.com/page/6/",
        "http://www.mygalgame.com/page/7/",
        "http://www.mygalgame.com/page/8/",
        "http://www.mygalgame.com/page/9/",
        "http://www.mygalgame.com/page/10/",
    ]

    def parse(self, response):

        for href in response.xpath('//div[@class = "title-article"]/center/h4/a/@href'):
            url = response.urljoin( href.extract())

            yield scrapy.Request(url, callback = self.parse_dir_contents)

    def parse_dir_contents(self,response):
        for sel in response.xpath('//div[@class = "title-article"]/h4/a/text()'):
            for sel2 in response.xpath('//div[@class = "panel panel-primary"]'):
                item = GalgameSpiderItem()
                item['pwd'] = sel2.xpath('//div[@class = "panel-footer"]/b//span/text()')[0:2].extract()
                item['addr'] = sel2.xpath('//div[@class = "panel-body"]/a/button/@onclick').re('\\/pan\\.baidu\\.com\\/s\\/.*[^.)]')
            item['title'] = sel.extract()
        yield item






