import sys
from PyQt5 import QtWidgets, QtGui, QtCore
import data


'''Wybór tabeli z bazy naych po wprowadzniu'''
class WinUser(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.center() #pozycjonowanie zawsze na środku ekranu
        self.properties()

        # Tytuł okienka
        self.setWindowTitle('Translator_program')

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

        self.shortcut_quit = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+Q"),self)
        self.shortcut_quit.activated.connect(self.b_quit)

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

class WinMain(WinUser):
    '''okno nr 2 tłumacz'''
    def properties(self):
        #Wielkość oknaP
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
        self.lable_text_to_translate_eng = QtWidgets.QLineEdit()


        # lable text
        text_bold = QtGui.QFont()
        text_bold.setBold(True)
        self.visible_text_translate_pol = QtWidgets.QLabel('Przetłumacz na język Polski:')
        self.visible_text_translate_pol.setAlignment(QtCore.Qt.AlignCenter)
        self.visible_text_translate_pol.setFont(text_bold)

        self.visible_text_translate_eng = QtWidgets.QLabel('Przetłumacz na język Angielski:')
        self.visible_text_translate_eng.setAlignment(QtCore.Qt.AlignCenter)
        self.visible_text_translate_eng.setFont(text_bold)

        self.visible_text_check_self = QtWidgets.QLabel('Sprawdź co pamiętasz:')
        self.visible_text_check_self.setAlignment(QtCore.Qt.AlignCenter)
        self.visible_text_check_self.setFont(text_bold)

        self.visible_text_base_opction = QtWidgets.QLabel('Operacje na zbiorze::')
        self.visible_text_base_opction.setAlignment(QtCore.Qt.AlignCenter)
        self.visible_text_base_opction.setFont(text_bold)


        # lable text action
        self.lable_text_action = QtWidgets.QLabel() #text po zrobieniu jakieś akcji na końcu
        self.lable_text_action.setAlignment(QtCore.Qt.AlignCenter)

        self.lable_text_action_trans_pol = QtWidgets.QLabel('Oznacza: ') #output translated text eng
        self.lable_text_action.setAlignment(QtCore.Qt.AlignCenter)
        self.lable_text_action_trans_pol.setFont(text_bold)

        self.lable_text_action_trans_eng = QtWidgets.QLabel('Oznacza: ') #output translated text eng
        self.lable_text_action_trans_eng.setAlignment(QtCore.Qt.AlignCenter)
        self.lable_text_action_trans_eng.setFont(text_bold)

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

        # button check_all_words and check_char
        v_box.addWidget(self.btw_check_all_words)
        v_box.addWidget(self.btw_check_word_char)

        #text 'Operacje na zabiorze'
        v_box.addStretch()
        v_box.addLayout(h_box_text_base_opction)
        v_box.addStretch()

        # button update_set and print all words in set
        v_box.addStretch()
        v_box.addWidget(self.btw_update_word)
        v_box.addWidget(self.btw_pint_all_words)
        v_box.addStretch()

        # button quit program
        v_box.addWidget(self.btw_quit)

        # text action bottom
        v_box.addStretch()
        v_box.addLayout(h_box_action)
        v_box.addStretch()

        '''okreslenie wartwy wyśiwtlanej'''
        self.setLayout((v_box))

        self.show()


if __name__ == '__main__':
    data.bd.create_data() # utorzenie i połączenie się z baza danych 'slowka'
    data.bd.create_table('slowka','id','pol VARCHAR(255) COLLATE utf8_unicode_ci NOT NULL,','ang VARCHAR(255) COLLATE utf8_unicode_ci NOT NULL,') #utorzenie dowolnej tabelki
    app = QtWidgets.QApplication(sys.argv)
    user = WinUser()
    sys.exit(app.exec_())


