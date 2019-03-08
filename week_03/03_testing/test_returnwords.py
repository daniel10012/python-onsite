import unittest
from returnwords import return_word


class TestReturnWords(unittest.TestCase):

    def test_returns_false_if_empty_string_as_char(self):
        self.assertIs(return_word("abcde",""), False)

    def test_returns_false_if_empty_string_as_word(self):
        self.assertIs(return_word("","e"), False)

    def test_returns_false_if_word_is_not_string(self):
        for i in range(10):
            self.assertIs(return_word(i,"e"), False)

    def test_returns_false_if_char_is_not_string(self):
        self.assertIs(return_word("rsg",3), False)

    def test_returns_false_if_word_is_blank_spaces(self):
        self.assertIs(return_word("  "," "), False)


if __name__ == '__main__':
    unittest.main()

