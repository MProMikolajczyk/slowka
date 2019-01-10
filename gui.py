#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''author: Marek Mikołajczyk
Moduł do wizualizacji graficznej - okienkowej
pozostałych modułów '''

import sys
from PyQt5 import QtWidgets, QtGui, QtCore
import data
import translator

'''Wybór tabeli z bazy naych po wprowadzniu'''
class WinUser(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.center() #pozycjonowanie zawsze na środku ekranu
        self.properties()

        # Tytuł okienka
        self.setWindowTitle('Translator_program')

        #shortcut quit
        self.shortcut_quit = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+Q"), self)
        self.shortcut_quit.activated.connect(self.b_quit)

    '''zawartośc okienka '''
    def properties(self):

        #Wielkość okna
        self.resize(300, 200)

        # lable button
        self.btw_connect = QtWidgets.QPushButton('Połącz')
        self.btw_quit = QtWidgets.QPushButton('Zakończ')
        self.btw_create_base = QtWidgets.QPushButton('Utwórz')

        #edit lable Edit line
        self.lable_base_text = QtWidgets.QLineEdit()
        self.lable_base_text.setAlignment(QtCore.Qt.AlignCenter)

        #lable text
        text_bold = QtGui.QFont()
        text_bold.setBold(True)
        self.lable_text_welcome = QtWidgets.QLabel('Podaj zbiór:')
        self.lable_text_welcome.setAlignment(QtCore.Qt.AlignCenter)
        self.lable_text_welcome.setFont(text_bold)

        self.lable_text_action = QtWidgets.QLabel()
        self.lable_text_action.setAlignment(QtCore.Qt.AlignCenter)

        '''horizoltal box z layoutu'''
        h_box_welcome = QtWidgets.QHBoxLayout()
        h_box_welcome.addStretch()
        h_box_welcome.addWidget(self.lable_text_welcome)
        h_box_welcome.setAlignment(QtCore.Qt.AlignTop)
        h_box_welcome.addStretch()

        h_box_action = QtWidgets.QHBoxLayout()
        h_box_action.addStretch()
        h_box_action.addWidget(self.lable_text_action)
        h_box_action.setAlignment(QtCore.Qt.AlignBottom)
        h_box_action.addStretch()


        '''vboxy'''
        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(h_box_welcome) #text lable 'Wpisz imię'
        v_box.addStretch()
        v_box.addWidget(self.lable_base_text)
        v_box.addStretch()
        v_box.addWidget(self.btw_connect)
        v_box.addWidget(self.btw_create_base)
        v_box.addWidget(self.btw_quit)
        v_box.addLayout(h_box_action)

        '''okreslenie wartwy wyśiwtlanej'''
        self.setLayout((v_box))


        '''łaczenie przycisków'''
        self.btw_quit.clicked.connect(self.b_quit)
        self.btw_create_base.clicked.connect(self.b_cb)
        self.btw_connect.clicked.connect(self.b_connect)

        '''errors'''
        self.error = QtWidgets.QErrorMessage()

        '''shortcut'''
        self.shortcut_connect = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Return), self)
        self.shortcut_connect.activated.connect(self.b_connect)

        self.show()

    '''pozycjonowanie okienka '''
    def center(self):
        geometry = self.frameGeometry()
        center_point = QtWidgets.QDesktopWidget().availableGeometry().center()
        geometry.moveCenter(center_point)
        self.move(geometry.topLeft())

    '''metody dla przycisków '''
    #quit
    def b_quit(self):
        self.close()

    #create dattabases
    def b_cb(self):
        #baza pusta
        if self.lable_base_text.text().lower() == '':
            self.error.showMessage('Nie może być pustego zbióru ')

        # baza istniejąca
        elif self.lable_base_text.text().lower() in data.bd.show_tables():
            self.lable_text_action.setText('Baza już istnieje')

        # warunek długości nazwy bazy
        elif len(self.lable_base_text.text().lower()) < 5:
            self.lable_text_action.setText('Baza musi zawierać conajmniej 5 znaków')

        # baza nieistniejąca
        else:
            data.bd.create_table(self.lable_base_text.text().lower(), 'id', 'pol VARCHAR(255) COLLATE utf8_unicode_ci NOT NULL,',
                                 'ang VARCHAR(255) COLLATE utf8_unicode_ci NOT NULL,')
            self.lable_text_action.setText('Utorzono zbiór')

    #przejście do następnego okna
    def b_connect(self):
        #pustu zbiór
        if self.lable_base_text.text().lower() == '':
            self.error.showMessage('Wybierz zbiór')

        #braz utorzonej bazy
        elif self.lable_base_text.text().lower() not in data.bd.show_tables():
            self.error.showMessage('Utwórz Bazę')

        #przejście do następnego okna
        else:
            self.close()
            self.main = WinMain()
            self.main.show()

    #wartość aktywnego zbioru - nazwa zbioru / użytkownika
    def activ_set(self):
        return self.lable_base_text.text().lower()

class WinMain(WinUser):
    '''okno nr 2 tłumacz'''
    def properties(self):

        #Wielkość okna
        self.resize(400, 700)

        # lable button
        self.btw_translate_to_pol = QtWidgets.QPushButton('Tłumacz na język Polski')
        self.btw_translate_to_eng = QtWidgets.QPushButton('Tłumacz na język Angielski')
        self.btw_check_all_words = QtWidgets.QPushButton('Cały zbiór')
        self.btw_check_word_char = QtWidgets.QPushButton('Słówka na wybraną litere')
        self.btw_update_word = QtWidgets.QPushButton('Popraw słowo w bazie')
        self.btw_pint_all_words = QtWidgets.QPushButton('Wyświetl zbiór słówek')
        self.btw_quit = QtWidgets.QPushButton('Zakończ')

        # edit lable Edit line
        self.lable_text_to_translate_pol = QtWidgets.QLineEdit()
        self.lable_text_to_translate_pol.setAlignment(QtCore.Qt.AlignCenter)

        self.lable_text_to_translate_eng = QtWidgets.QLineEdit()
        self.lable_text_to_translate_eng.setAlignment(QtCore.Qt.AlignCenter)

        self.lable_id =QtWidgets.QLineEdit() #ID
        self.lable_id.setAlignment(QtCore.Qt.AlignCenter)

        self.lable_pol_word = QtWidgets.QLineEdit()  #POL
        self.lable_pol_word.setAlignment(QtCore.Qt.AlignCenter)

        self.lable_eng_word = QtWidgets.QLineEdit() #ANG"
        self.lable_eng_word.setAlignment(QtCore.Qt.AlignCenter)

        self.lable_char = QtWidgets.QLineEdit() # literka do zbioru zaczynającego się na litere
        self.lable_char.setAlignment((QtCore.Qt.AlignCenter))

        # text attribute
        text_bold = QtGui.QFont()
        text_bold.setBold(True)

        # lable text
        self.visible_text_translate_pol = QtWidgets.QLabel('Przetłumacz na język Polski:')
        self.visible_text_translate_pol.setAlignment(QtCore.Qt.AlignCenter)
        self.visible_text_translate_pol.setFont(text_bold)

        self.visible_text_translate_eng = QtWidgets.QLabel('Przetłumacz na język Angielski:')
        self.visible_text_translate_eng.setAlignment(QtCore.Qt.AlignCenter)
        self.visible_text_translate_eng.setFont(text_bold)

        self.visible_text_check_self = QtWidgets.QLabel('Sprawdź co pamiętasz:')
        self.visible_text_check_self.setAlignment(QtCore.Qt.AlignCenter)
        self.visible_text_check_self.setFont(text_bold)

        self.visible_text_base_opction = QtWidgets.QLabel('Operacje na zbiorze:')
        self.visible_text_base_opction.setAlignment(QtCore.Qt.AlignCenter)
        self.visible_text_base_opction.setFont(text_bold)

        #text to text_lable_mistake
        self.text_id = QtWidgets.QLabel('#ID')
        self.text_id.setAlignment(QtCore.Qt.AlignCenter)

        self.text_pol = QtWidgets.QLabel('#POL')
        self.text_pol.setAlignment(QtCore.Qt.AlignCenter)

        self.text_eng = QtWidgets.QLabel('#ANG')
        self.text_eng.setAlignment(QtCore.Qt.AlignCenter)


        # lable text action
        self.lable_text_action = QtWidgets.QLabel() #text po zrobieniu jakieś akcji na końcu
        self.lable_text_action.setAlignment(QtCore.Qt.AlignCenter)

        self.lable_text_action_trans_pol = QtWidgets.QLabel('Oznacza: ') #output translated text eng
        self.lable_text_action.setAlignment(QtCore.Qt.AlignCenter)
        self.lable_text_action_trans_pol.setFont(text_bold)

        self.lable_text_action_trans_eng = QtWidgets.QLabel('Oznacza: ') #output translated text eng
        self.lable_text_action_trans_eng.setAlignment(QtCore.Qt.AlignCenter)
        self.lable_text_action_trans_eng.setFont(text_bold)

        #checkbox
        self.checkbox_pol = QtWidgets.QCheckBox('Pol')
        self.checkbox_eng = QtWidgets.QCheckBox('Eng')

        '''horizoltal box z layoutu'''
        #text Tłumacz na język Polski
        h_box_text_translate_pol = QtWidgets.QHBoxLayout()
        h_box_text_translate_pol.addStretch()
        h_box_text_translate_pol.addWidget(self.visible_text_translate_pol)
        h_box_text_translate_pol.setAlignment(QtCore.Qt.AlignTop)
        h_box_text_translate_pol.addStretch()

        #text Sprawdź sie
        h_box_text_check_self = QtWidgets.QHBoxLayout()
        h_box_text_check_self.addStretch()
        h_box_text_check_self.addWidget(self.visible_text_check_self)
        h_box_text_check_self.setAlignment(QtCore.Qt.AlignTop)
        h_box_text_check_self.addStretch()

        #text Operacje na zbiorze
        h_box_text_base_opction = QtWidgets.QHBoxLayout()
        h_box_text_base_opction.addStretch()
        h_box_text_base_opction.addWidget(self.visible_text_base_opction)
        h_box_text_base_opction.addStretch()

        # text Tłumacz na język Angieslki
        h_box_text_translate_eng = QtWidgets.QHBoxLayout()
        h_box_text_translate_eng.addStretch()
        h_box_text_translate_eng.addWidget(self.visible_text_translate_eng)
        h_box_text_translate_eng.setAlignment(QtCore.Qt.AlignTop)
        h_box_text_translate_eng.addStretch()

        # text_action wyświetlany po akcji na końcu okienka
        h_box_action = QtWidgets.QHBoxLayout()
        h_box_action.addWidget(self.lable_text_action)
        h_box_action.setAlignment(QtCore.Qt.AlignBottom)

        # text_action tłumaczenie pol na eng
        h_box_action_trans_pol = QtWidgets.QHBoxLayout()
        h_box_action_trans_pol.addStretch()
        h_box_action_trans_pol.addWidget(self.lable_text_action_trans_pol)
        h_box_action_trans_pol.setAlignment(QtCore.Qt.AlignCenter)
        h_box_action_trans_pol.addStretch()

        # text_action tłumaczenie eng na pol
        h_box_action_trans_eng = QtWidgets.QHBoxLayout()
        h_box_action_trans_eng.addStretch()
        h_box_action_trans_eng.addWidget(self.lable_text_action_trans_eng)
        h_box_action_trans_eng.setAlignment(QtCore.Qt.AlignCenter)
        h_box_action_trans_eng.addStretch()

        # text_edit poprawienie błędów
        h_box_lable_text_mistake = QtWidgets.QHBoxLayout()
        h_box_lable_text_mistake.addWidget(self.text_id,1)
        h_box_lable_text_mistake.addWidget(self.text_pol,3)
        h_box_lable_text_mistake.addWidget(self.text_eng,3)

        h_box_lable_mistake = QtWidgets.QHBoxLayout()
        h_box_lable_mistake.addWidget(self.lable_id,1)
        h_box_lable_mistake.addWidget(self.lable_pol_word,3)
        h_box_lable_mistake.addWidget(self.lable_eng_word,3)

        # text_edit literka
        h_box_lable_char = QtWidgets.QHBoxLayout()
        h_box_lable_char.addWidget(self.btw_check_word_char,9)
        h_box_lable_char.addWidget(self.lable_char,1)

        #checkbox
        h_box_lable_checkbox =QtWidgets.QHBoxLayout()
        h_box_lable_checkbox.addStretch()
        h_box_lable_checkbox.addWidget(self.checkbox_pol)
        h_box_lable_checkbox.addStretch()
        h_box_lable_checkbox.addWidget(self.checkbox_eng)
        h_box_lable_checkbox.addStretch()
        h_box_lable_checkbox.setAlignment(QtCore.Qt.AlignCenter)

        '''vboxy'''
        v_box = QtWidgets.QVBoxLayout()

        # text translate word pol to eng'
        v_box.addStretch()
        v_box.addLayout(h_box_text_translate_pol)
        v_box.addStretch()

        # text edit line to translate pol to eng
        v_box.addWidget(self.lable_text_to_translate_pol)

        # button to translate pol to eng
        v_box.addWidget(self.btw_translate_to_pol)

        # action_text translate word to eng
        v_box.addStretch()
        v_box.addLayout(h_box_action_trans_pol)

        # text translate word eng to pol'
        v_box.addStretch()
        v_box.addLayout(h_box_text_translate_eng)
        v_box.addStretch()

        # text edit line to translate eng to pol
        v_box.addWidget(self.lable_text_to_translate_eng)

        # button to translate eng to pol
        v_box.addWidget(self.btw_translate_to_eng)

        # action_text translate word to pol
        v_box.addStretch()
        v_box.addLayout(h_box_action_trans_eng)

        # text 'Sprawdź się'
        v_box.addStretch()
        v_box.addLayout(h_box_text_check_self)
        v_box.addStretch()

        # button check_all_words
        v_box.addWidget(self.btw_check_all_words)

        # button check_char and edit_text_char
        v_box.addLayout(h_box_lable_char)

        #checkbox choice language version
        v_box.addLayout(h_box_lable_checkbox)

        #text 'Operacje na zabiorze'
        v_box.addStretch()
        v_box.addLayout(h_box_text_base_opction)
        v_box.addStretch()

        # button update_set and print all words in set
        v_box.addStretch()
        v_box.addWidget(self.btw_update_word)
        v_box.addLayout(h_box_lable_text_mistake)
        v_box.addLayout(h_box_lable_mistake)
        v_box.addStretch()
        v_box.addWidget(self.btw_pint_all_words)
        v_box.addStretch()

        # button quit program
        v_box.addWidget(self.btw_quit,2)

        # text action bottom
        v_box.addStretch()
        v_box.addLayout(h_box_action)
        v_box.addStretch()

        '''okreslenie wartwy wyśiwtlanej'''
        self.setLayout((v_box))

        '''dodoatkowe okienka'''
        self.window_slowo = QtWidgets.QMainWindow()
        self.text_edit_slowo = QtWidgets.QPlainTextEdit()

        '''łaczenie przycisków'''
        self.btw_quit.clicked.connect(self.b_quit)
        self.btw_translate_to_pol.clicked.connect(self.b_tran_to_pol)
        self.btw_translate_to_eng.clicked.connect(self.b_tran_to_eng)
        self.btw_check_all_words.clicked.connect(self.b_check_all_words)
        self.btw_check_word_char.clicked.connect(self.b_check_word_char)
        self.btw_update_word.clicked.connect(self.b_update_word)
        self.btw_pint_all_words.clicked.connect(self.b_print_all_words)

        '''errors'''
        self.error_text = QtWidgets.QErrorMessage()

        self.show()

    #metoda do czyszczenia text_edit
    def clear(self):
        self.clear()

    """checkboxes"""
    def chx_pol_eng(self):
        # jeśli pol jest zaznaczony
        if self.checkbox_pol.isChecked():
            return 'pol'

        # jeśli eng jest zaznaczony
        elif self.checkbox_eng.isChecked():
            return 'ang'

    '''metody dla przycisków '''
    # quit
    def b_quit(self):
        self.close()

    #translate to pol
    def b_tran_to_pol(self):
        # oczyszczenie actywnego pola textowego u dołu ekrany w przypadku ponowego wyboru słówka
        self.lable_text_action.clear()

        # kolor textu po kliknieciu
        self.lable_text_action_trans_pol.setStyleSheet("color: red;")

        # gdy zbiór jest pusty to wyświetl error
        if self.lable_text_to_translate_pol.text() == '':
            self.error_text.showMessage('Zbiór nie może być pusty')

        # gdy są duplikaty w zbiorze wyświetl w activ_text na dole komunikat
        elif (translator.ENG(self.lable_text_to_translate_pol.text().upper()).translate_words_output(),
              # POL słówko wprowadzone, # ENG słówko otrzymane
              translator.ENG(self.lable_text_to_translate_pol.text().upper()).translate_words_input()) \
             in data.bd.show_pol_ang_values(user.activ_set(), 'pol', 'ang'):  # aktywny zbiór słówek

            # dodanie textu do pola text_activ, wyniku tłumaczenia
            self.lable_text_action_trans_pol.setText(
                translator.ENG(
                    self.lable_text_to_translate_pol.text().upper()).translate_words_input() +  # POL słówko wprowadzone
                str(' = ') +
                translator.ENG(
                    self.lable_text_to_translate_pol.text().upper()).translate_words_output())  # ENG słówko otrzymane

            # wyświetlenie komunikatu na dole okienka
            self.lable_text_action.setText('Już kiedyś sprawdzałaś/eś')

        #gdy słówko ze zbioru pol jest takie samo jak w ang
        elif translator.ENG(self.lable_text_to_translate_pol.text().upper()).translate_words_output() == \
                translator.ENG(self.lable_text_to_translate_pol.text().upper()).translate_words_input():

            #wyświetl error nie ma takiego słowa
            self.error_text.showMessage('Nie ma takiego słowa')


        # gdy nie ma duplikatów i zbiór nie jest pusty
        else:

            # dodanie textu do pola text_activ, wyniku tłumaczenia
            self.lable_text_action_trans_pol.setText(
                translator.ENG(
                    self.lable_text_to_translate_pol.text().upper()).translate_words_input() +  # ENG słówko wprowadzone
                str(' = ') +
                translator.ENG(
                    self.lable_text_to_translate_pol.text().upper()).translate_words_output())  # POL słówko otrzymane

            # dodanie słówek do zbioru
            data.bd.insert_into_table(user.activ_set(),
                                      translator.ENG(
                                          self.lable_text_to_translate_pol.text().upper()).translate_words_output(),  # POL słówko otrzymane
                                      translator.ENG(
                                          self.lable_text_to_translate_pol.text().upper()).translate_words_input()  # ENG słówko wprowadzone
                                      )

            # aktualizacja zbioru
            self.b_print_all_words()

    #translate to eng
    def b_tran_to_eng(self):
        #oczyszczenie actywnego pola textowego u dołu ekrany w przypadku ponowego wyboru słówka
        self.lable_text_action.clear()

        # kolor textu po kliknieciu
        self.lable_text_action_trans_eng.setStyleSheet("color: red;")

        #gdy zbiór jest pusty to wyświetl error
        if self.lable_text_to_translate_eng.text() == '':
            self.error_text.showMessage('Zbiór nie może być pusty')

        #gdy są duplikaty w zbiorze wyświetl w activ_text na dole komunikat
        elif (translator.POL(self.lable_text_to_translate_eng.text().upper()).translate_words_input(),  # POL słówko wprowadzone, # ENG słówko otrzymane
              translator.POL(self.lable_text_to_translate_eng.text().upper()).translate_words_output()) \
                in data.bd.show_pol_ang_values(user.activ_set(),'pol','ang'): #aktywny zbiór słówek

            # dodanie textu do pola text_activ, wyniku tłumaczenia
            self.lable_text_action_trans_eng.setText(
                translator.POL(
                    self.lable_text_to_translate_eng.text().upper()).translate_words_input() +  # POL słówko wprowadzone
                str(' = ') +
                translator.POL(
                    self.lable_text_to_translate_eng.text().upper()).translate_words_output())  # ENG słówko otrzymane

            #wyświetlenie komunikatu na dole okienka
            self.lable_text_action.setText('Już kiedyś sprawdzałaś/eś')

        # gdy słówko ze zbioru pol jest takie samo jak w ang
        elif translator.POL(self.lable_text_to_translate_eng.text().upper()).translate_words_output() == \
                translator.POL(self.lable_text_to_translate_eng.text().upper()).translate_words_input():

            # wyświetl error nie ma takiego słowa
            self.error_text.showMessage('Nie ma takiego słowa')

        # gdy nie ma duplikatów i zbiór nie jest pusty
        else:

            # dodanie textu do pola text_activ, wyniku tłumaczenia
            self.lable_text_action_trans_eng.setText(
                translator.POL(
                    self.lable_text_to_translate_eng.text().upper()).translate_words_input() +  # POL słówko wprowadzone
                str(' = ') +
                translator.POL(
                    self.lable_text_to_translate_eng.text().upper()).translate_words_output())  # ENG słówko otrzymane

            # dodanie słówek do zbioru
            data.bd.insert_into_table(user.activ_set(),
                                      translator.POL(
                                          self.lable_text_to_translate_eng.text().upper()).translate_words_input(),
                                      translator.POL(
                                          self.lable_text_to_translate_eng.text().upper()).translate_words_output())

            # aktualizacja zbioru
            self.b_print_all_words()

    #check all set
    def b_check_all_words(self):

        '''skopolowany moduł slowo z dobranym zbiorem -całym '''

        import random

        dictionary_words = data.bd_main.show_words_in_dict(user.activ_set(), 'pol', 'ang')

        words_eng = [word for word in dictionary_words]
        words_pol = [dictionary_words[keys] for keys in dictionary_words]

        '''zaminienia slowo wpowadzone na liste znakow'''

        def list_letter(word):
            for letter in range(len(word)):
                yield word[letter]

        '''#spr. dlugosc podannego slowa ze slowem ze zbioru. 
        Wyrównuje ich dlugosc, wstawiaja lub usuwajac zanki ze slowa'''

        def check_len_word(list_words, find_word, index_random_words):
            list_find_word = list(list_letter(find_word))
            if len(list_words[index_random_words]) == len(list_find_word):
                return list_find_word
            elif len(list_words[index_random_words]) > len(list_find_word):
                list_find_word += '-' * (len(list_words[index_random_words]) - len(list_find_word))
            elif len(list_words[index_random_words]) < len(list_find_word):
                while len(list_find_word) > len(list_words[index_random_words]):
                    list_find_word.pop(len(list_find_word) - 1)
            return list_find_word

        '''spr znaki w słowie uzytym i wpisamyn. 
        Tworzy liste ze znakami poprawnymi. w
        Źle wpisane znaki zamienia na '-' '''

        def check_word(lang_list_words, find_word, index_random_words):
            list_char_word = list()
            for i in range(len(lang_list_words[index_random_words])):
                if lang_list_words[index_random_words][i] == \
                        check_len_word(lang_list_words, find_word, index_random_words)[i]:
                    list_char_word.append(check_len_word(lang_list_words, find_word, index_random_words)[i])
                else:
                    list_char_word.append('-')
            return list_char_word

        '''Wybór opcji językowej, okreslenie zbioru poszukiwanego'''

        def select_lang_version(lang_version_list, index_random_words):
            if lang_version_list == words_pol:  # spr warunku jezykowego (odpoweidz po polsku)
                return words_eng[index_random_words]
            elif lang_version_list == words_eng:  # spr warunku jezykowego (odpoweidz po angielsku)
                return words_pol[index_random_words]

        ''' Pęta az to wpisania pożądanego słowa'''

        def loop_looking_word(lang_version_list, index_random_words, find_word=''):
            while find_word != lang_version_list[index_random_words]:
                find_word = input(select_lang_version(lang_version_list, index_random_words) + ' = '
                                  + str(
                    check_word(lang_version_list, find_word, index_random_words))) .upper() # szukane (wpisywane) slowo
                print('Podano : ' + find_word)  # wydruk poszukiwanego slowaP
                if find_word == lang_version_list[index_random_words]:
                    print('dobrze\n')
                    break
                elif find_word == 'N':  # po wpisanu n pokazuje slowo szukane
                    print(select_lang_version(lang_version_list, index_random_words) + ' = '
                          + lang_version_list[index_random_words] + '\n')  # słówko ang i znaczenie polskie
                    break

        '''Peta kolejnych słów wpisywanydata.bd_main.show_words_in_dict('slowka','pol','ang')ch + usówanie ze zbioru uzytego slowa'''

        def loop_next_word(lang_version_list):
            while len(lang_version_list) > 0:
                index_random_words = random.randint(0, len(lang_version_list) - 1)  # losowanie indexu w zdiorze słóów
                loop_looking_word(lang_version_list, index_random_words,
                                  find_word='')  # opdowiedź po polsku, tytaj wybiera sie jezyk w jakim chce sie odpowiadać.
                if lang_version_list == words_eng:
                    lang_version_list.pop(index_random_words)
                    words_pol.pop(index_random_words)
                elif lang_version_list == words_pol:
                    lang_version_list.pop(index_random_words)
                    words_eng.pop(index_random_words)

        '''zakończenie programu, uruchomienie ponownie, 
        pobranie nowego zbioru słów do programy, ponowny wybór wersji językowej '''

        def loop_quit_program(lang_version_list, quit_program=''):
            while quit_program != 'y':  # pętla do póki nie wybierzes się 'y' przy zakończeniu programu
                loop_next_word(lang_version_list)  # tu nalezy określić wersję językową
                quit_program = input('Czy zakończyć (y/n)')
                if quit_program == 'n':  # określenie warunków przy wyborze 'n'. Wybór wersji językowej, uzupełnienie słów w zbiorze
                    again_words_eng = [word for word in dictionary_words]  # ponownie imprementowany zbiór słów ang
                    again_words_pol = [dictionary_words[keys] for keys in
                                       dictionary_words]  # ponownie imprementowany zbiór słów pol
                    for words in again_words_eng:
                        words_eng.append(words)
                    for words in again_words_pol:
                        words_pol.append(words)
                    loop_next_word(choice_language_version())  # ponowny wybór wersji językowej + wpisywanie slów

        '''Określenie przez użytkownika wersji językowej'''

        def choice_language_version(lang_version_list=''):
            while lang_version_list != 'pol' or lang_version_list != 'ang':
                lang_version_list = input('Wybierz w jakim języku chcesz odpowiadać (pol/ang) ')
                if lang_version_list == 'pol':
                    return words_pol
                elif lang_version_list == 'ang':
                    return words_eng

        loop_quit_program(choice_language_version())


    #check char in words set
    def b_check_word_char(self):

        '''słownik do podpięcia modułu'''
        dictionary_words = data.bd_letter.database_like(user.activ_set(),  # activ set
                                                        'pol',  # column pol in select table
                                                        'ang',  # column ang in select table
                                                        self.chx_pol_eng(),  # checked conditions checkbox
                                                        self.lable_char.text())  # set wherein choice char

        # jeśli dwa checkboxy są zaznaczone równocześnie
        if self.checkbox_pol.isChecked() and self.checkbox_eng.isChecked():
            self.error_text.showMessage('Wybierz jeden język, w którym chcesz słówka')

        # jeśli żaden checkbox nie jest zaznaczony
        elif not self.checkbox_pol.isChecked() and not self.checkbox_eng.isChecked():
            self.error_text.showMessage('Wybierz jeden język, w którym chcesz słówka')

        # jeśli nie wybrano literki
        elif self.lable_char.text() == '':
            self.error_text.showMessage('Wybierz literę, na którą chcesz słówka')

        #jeżeli nie ma slówek w zbiorze
        elif not dictionary_words:
            self.error_text.showMessage('Brak słówek na tą litere')

        # wszytkie pola zostały uzupenione
        else:

            '''skopolowany moduł slowo z dobranym zbiorem - zaczynjącym sie na litere'''

            import random

            words_eng = [word for word in dictionary_words]
            words_pol = [dictionary_words[keys] for keys in dictionary_words]

            '''zaminienia slowo wpowadzone na liste znakow'''

            def list_letter(word):
                for letter in range(len(word)):
                    yield word[letter]

            '''#spr. dlugosc podannego slowa ze slowem ze zbioru. 
            Wyrównuje ich dlugosc, wstawiaja lub usuwajac zanki ze slowa'''

            def check_len_word(list_words, find_word, index_random_words):
                list_find_word = list(list_letter(find_word))
                if len(list_words[index_random_words]) == len(list_find_word):
                    return list_find_word
                elif len(list_words[index_random_words]) > len(list_find_word):
                    list_find_word += '-' * (len(list_words[index_random_words]) - len(list_find_word))
                elif len(list_words[index_random_words]) < len(list_find_word):
                    while len(list_find_word) > len(list_words[index_random_words]):
                        list_find_word.pop(len(list_find_word) - 1)
                return list_find_word

            '''spr znaki w słowie uzytym i wpisamyn. 
            Tworzy liste ze znakami poprawnymi. w
            Źle wpisane znaki zamienia na '-' '''

            def check_word(lang_list_words, find_word, index_random_words):
                list_char_word = list()
                for i in range(len(lang_list_words[index_random_words])):
                    if lang_list_words[index_random_words][i] == \
                            check_len_word(lang_list_words, find_word, index_random_words)[i]:
                        list_char_word.append(check_len_word(lang_list_words, find_word, index_random_words)[i])
                    else:
                        list_char_word.append('-')
                return list_char_word

            '''Wybór opcji językowej, okreslenie zbioru poszukiwanego'''

            def select_lang_version(lang_version_list, index_random_words):
                if lang_version_list == words_pol:  # spr warunku jezykowego (odpoweidz po polsku)
                    return words_eng[index_random_words]
                elif lang_version_list == words_eng:  # spr warunku jezykowego (odpoweidz po angielsku)
                    return words_pol[index_random_words]

            ''' Pęta az to wpisania pożądanego słowa'''

            def loop_looking_word(lang_version_list, index_random_words, find_word=''):
                while find_word != lang_version_list[index_random_words]:
                    find_word = input(select_lang_version(lang_version_list, index_random_words) + ' = '
                                      + str(
                        check_word(lang_version_list, find_word, index_random_words))).upper()  # szukane (wpisywane) slowo
                    print('Podano : ' + find_word)  # wydruk poszukiwanego slowaP
                    if find_word == lang_version_list[index_random_words]:
                        print('dobrze\n')
                        break
                    elif find_word == 'N':  # po wpisanu n pokazuje slowo szukane
                        print(select_lang_version(lang_version_list, index_random_words) + ' = '
                              + lang_version_list[index_random_words] + '\n')  # słówko ang i znaczenie polskie
                        break

            '''Peta kolejnych słów wpisywanydata.bd_main.show_words_in_dict('slowka','pol','ang')ch + usówanie ze zbioru uzytego slowa'''

            def loop_next_word(lang_version_list):
                while len(lang_version_list) > 0:
                    index_random_words = random.randint(0, len(lang_version_list) - 1)  # losowanie indexu w zdiorze słóów
                    loop_looking_word(lang_version_list, index_random_words,
                                      find_word='')  # opdowiedź po polsku, tytaj wybiera sie jezyk w jakim chce sie odpowiadać.
                    if lang_version_list == words_eng:
                        lang_version_list.pop(index_random_words)
                        words_pol.pop(index_random_words)
                    elif lang_version_list == words_pol:
                        lang_version_list.pop(index_random_words)
                        words_eng.pop(index_random_words)

            '''zakończenie programu, uruchomienie ponownie, 
            pobranie nowego zbioru słów do programy, ponowny wybór wersji językowej '''

            def loop_quit_program(lang_version_list, quit_program=''):
                while quit_program != 'y':  # pętla do póki nie wybierzes się 'y' przy zakończeniu programu
                    loop_next_word(lang_version_list)  # tu nalezy określić wersję językową
                    quit_program = input('Czy zakończyć (y/n)')
                    if quit_program == 'n':  # określenie warunków przy wyborze 'n'. Wybór wersji językowej, uzupełnienie słów w zbiorze
                        again_words_eng = [word for word in dictionary_words]  # ponownie imprementowany zbiór słów ang
                        again_words_pol = [dictionary_words[keys] for keys in
                                           dictionary_words]  # ponownie imprementowany zbiór słów pol
                        for words in again_words_eng:
                            words_eng.append(words)
                        for words in again_words_pol:
                            words_pol.append(words)
                        loop_next_word(choice_language_version())  # ponowny wybór wersji językowej + wpisywanie slów

            '''Określenie przez użytkownika wersji językowej'''

            def choice_language_version(lang_version_list=''):
                while lang_version_list != 'pol' or lang_version_list != 'ang':
                    lang_version_list = input('Wybierz w jakim języku chcesz odpowiadać (pol/ang) ')
                    if lang_version_list == 'pol':
                        return words_pol
                    elif lang_version_list == 'ang':
                        return words_eng

            loop_quit_program(choice_language_version())

    #update mistake
    def b_update_word(self):
        #gdy któreś pole jest puste to wyświetl error
        if self.lable_pol_word.text() == '' \
                or self.lable_eng_word.text() == '' \
                or self.lable_id.text() == '':
            self.error_text.showMessage('Pola nie mogą być puste')

        #gdy pola się usupełnione
        else:
            data.bd.update_databases(user.activ_set(), #name active set1
                                     'pol', #name pol column
                                     self.lable_pol_word.text().upper(), #name polish word
                                     'ang', #name ang word
                                     self.lable_eng_word.text().upper(), #name eng word
                                     self.lable_id.text()) #id name

            #oczyszczenie pół textowych
            self.lable_pol_word.clear()
            self.lable_eng_word.clear()
            self.lable_id.clear()

            #aktualizacja zbioru
            self.b_print_all_words()

    #print all words in set
    def b_print_all_words(self):
        self.all_set = WinALL()
        self.all_set.show()

'''Window all set - pokazuje wylistowane pozycje zbioru'''
class WinALL(WinUser):

    def properties(self):
        #przesunięcie okna
        self.move(1100,300)

        # Wielkość okna
        self.resize(400, 700)

        #text lable
        self.lable_all_set = QtWidgets.QListWidget()

        #list((data.bd.show_all_values('slowka')))

        'h_box'
        h_box_lable_all_set = QtWidgets.QHBoxLayout()
        h_box_lable_all_set.addStretch()
        h_box_lable_all_set.addWidget(self.lable_all_set)
        h_box_lable_all_set.addStretch()

        #dodanie zbioru w postaci listy
        self.lable_all_set.addItems(data.bd.show_all_values(user.activ_set()))

        #wyświetlenie tego co w okienku
        self.setLayout(h_box_lable_all_set)

    def b_quit(self):
        self.close()


if __name__ == '__main__':
    data.bd.create_data() # utorzenie i połączenie się z baza danych 'slowka'
    data.bd.create_table('slowka','id','pol VARCHAR(255) COLLATE utf8_unicode_ci NOT NULL,',
                         'ang VARCHAR(255) COLLATE utf8_unicode_ci NOT NULL,') #utorzenie dowolnej tabelki
    app = QtWidgets.QApplication(sys.argv)
    user = WinUser()
    sys.exit(app.exec_())
