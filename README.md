# Galgame Spider
#### 不知道这是拿来干啥的（逃
---


环境配置：

- Scrapy:
``` bash
pip install Scrapy
```

- lxml: 大多数发行版Linux自带lxml，如果缺失请查看<http://lxml.de/installation.html>

- OpenSSL 除了Windows之外的系统基本已经提供


启动：
在galgame_spider目录下：
``` bash
scrapy crawl MGS
```


JSON存在 `/game_list.json`中

能方便看懂的结果在 `/game_list`中

~~由于Scrapy的Request是异步的所以顺序全乱了(~~

