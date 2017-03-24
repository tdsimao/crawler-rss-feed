from scrapy.spiders import XMLFeedSpider


class AutoEsporteSpider(XMLFeedSpider):
    name = 'autoesporte'
    allowed_domains = ['revistaautoesporte.globo.com']
    start_urls = ['http://revistaautoesporte.globo.com/rss/ultimas/feed.xml']
    iterator = 'iternodes'
    itertag = 'item'

    def parse_node(self, response, node):
        item = {}
        item['title'] = self.get_title(node)
        item['link'] = self.get_link(node)
        return item

    def get_title(self, node):
        return node.xpath('title/text()').extract_first() or ""

    def get_link(self, node):
        return node.xpath('link/text()').extract_first() or ""
