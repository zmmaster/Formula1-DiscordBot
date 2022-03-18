import unittest
from ergstapiclient import UrlBuilder


class TestUrlBuilder(unittest.TestCase):
    def test_url(self):
        correcturl = "https://ergast.com/api/f1/current/next.json"
        result = UrlBuilder.url_builder()
        self.assertEqual(result, correcturl)


if __name__ == '__main__':
    unittest.main()
