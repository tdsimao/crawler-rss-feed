# crawler-rss-feed
Crawler for a rss feed.


# How to install

```
	$ pip install -r requirements.txt
```

# Usage
```
	$ scrapy crawl autoesporte

2017-03-24 10:32:14 [scrapy.core.scraper] DEBUG: Scraped from <200 http://revistaautoesporte.globo.com/rss/ultimas/feed.xml>
{'title': 'Recall: BMW convoca X1 por falha no painel que afeta o funcionamento do airbag'}
2017-03-24 10:32:14 [scrapy.core.scraper] DEBUG: Scraped from <200 http://revistaautoesporte.globo.com/rss/ultimas/feed.xml>
{'title': 'STOCK CAR - PINTURA RADICAL DÁ O TOM NA APRESENTAÇÃO DO PILOTO LUCAS FORESTI'}
```



# Testing

Test crawler
```
	$ python -m crawler.tests
```

Verbose test
```
	$ python -m unittest -v crawler.tests
```