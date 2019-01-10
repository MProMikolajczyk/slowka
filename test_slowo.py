#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''author: Marek Mikołajczyk
Testy jednoskowe do modułu slowo, data i translator'''

import unittest
import unittest.mock
import slowo
import data
import translator



class Testslowo(unittest.TestCase):

    slowo.words_eng = ['red', 'blue', 'green']
    slowo.words_pol = ['czerwony', 'niebieski', 'zielony']

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

class Testdata(unittest.TestCase):

    def test_create_data(self):
        data_base_list=list()
        data.bd.mycursor.execute('SHOW DATABASES;')
        for bd in data.bd.mycursor:
            data_base_list.append(bd)
        self.assertIn(('slowka',),data_base_list)

    def test_create_table(self):
        data_table_list=list()
        data.bd.mycursor.execute('SHOW TABLES;')
        for tables in data.bd.mycursor:
            data_table_list.append(tables)
        self.assertIn(('slowka',),data_table_list)

    def test_insert_into_table(self):
        data_words_list = list()
        data.bd.mycursor.execute('SELECT * FROM slowka')
        for words in data.bd.mycursor:
            data_words_list.append(words)
        self.assertIn('łóżko',data_words_list[0])
        self.assertIn('bed', data_words_list[0])

    def test_update_databases(self):
        data_words_list = list()
        data.bd.mycursor.execute('SELECT * FROM slowka')
        for words in data.bd.mycursor:
            data_words_list.append(words)
        self.assertIn('drzwi', data_words_list[3])
        self.assertIn('door', data_words_list[3])

    def test_show_all_values(self):
        self.assertIsNot(data.bd.show_all_values('slowka'),False)

    def test_show_words_in_dict(self):
        self.assertEqual(data.bd_main.show_words_in_dict('slowka','pol','ang')['bed'],'łóżko')

    def test_database_like(self):
        self.assertEqual(data.bd_letter.database_like('slowka', 'pol', 'ang', 'pol','k')['krzesło'],'chair')

    def test_show_tables(self):
        self.assertTrue(data.bd.show_tables())

class Testtranslator(unittest.TestCase):

    test_translate_eng = translator.ENG('red')
    test_translate_pol = translator.POL('róża')

    def test_translate_words_input(self):
        self.assertEqual(self.test_translate_eng.translate_words_input(),'red')
        self.assertEqual(self.test_translate_pol.translate_words_input(), 'róża')

    def test_translate_words_output(self):
        self.assertEqual(self.test_translate_eng.translate_words_output(),'czerwony')
        self.assertEqual(self.test_translate_pol.translate_words_output(), 'rose')

if __name__ == '__main__':
    unittest.main()

