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

    def test_link(self):
        response = fake_response_from_file('samples/single-item.xml')
        results = self.spider.parse(response)
        results = list(results)
        self.assertEqual(1, len(results))
        self.assertEqual("http://www.example.com/", results[0]['link'])

    def test_empty_link(self):
        response = fake_response_from_file('samples/empty-item.xml')
        results = self.spider.parse(response)
        results = list(results)
        self.assertEqual(1, len(results))
        self.assertEqual("", results[0]['link'])

    def test_content(self):
        response = fake_response_from_file('samples/single-item.xml')
        results = self.spider.parse(response)
        results = list(results)
        self.assertEqual(1, len(results))
        self.assertIs(list, type(results[0]['content']))

    def test_empty_content(self):
        response = fake_response_from_file('samples/empty-item.xml')
        results = self.spider.parse(response)
        results = list(results)
        self.assertEqual(1, len(results))
        self.assertEqual([], results[0]['content'])

if __name__ == '__main__':
    unittest.main()
