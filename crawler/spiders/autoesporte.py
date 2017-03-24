from scrapy.spiders import XMLFeedSpider
from bs4 import BeautifulSoup


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
        item['content'] = self.get_content(node)
        return item

    def get_title(self, node):
        return node.xpath('title/text()').extract_first() or ""

    def get_link(self, node):
        return node.xpath('link/text()').extract_first() or ""

    def get_content(self, node):
        raw_html = node.xpath('description/node()').extract_first()
        if not raw_html:
            return []
        soup = BeautifulSoup(raw_html, 'lxml')
        results = []
        for child in soup.body.children:
            item = self.get_item(child)
            if item:
                results.append(item)
        return results

    def get_item(self, soup):
        if soup.name == 'p':
            return self.get_text(soup)
        elif soup.name == 'div' and soup.find('img'):
            return self.get_image(soup)
        elif soup.name == 'div' and soup.find('ul'):
            return self.get_links(soup)
        else:
            return None

    def get_text(self, soup):
        text = soup.text.strip()
        if text:
            return {"type": "text", "content": text}
        else:
            return None

    def get_image(self, soup):
        link = soup.img.get('src')
        return {"type": "image", "content": link}

    def get_links(self, soup):
        links = []
        for li in soup.ul.find_all('a'):
            link = li.get('href')
            links.append(link)
        return {"type": "links",
                "content": links}
