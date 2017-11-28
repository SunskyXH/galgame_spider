# -*- coding: utf-8 -*-
import codecs
import json

class GalgameSpiderPipeline(object):
    def __init__(self):
        self.file = codecs.open('game_list.json','w+',encoding='utf-8')
        self.file2 = codecs.open('game_list','w+',encoding='utf-8')
        self.data = []
    def process_item(self, item, spider):
        if item != [] and item['addr'] != []:
            item['addr'] = item['addr'][0].lstrip("/").rstrip("'")
            item['title'] = item['title'][0]
            item['pwd'] = item['pwd'][0].rstrip(u"：") + ":" + item['pwd'][1]
            item['date'] = item['date'].lstrip()
            line = json.dumps(dict(item), ensure_ascii=False) + "\r\n"
            self.data.append(item)
            self.file.write(line)
        return '[INFO]FINISH'
    def close_spider(self, spider):
        for i in self.data:
            addr = i['addr']
            title = i['title']
            pwd = i['pwd']
            date = i['date']
            self.file2.write(u"标题:"+title+"\r\n")
            self.file2.write(u"日期:" + date + "\r\n")
            self.file2.write(u"链接:"+addr+"\r\n")
            self.file2.write(pwd+"\r\n")
            self.file2.write("\r\n")
        self.file.close()
        self.file2.close()
