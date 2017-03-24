import unittest
from crawler.tests.fake_response import fake_response_from_file
from crawler.spiders.autoesporte import AutoEsporteSpider


class AutoEsporteSpiderTest(unittest.TestCase):

    def setUp(self):
        self.spider = AutoEsporteSpider()

    def _get_results_from_file(self, file_name):
        response = fake_response_from_file(file_name)
        results = self.spider.parse(response)
        return list(results)

    def test_title(self):
        results = self._get_results_from_file('samples/single-item.xml')
        self.assertEqual("Título", results[0]['title'])

    def test_empty_title(self):
        results = self._get_results_from_file('samples/empty-item.xml')
        self.assertEqual("", results[0]['title'])

    def test_link(self):
        results = self._get_results_from_file('samples/single-item.xml')
        self.assertEqual("http://www.example.com/", results[0]['link'])

    def test_empty_link(self):
        results = self._get_results_from_file('samples/empty-item.xml')
        self.assertEqual("", results[0]['link'])

    def test_content(self):
        results = self._get_results_from_file('samples/single-item.xml')
        self.assertIs(list, type(results[0]['content']))

    def test_empty_content(self):
        results = self._get_results_from_file('samples/empty-item.xml')
        self.assertEqual([], results[0]['content'])


if __name__ == '__main__':
    unittest.main()
