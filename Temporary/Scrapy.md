## Spider
spider/stocktwits.py
```python=
from ..items import StockItem

import scrapy
import json

BASE_URL = 'https://api.stocktwits.com/api/2/streams/symbol/TSLA.json?max='


class TSLASpider(scrapy.Spider):
    name = "TSLA"

    def __init__(self):
        self.count = 0
        self.data_limit = 100

    def start_requests(self):
        urls = [
            'https://api.stocktwits.com/api/2/streams/symbol/TSLA.json'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
		# for data clean init
        items = StockItem()

        data = json.loads(response.text)
        messages = data['messages']
        self.messages += messages

        for message in messages:
            sentiment = message['entities']['sentiment']
            if sentiment:
                sentiment = sentiment['basic']

            items['message_id'] = message['id']
            items['body'] = message['body']
            items['sentiment'] = message['entities']['sentiment'] 
            items['created_at'] = message['created_at']

            yield items
        
        self.count += len(messages)

        if self.count < self.data_limit:
            new_max = messages[-1]['id']
            new_url = BASE_URL + str(new_max)
			# crawl new url
            yield scrapy.Request(url=new_url, callback=self.parse)

```

```shell
scrapy crawl TSLA
```

## Item pipeline
items.py
```python
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StockItem(scrapy.Item):
    # define the fields for your item
    message_id = scrapy.Field() 
    body = scrapy.Field()
    sentiment = scrapy.Field()
    created_at = scrapy.Field()
```

pipelines.py
```python
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class StockPipeline:

    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['sentiment']:
            item['sentiment'] = item['sentiment']['basic']

		# clean duplicate item
        adapter = ItemAdapter(item)
        if adapter['message_id'] in self.ids_seen:
            raise DropItem(f"Duplicate item found: {item!r}")
        else:
            self.ids_seen.add(adapter['message_id'])
            return item
```

```shell
scrapy crawl TSLA -o TSLA.json
scrapy crawl TSLA -o TSLA.CSV
```