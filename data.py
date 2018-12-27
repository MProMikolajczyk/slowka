#!/usr/bin/env python3
#-*- coding: utf-8 -*-


import mysql.connector

class Database(object):


    def __init__(self):
        self.mydb=mysql.connector.connect( #połoczenie z bazą danych'''
            host = 'localhost',
            user = 'root',
            port = '3307',
            passwd ='',
            collation = 'utf8_unicode_ci')
        self.mycursor = self.mydb.cursor() #definiowanie dodawania zapytań

    '''utorzenie bazydanych slowka'''
    def create_data(self):
        self.mycursor.execute("CREATE DATABASE IF NOT EXISTS slowka;")
        self.mycursor.execute("USE slowka;")
        self.mydb.commit()

    '''utorzenie tabeli '''
    def create_table(self,name_table,identity,name_column_attribute_1 = '',name_column_attribute_2 = ''):
        self.mycursor.execute("CREATE TABLE IF NOT EXISTS {name_table}("
                              "{id} INT NOT NULL AUTO_INCREMENT, "
                              "{name_column_1} "
                              "{name_column_2} "
                              "PRIMARY KEY({id}));".format(name_table=name_table,
                                                           id = identity,
                                                           name_column_1 = name_column_attribute_1,
                                                           name_column_2 = name_column_attribute_2
                                                           ))
        self.mydb.commit()

    '''dodawanie do tabeli slowek '''
    def insert_into_table(self, name_table, word_pol, word_ang):
        self.mycursor.execute("INSERT INTO {name_table} (pol,ang) VALUES ('{word_pol}','{word_ang}');".format(name_table = name_table,
                                                                                            word_pol = word_pol,
                                                                                            word_ang = word_ang
                                                                                            ))
        self.mydb.commit()

    '''odczyt wszystkich slowek z tabeli w postaci słownika'''
    def show_words_in_dict(self):
        dict_words = dict()
        self.mycursor.execute("SELECT ang, pol FROM slowka;")
        myresult_words = self.mycursor.fetchall()
        self.mydb.commit()
        for key,values in myresult_words:
            dict_words.update({key:values})
        return dict_words



bd=Database()
bd.create_data()
bd.create_table('slowka','id','pol VARCHAR(255) COLLATE utf8_unicode_ci NOT NULL,','ang VARCHAR(255) COLLATE utf8_unicode_ci NOT NULL,')
#bd.insert_into_table('slowka','niebieski','blue') #dodawanie słówek do tabeli
bd.show_words_in_dict() #wyjściowe słownik do slówek







'''pomoc naukowa'''
#mycursor.executemany() dodaje całe listy danych

#for db in mycursor: #drukowanie wszystkich baz danych
    #print(db)

#myresult = mycursor.fetchall() # używane do otrzywyania wyrukóœ wyników zapytań
#myresult = mycursor.fetchone()# otrzymuje tylko jeden wynik zapytania

#mydb.commit() # bez tej komendy zapytania nie znają się w bazie danych
