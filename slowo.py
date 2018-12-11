'''author: Marek Mikołajczyk
Program do nauki slówek języka angielskiego.
Program pozyskuje slowa zestrony google tanslate po jego uruchomiwniu.
Dane przechowyne są w bazie danych MySQL'''

#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import random

words_eng = ['red','blue','green']
words_pol = ['czerwony','niebieski','zielony']
random_words_eng = list() #lista slowek wybranych losowo


random_words_eng.append(random.choice(words_eng)) #dodanie do zbioru losowego angielskiego slowka
index_random_words_eng = words_eng.index(random_words_eng[0]) #index losowego angielskiego slowka

'''zaminienia slowo wpowadzone na liste znakow'''
def list_letter():
    for letter in range(len(find_word)):
        yield find_word[letter]

'''#spr. dlugosc podannego slowa ze slowem ze zbioru. 
Wyrównuje ich dlugosc, wstawiaja lub usuwajac zanki ze slowa'''
def check_len_word():
    list_find_word=list(list_letter())
    if len(words_pol[index_random_words_eng]) == len(list_find_word):
        return list_find_word
    elif len(words_pol[index_random_words_eng]) > len(list_find_word):
        list_find_word += '-' * (len(words_pol[index_random_words_eng]) - len(list_find_word))
    elif len(words_pol[index_random_words_eng]) < len(list_find_word):
        while len(list_find_word) > len(words_pol[index_random_words_eng]):
            list_find_word.pop(len(list_find_word)-1)
    return list_find_word

'''spr znaki w spowie uzytym i wpisamyn. 
Tworzy liste ze znakami poprawnymi. 
Źle wpisane znaki zamienia na '-' '''
def check_word():
    list_char_word = list()
    for i in range(len(words_pol[index_random_words_eng])):
        if words_pol[index_random_words_eng][i] == check_len_word()[i]:
            list_char_word.append(check_len_word()[i])

        else:
            list_char_word.append('-')
    return list_char_word




find_word = input(random_words_eng[0] + ' = ' +'-'*len(words_pol[index_random_words_eng])) # poszukiwane slowo
print(check_len_word()) #wydruk słowa wpisanego po zmianie długowści
print("".join(check_word())) #wydruk słowa wpisanego po sprawdzeniu dligosci i podmienieniu niewłaściwych lister
print(random_words_eng[0] + ' = '+ find_word) #wydruk poszukiwanego slowa
print(random_words_eng[0] + ' = ' + words_pol[index_random_words_eng]) #słówko ang i znaczenie polskie