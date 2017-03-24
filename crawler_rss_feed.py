import json
import argparse
from urllib.request import urlopen
from scrapy.http import Response, Request
from crawler.spiders.autoesporte import AutoEsporteSpider


def get_feed():
    spider = AutoEsporteSpider()
    url = spider.start_urls[0]
    body = urlopen(url).read()
    response = Response(url=url, request=Request(url=url), body=body)
    response.encoding = 'utf-8'
    items = [{'item': item} for item in spider.parse(response)]
    return {'feed': items}


parser = argparse.ArgumentParser()
parser.add_argument("-o", "--output", help="Output file",
                    type=argparse.FileType('w'))


if __name__ == '__main__':
    args = parser.parse_args()
    feed = get_feed()
    if args.output:
        json.dump(feed, args.output)
    else:
        print(feed)
