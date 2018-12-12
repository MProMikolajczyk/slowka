
import unittest
import slowo

slowo.index_random_words=1 # stały wybór brak prawdopodobieństwa. Zawsze sprwdzaj dla 1 w zbiorze

class Testslowo(unittest.TestCase):

    def test_list_letter(self):
        self.assertEqual(list(slowo.list_letter('big')),['b','i','g'])
        self.assertEqual(list(slowo.list_letter('data')), ['d', 'a', 't','a'])
        self.assertEqual(list(slowo.list_letter('')), [])

    def test_check_len_word(self):
        self.assertEqual(len(slowo.check_len_word(['zbc', 'dsaa', 'cfres'])),
                         len(['a-b','--ca','--abc'][slowo.index_random_words]))

    def test_check_word(self):
        self.assertEqual(len(slowo.check_word(['czerwony','niebieski','zielony'])),
                         len(['-------','---------','-------'][slowo.index_random_words]))
        self.assertEqual(len(slowo.check_word(['red','blue','green'])),
                         len(['---','----','-----'][slowo.index_random_words]))


if __name__ == '__main__':
    unittest.main()

