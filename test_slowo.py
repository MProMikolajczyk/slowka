
import unittest
import slowo

slowo.index_random_words=0

class Testslowo(unittest.TestCase):
    def test_list_letter(self):
        self.assertEqual(list(slowo.list_letter('big')),['b','i','g'])
        self.assertEqual(list(slowo.list_letter('data')), ['d', 'a', 't','a'])
        self.assertEqual(list(slowo.list_letter('')), [])

    def test_check_len_word(self):
        self.assertEqual(len(slowo.check_len_word(['zbc', 'dsaa', 'cfres'],'')),
                         len(['a-b','--ca','--abc'][slowo.index_random_words]))

    def test_check_word(self):
        self.assertEqual(len(slowo.check_word(['bbarwony','bbubieski','ccalony'],'')),
                         len(['--------','---------','-------'][slowo.index_random_words]))
        self.assertEqual(len(slowo.check_word(['red','blue','green'],'')),
                         len(['---','----','-----'][slowo.index_random_words]))
        self.assertEqual(len(slowo.check_word(['bbarwony', 'bbubieski', 'ccalony'], 'bb------')),
                         len(['bb------', '---------', '-------'][slowo.index_random_words]))

    def test_select_lang_version(self):
        self.assertEqual(slowo.select_lang_version(slowo.words_pol),slowo.random_words_eng)
        self.assertEqual(slowo.select_lang_version(slowo.words_eng),slowo.random_words_pol)

    def test_loop_looking_word(self):
        self.assertEqual(([['zarwony'],['iubieski'],['ialony']][slowo.index_random_words]),
                         [['zarwony'],['iubieski'],['ialony']][slowo.index_random_words])
        self.assertEqual(([['ad'], ['loe'], ['rean']][slowo.index_random_words]),
                         [['ad'], ['loe'], ['rean']][slowo.index_random_words])


if __name__ == '__main__':
    unittest.main()

