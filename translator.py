#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from googletrans import Translator

'''usyskanie dostępu do https://translate.google.com.
Wprowadznie słówek + tłumaczenie'''


class ENG:
    translate_lang_start = 'en' # Tłumaczenie języka
    translated_lang_end = 'pl' # Język tłumaczony

    def __init__(self,word):
        self.translator = Translator()
        self.word = word

        # Transloator
        self.translations = self.translator.translate(self.word,
                                                 src=self.translate_lang_start,
                                                 dest=self.translated_lang_end
                                                 )
    '''wprowadzone słowo'''
    def translate_words_input(self):
        return self.translations.origin

    '''wyjściowe słowo'''
    def translate_words_output(self):
        return self.translations.text

'''Podklasa do kolejnej wersji językowej'''
class POL(ENG):

    translate_lang_start = 'pl' # Tłumaczenie języka
    translated_lang_end = 'en' # Język tłumaczony


'''do wstawienia do końcowego modułu'''

translate_eng = ENG('door') # Wprowadzanie słówka ENG do tłumaczenia
translate_pol = POL('drzewo') # Wprowadzanie słówka POL do tłumaczenia


translate_eng.translate_words_input() #ENG słówko wprowadzone
translate_eng.translate_words_output() #POL słówko otrzymane

translate_pol.translate_words_input() #POL słówko wprowadzone
translate_pol.translate_words_output() #ENG słówko otrzymane

