import unittest
from ergstapiclient import url_builder


class TestUrlBuilder(unittest.TestCase):
    def test_url(self):
        correcturl = "https://ergast.com/api/f1/current/next.json"
        result = url_builder()
        self.assertEqual(result, correcturl)


if __name__ == '__main__':
    unittest.main()
