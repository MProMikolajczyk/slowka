#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''author: Marek Mikołajczyk
Moduł Translator.
Dostaje zwracane zapytanie
ze strony https://translate.google.com. '''

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





