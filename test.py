import unittest
from function import get_word, display

# class Get_word_Test(unittest.TestCase):
#     def test_word(self):
#         word = get_word()
#         self.assertEqual(word, word)


class Display_Test(unittest.TestCase):
    def test_display(self):
        word = get_word()
        letter = "фывапролд"
        dis = display(letter, word)
        self.assertEqual(dis, dis)

unittest.main()