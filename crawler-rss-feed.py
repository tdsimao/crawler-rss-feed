import json
import argparse
import pprint
from urllib.request import urlopen
from scrapy.crawler import CrawlerProcess
from scrapy.http import Response, Request
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
from crawler.spiders.autoesporte import AutoEsporteSpider

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", help="Output file",
                        type=argparse.FileType('w'))
    args = parser.parse_args()

    spider = AutoEsporteSpider()
    url = spider.start_urls[0]
    body = urlopen(url).read()
    response = Response(url=url, request=Request(url=url), body=body)
    response.encoding = 'utf-8'
    items = [{'item': item} for item in spider.parse(response)]
    feed = {'feed': items}

    if args.output:
        json.dump(feed, args.output)
    else:
        pprint.pprint(feed)
