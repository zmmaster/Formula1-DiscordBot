import unittest
from ergstapiclient import earliest_year, season_checker, rnd_checker

class TestSeasonFormat(unittest.TestCase):
    def test_correct_earliest_year(self):
        year = 1950
        self.assertEqual(earliest_year, year)

    def test_correct_season_length(self):
        season = 2021
        self.assertTrue(season_checker(season, False))

    def test_wrong_season_lengthshort(self):
        season = 2
        self.assertFalse(season_checker(season, False))

    def test_wrong_season_lengthlong(self):
        season = 20222
        self.assertFalse(season_checker(season, False))

    def test_season_outofrange_low(self):
        season = 1930
        self.assertFalse(season_checker(season, False))

    def test_season_outofrange_high(self):
        season = 3330
        self.assertFalse(season_checker(season, False))

    def test_season_inrange(self):
        season = 1980
        self.assertTrue(season_checker(season, False))

    def test_season_correctkeyword(self):
        season = "current"
        self.assertTrue(season_checker(season))

    def test_season_wrongkeyword(self):
        season = "cuurent"
        self.assertFalse(season_checker(season))

    def test_season_emptystr(self):
        season = ""
        self.assertFalse(season_checker(season))


class TestRndFormat(unittest.TestCase):
    def test_correct_rnd_length_twodigits(self):
        rnd = 12
        self.assertTrue(rnd_checker(rnd, False))

    def test_correct_rnd_length_onedigits(self):
        rnd = 2
        self.assertTrue(rnd_checker(rnd, False))

    def test_wrong_rnd_lengthshort(self):
        rnd = ""
        self.assertFalse(rnd_checker(rnd))

    def test_wrong_rnd_lengthlong(self):
        rnd = 20214
        self.assertFalse(rnd_checker(rnd, False))

    def test_non_integer_rnd(self):
        rnd = "a"
        self.assertFalse(rnd_checker(rnd))

    def test_integer_rnd(self):
        rnd = 21
        self.assertTrue(rnd_checker(rnd, False))

    def test_rnd_outofrange_low(self):
        rnd = 0
        self.assertFalse(rnd_checker(rnd, False))

    def test_rnd_outofrange_high(self):
        rnd = 25
        self.assertFalse(rnd_checker(rnd, False))

    def test_rnd_inrange(self):
        rnd = 6
        self.assertTrue(rnd_checker(rnd, False))

    def test_rnd_correctkeyword(self):
        rnd = "last"
        self.assertTrue(rnd_checker(rnd))

    def test_rnd_wrongkeyword(self):
        rnd = "netx"
        self.assertFalse(rnd_checker(rnd))

if __name__ == '__main__':
    unittest.main()
