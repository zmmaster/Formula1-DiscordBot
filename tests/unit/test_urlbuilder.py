import unittest

from ergstapiclient import url_builder


class TestUrlBuilder(unittest.TestCase):
    def test_url(self):
        correcturl = "https://ergast.com/api/f1/current/next.json"
        result = url_builder()
        self.assertEqual(result, correcturl)


class TestSeasonFormat(unittest.TestCase):
    def test_correct_season_length(self):
        season = "2021"
        self.assertTrue()

    def test_wrong_season_lengthshort(self):
        season = "2"
        self.assertFalse()

    def test_wrong_season_lengthlong(self):
        season = "20214"
        self.assertFalse()

    def test_non_integer_season(self):
        season = "2a021"
        self.assertFalse()

    def test_integer_season(self):
        season = "2021"
        self.assertTrue()

    def test_season_outofrange_low(self):
        season = "1930"
        self.assertFalse()

    def test_season_outofrange_high(self):
        season = "3330"
        self.assertFalse()

    def test_season_inrange(self):
        season = "1980"
        self.assertTrue()

    def test_season_correctkeyword(self):
        season = "current"
        self.assertTrue()

    def test_season_wrongkeyword(self):
        season = "cuurent"
        self.assertFalse()


class TestRndFormat(unittest.TestCase):
    def test_correct_rnd_length_twodigits(self):
        rnd = "12"
        self.assertTrue()

    def test_correct_rnd_length_onedigits(self):
        rnd = "2"
        self.assertTrue()

    def test_wrong_rnd_lengthshort(self):
        rnd = ""
        self.assertFalse()

    def test_wrong_rnd_lengthlong(self):
        rnd = "20214"
        self.assertFalse()

    def test_non_integer_rnd(self):
        rnd = "a"
        self.assertFalse()

    def test_integer_rnd(self):
        rnd = "21"
        self.assertTrue()

    def test_rnd_outofrange_low(self):
        rnd = "0"
        self.assertFalse()

    def test_rnd_outofrange_high(self):
        rnd = "25"
        self.assertFalse()

    def test_rnd_inrange(self):
        rnd = "6"
        self.assertTrue()

    def test_rnd_correctkeyword(self):
        rnd = "last"
        self.assertTrue()

    def test_rnd_wrongkeyword(self):
        rnd = "netx"
        self.assertTrue()


class TestFormatHelper(unittest.TestCase):
    def test_format_helper_both_correct(self):
        pass

    def test_format_helper_rndT_seasonF(self):
        pass

    def test_format_helper_rndF_seasonT(self):
        pass


if __name__ == '__main__':
    unittest.main()
