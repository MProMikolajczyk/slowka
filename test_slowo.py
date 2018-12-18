#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import unittest
import unittest.mock
import slowo

slowo.words_eng = ['red','blue','green']
slowo.words_pol = ['czerwony','niebieski','zielony']

class Testslowo(unittest.TestCase):
    def test_list_letter(self):
        self.assertEqual(list(slowo.list_letter('big')),['b','i','g'])
        self.assertEqual(list(slowo.list_letter('data')), ['d', 'a', 't','a'])
        self.assertEqual(list(slowo.list_letter('')), [])

    def test_check_len_word(self):
        self.assertEqual(len(slowo.check_len_word(['zbc', 'dsaa', 'cfres'],'',0)),
                         len(['a-b','--ca','--abc'][0]))

    def test_check_word(self):
        self.assertEqual(len(slowo.check_word(['bbarwony','bbubieski','ccalony'],'',0)),
                         len(['--------','---------','-------'][0]))
        self.assertEqual(len(slowo.check_word(['red','blue','green'],'',0)),
                         len(['---','----','-----'][0]))
        self.assertEqual(len(slowo.check_word(['bbarwony', 'bbubieski', 'ccalony'], 'bb------',0)),
                         len(['bb------', '---------', '-------'][0]))

    def test_select_lang_version(self):
        self.assertEqual(slowo.select_lang_version(slowo.words_pol,1),slowo.words_eng[1])
        self.assertEqual(slowo.select_lang_version(slowo.words_eng,1),slowo.words_pol[1])

    def test_loop_looking_word(self):
        self.assertEqual(slowo.loop_looking_word(slowo.words_eng,1),None) #spr tylko początek funkcji

    def test_loop_next_word(self):
        #self.assertEqual(slowo.loop_next_word(slowo.words_eng), None)
        pass

    def test_loop_quit_program(self):
        self.assertIs(slowo.loop_quit_program(slowo.words_eng,'y'),None)

    def test_choice_language_version(self):
        with unittest.mock.patch('builtins.input', return_value="pol"):
            self.assertEqual(slowo.choice_language_version(), slowo.words_pol)
        with unittest.mock.patch('builtins.input', return_value="ang"):
            self.assertEqual(slowo.choice_language_version(), slowo.words_eng)

if __name__ == '__main__':
    unittest.main()

