import sys
from PyQt5 import QtWidgets, QtGui, QtCore
import data


'''Wybór tabeli z bazy naych po wprowadzniu'''
class WinUser(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.center() #pozycjonowanie zawsze na środku ekranu
        self.user()



    '''zawartośc okienka '''
    def user(self):
        #Wielkość okna
        self.resize(300, 200)

        #Tytuł okienka
        self.setWindowTitle('Translator_program')

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


        self.show()

    '''pozycjonowanie okienka '''
    def center(self):
        geometry = self.frameGeometry()
        center_point = QtWidgets.QDesktopWidget().availableGeometry().center()
        geometry.moveCenter(center_point)
        self.move(geometry.topLeft())

    '''przyciski '''
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

        # baza nieistniejąca
        else:
            data.bd.create_table(self.lable_base_text.text().lower(), 'id', 'pol VARCHAR(255) COLLATE utf8_unicode_ci NOT NULL,',
                                 'ang VARCHAR(255) COLLATE utf8_unicode_ci NOT NULL,')
            self.lable_text_action.setText('Utorzono zbiór')

    #przejście do następnego okna
    def b_connect(self):
        if self.lable_base_text.text().lower() == '':
            self.error.showMessage('Wybierz zbiór')
        else:
            self.close()
            self.main = WinMain()
            self.main.show()

class WinMain(WinUser):
    pass

if __name__ == '__main__':
    data.bd.create_data() # utorzenie i połączenie się z baza danych 'slowka'
    data.bd.create_table('slowka','id','pol VARCHAR(255) COLLATE utf8_unicode_ci NOT NULL,','ang VARCHAR(255) COLLATE utf8_unicode_ci NOT NULL,') #utorzenie dowolnej tabelki
    app = QtWidgets.QApplication(sys.argv)
    user = WinUser()
    sys.exit(app.exec_())

