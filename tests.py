import bot
from bot import Mask
import unittest

class TestWordMask(unittest.TestCase):

    def test_case_1(self):
        mask_output = self.call_mask("abcda", "azzaz")
        correct_output = Mask.create_mask_list(list("CWWMW"))
        self.assertEqual(correct_output, mask_output)

    def call_mask(self, guess_word, correct_word):
        return bot.create_word_mask(list(guess_word), list(correct_word))

if __name__ == '__main__':
    unittest.main(verbosity=2)