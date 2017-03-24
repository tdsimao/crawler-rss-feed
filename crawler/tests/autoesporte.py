import unittest
from crawler.tests.fake_response import fake_response_from_file
from crawler.spiders.autoesporte import AutoEsporteSpider


class AutoEsporteSpiderTest(unittest.TestCase):

    def setUp(self):
        self.spider = AutoEsporteSpider()

    def test_title(self):
        response = fake_response_from_file('samples/single-item.xml')
        results = self.spider.parse(response)
        results = list(results)
        self.assertEqual(1, len(results))
        self.assertEqual("Título", results[0]['title'])

    def test_empty_title(self):
        response = fake_response_from_file('samples/empty-item.xml')
        results = self.spider.parse(response)
        results = list(results)
        self.assertEqual(1, len(results))
        self.assertEqual("", results[0]['title'])

if __name__ == '__main__':
    unittest.main()
