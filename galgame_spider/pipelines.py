# -*- coding: utf-8 -*-
import codecs
import json
import time

class GalgameSpiderPipeline(object):
    def __init__(self):
        self.game_list_json = codecs.open('game_list.json','w+',encoding='utf-8')
        self.game_list = codecs.open('game_list','w+',encoding='utf-8')
        self.change_log = codecs.open('changelog', 'r+', encoding='utf-8')
        self.data = []

    def process_item(self, item, spider):
        if item != [] and item['addr'] != []:
            item['addr'] = item['addr'][0].lstrip("/").rstrip("'")
            item['title'] = item['title'][0]
            item['pwd'] = item['pwd'][0].rstrip(u"：") + ":" + item['pwd'][1]
            item['date'] = item['date'].lstrip()
            line = json.dumps(dict(item), ensure_ascii=False) + "\r\n"
            self.data.append(item)
            self.game_list_json.write(line)
        return '[INFO]FINISH'

    def close_spider(self, spider):
        for i in self.data:
            addr = i['addr']
            title = i['title']
            pwd = i['pwd']
            date = i['date']
            self.game_list.write(u"标题:"+title+"\r\n")
            self.game_list.write(u"日期:" + date + "\r\n")
            self.game_list.write(u"链接:"+addr+"\r\n")
            self.game_list.write(pwd+"\r\n")
            self.game_list.write("\r\n")
        time_string = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        time_spend = int(round(time.time() - spider.start_time))
        old_log = self.change_log.read()
        self.change_log.seek(0)
        self.change_log.write(u"%s 共爬取%d条, 耗时%d秒\r\n" % (time_string, len(self.data), time_spend))
        self.change_log.write(old_log)
        self.game_list_json.close()
        self.game_list.close()
        self.change_log.close()
