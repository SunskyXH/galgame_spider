# -*- coding:utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy import log
import time
from galgame_spider.items import GalgameSpiderItem

class MyGalgameSpider(scrapy.Spider):
    start_time = time.time()
    name = "MGS"
    start_urls = ["http://www.mygalgame.com"]
    page_number = 72
    for i in range(2, page_number+1):
        start_urls.append("http://www.mygalgame.com/page/"+str(i)+"/")
    print(u'爬虫程序开始运行')

    def parse(self, response):
        for href in response.xpath('//div[@class = "title-article"]/center/h4/a/@href'):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback = self.parse_dir_contents)

    def parse_dir_contents(self,response):
        item = GalgameSpiderItem()
        item['pwd'] = response.xpath('//div[@class = "panel panel-primary"]/div[@class = "panel-footer"]/b//span/text()')[0:2].extract()
        item['addr'] = response.xpath('//div[@class = "panel panel-primary"]/div[@class = "panel-body"]/a/button/@onclick').re('\\/pan\\.baidu\\.com\\/s\\/.*[^.)]')
        item['title'] = response.xpath('//div[@class = "title-article"]/h4/a/text()').extract()
        item['date'] = response.xpath('//span[@class = "label label-zan"]/text()')[0].extract()
        yield item