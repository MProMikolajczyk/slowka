'''author: Marek Mikołajczyk
Program do nauki slówek języka angielskiego.
Program pozyskuje slowa zestrony google tanslate po jego uruchomiwniu.
Dane przechowyne są w bazie danych MySQL'''

#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import random

words_eng = ['red','blue','green']
words_pol = ['czerwony','niebieski','zielony']
random_words_eng = list() #lista slowek  angielskich wybranych losowo
random_words_pol = list() #lista slowek poslich wybranych losowo

random_words_eng.append(random.choice(words_eng)) #dodanie do zbioru losowego angielskiego slowka
random_words_pol.append(random.choice(words_pol)) #dodanie do zbioru losowego posliego slowka

index_random_words = words_eng.index(random_words_eng[0]) #index losowego angielskiego slowka

'''zaminienia slowo wpowadzone na liste znakow'''
def list_letter(word):
    for letter in range(len(word)):
        yield word[letter]

'''#spr. dlugosc podannego slowa ze slowem ze zbioru. 
Wyrównuje ich dlugosc, wstawiaja lub usuwajac zanki ze slowa'''
def check_len_word(list_words):
    list_find_word=list(list_letter(find_word))
    if len(list_words[index_random_words]) == len(list_find_word):
        return list_find_word
    elif len(list_words[index_random_words]) > len(list_find_word):
        list_find_word += '-' * (len(list_words[index_random_words]) - len(list_find_word))
    elif len(list_words[index_random_words]) < len(list_find_word):
        while len(list_find_word) > len(list_words[index_random_words]):
            list_find_word.pop(len(list_find_word)-1)
    return list_find_word

'''spr znaki w spowie uzytym i wpisamyn. 
Tworzy liste ze znakami poprawnymi. 
Źle wpisane znaki zamienia na '-' '''
def check_word(lang_list_words):
    list_char_word = list()
    for i in range(len(lang_list_words[index_random_words])):
        if lang_list_words[index_random_words][i] == check_len_word(lang_list_words)[i]:
            list_char_word.append(check_len_word(lang_list_words)[i])

        else:
            list_char_word.append('-')
    return list_char_word






'''Wyduki funkkcji +mechanika'''
find_word = input(random_words_eng[0] + ' = ' +'-'*len(words_pol[index_random_words])) # wpisywane slowo
print("".join(check_word(words_pol))) #wydruk słowa wpisanego po sprawdzeniu dligosci i podmienieniu niewłaściwych lister
print('Podano : '+ find_word) #wydruk poszukiwanego slowa
print(random_words_eng[0] + ' = ' + words_pol[index_random_words]) #słówko ang i znaczenie polskie