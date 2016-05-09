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
        "http://www.mygalgame.com/page/11/",
        "http://www.mygalgame.com/page/12/",
        "http://www.mygalgame.com/page/13/",
        "http://www.mygalgame.com/page/14/",
        "http://www.mygalgame.com/page/15/",
        "http://www.mygalgame.com/page/16/",
        "http://www.mygalgame.com/page/17/",
        "http://www.mygalgame.com/page/18/",
        "http://www.mygalgame.com/page/19/",
        "http://www.mygalgame.com/page/20/",
    ]

    def parse(self, response):

        for href in response.xpath('//div[@class = "title-article"]/center/h4/a/@href'):
            url = response.urljoin( href.extract())

            yield scrapy.Request(url, callback = self.parse_dir_contents)

    def parse_dir_contents(self,response):
        item = GalgameSpiderItem()
        item['pwd'] = response.xpath('//div[@class = "panel panel-primary"]/div[@class = "panel-footer"]/b//span/text()')[0:2].extract()
        item['addr'] = response.xpath('//div[@class = "panel panel-primary"]/div[@class = "panel-body"]/a/button/@onclick').re('\\/pan\\.baidu\\.com\\/s\\/.*[^.)]')
        item['title'] = response.xpath('//div[@class = "title-article"]/h4/a/text()').extract()
        yield item






