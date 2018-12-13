'''author: Marek Mikołajczyk
Program do nauki slówek języka angielskiego.
Program pozyskuje slowa zestrony google tanslate po jego uruchomiwniu.
Dane przechowyne są w bazie danych MySQL'''

#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import random

words_eng = ['red','blue','green']
words_pol = ['czerwony','niebieski','zielony']

'''zaminienia slowo wpowadzone na liste znakow'''
def list_letter(word):
    for letter in range(len(word)):
        yield word[letter]

'''#spr. dlugosc podannego slowa ze slowem ze zbioru. 
Wyrównuje ich dlugosc, wstawiaja lub usuwajac zanki ze slowa'''
def check_len_word(list_words,find_word):
    list_find_word=list(list_letter(find_word))
    if len(list_words[index_random_words]) == len(list_find_word):
        return list_find_word
    elif len(list_words[index_random_words]) > len(list_find_word):
        list_find_word += '-' * (len(list_words[index_random_words]) - len(list_find_word))
    elif len(list_words[index_random_words]) < len(list_find_word):
        while len(list_find_word) > len(list_words[index_random_words]):
            list_find_word.pop(len(list_find_word)-1)
    return list_find_word

'''spr znaki w słowie uzytym i wpisamyn. 
Tworzy liste ze znakami poprawnymi. 
Źle wpisane znaki zamienia na '-' '''
def check_word(lang_list_words,find_word):
    list_char_word = list()
    for i in range(len(lang_list_words[index_random_words])):
        if lang_list_words[index_random_words][i] == check_len_word(lang_list_words,find_word)[i]:
            list_char_word.append(check_len_word(lang_list_words,find_word)[i])
        else:
            list_char_word.append('-')
    return list_char_word

'''Wybór opcji językowej'''
def select_lang_version(lang_version_list):
    if lang_version_list == words_pol: #spr warunku jezykowego (odpoweidz po polsku)
        question_lang_word = random_words_eng
        return question_lang_word
    elif lang_version_list == words_eng: #spr warunku jezykowego (odpoweidz po angielsku)
        question_lang_word = random_words_pol
        return question_lang_word

''' Pęta az to wpisania pożądanego słowa'''
def loop_looking_word(lang_version_list):
    select_lang_version(lang_version_list)
    find_word = ''
    while find_word != lang_version_list[index_random_words]:
        find_word = input(select_lang_version(lang_version_list)[0] + ' = ' + str(check_word(lang_version_list,find_word))) #szukane (wpisywane) slowo
        print('Podano : ' + find_word)  # wydruk poszukiwanego slowaP
        if find_word == lang_version_list[index_random_words]:
            print('dobrze')
            break
        elif find_word == 'n': #po wpisanu n pokazuje slowo szukane
            print(select_lang_version(lang_version_list)[0] + ' = ' + lang_version_list[index_random_words])  # słówko ang i znaczenie polskie
            break

while True:
    index_random_words=random.randint(0,len(words_eng)-1)
    random_words_eng = list() #lista slowek  angielskich wybranych losowo
    random_words_pol = list() #lista slowek poslich wybranych losowo
    random_words_eng.append(words_eng[index_random_words])  #dodanie do zbioru losowego angielskiego slowka
    random_words_pol.append(words_pol[index_random_words]) #dodanie do zbioru losowego posliego slowka
    loop_looking_word(words_eng) #opdowiedź po polsku, tytaj wybiera sie jezyk w jakim chce sie odpowiadać.