import unittest
from ergstapiclient import is_alpha, correct_format_helper


class TestIsAlpha(unittest.TestCase):
    def test_all_digit(self):
        endpoint_variable = 1980
        self.assertFalse(is_alpha(endpoint_variable))

    def test_all_alpha(self):
        endpoint_variable = "next"
        self.assertTrue(is_alpha(endpoint_variable))

    def test_alpha_digit(self):
        endpoint_variable = "19a0"
        self.assertFalse(is_alpha(endpoint_variable))

    def test_empty_string(self):
        endpoint_variable = ""
        self.assertFalse(is_alpha(endpoint_variable))

class TestFormatHelper(unittest.TestCase):
    def test_correct_format_helper_both_correct_keywords(self):
        season = "current"
        rnd = "next"
        self.assertTrue(correct_format_helper(season, rnd))

    def test_correct_format_helper_both_incorrect_keywords(self):
        season = "curren"
        rnd = "lats"
        self.assertFalse(correct_format_helper(season, rnd))

    def test_correct_format_helper_rndT_seasonF(self):
        season = "curent"
        rnd = "next"
        self.assertFalse(correct_format_helper(season, rnd))

    def test_correct_format_helper_rndF_seasonT(self):
        season = "current"
        rnd = "nxt"
        self.assertFalse(correct_format_helper(season, rnd))

    def test_correct_format_helper_both_correct_int(self):
        season = 2011
        rnd = 5
        self.assertTrue(correct_format_helper(season, rnd))

    def test_correct_format_helper_both_incorrect_int(self):
        season = 1948
        rnd = 26
        self.assertFalse(correct_format_helper(season, rnd))

    def test_correct_format_helper_rndT_seasonF_int(self):
        season = 2023
        rnd = 7
        self.assertFalse(correct_format_helper(season, rnd))

    def test_correct_format_helper_rndF_seasonT_int(self):
        season = 2000
        rnd = 0
        self.assertFalse(correct_format_helper(season, rnd))

    def test_correct_format_helper_both_correct_mixed(self):
        season = 2011
        rnd = "next"
        self.assertTrue(correct_format_helper(season, rnd))

    def test_correct_format_helper_both_incorrect_mixed(self):
        season = "Current"
        rnd = 62
        self.assertFalse(correct_format_helper(season, rnd))

    def test_correct_format_helper_rndT_seasonF_mixed(self):
        season = 2023
        rnd = "last"
        self.assertFalse(correct_format_helper(season, rnd))

    def test_correct_format_helper_rndF_seasonT_mixed(self):
        season = "current"
        rnd = 0
        self.assertFalse(correct_format_helper(season, rnd))

if __name__ == '__main__':
    unittest.main()
