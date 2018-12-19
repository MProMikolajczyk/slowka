#!/usr/bin/env python3
#-*- coding: utf-8 -*-



dictionary_words = {'bed' : 'łóżko',
                    'chair' : 'krzesło',
                    'desk' : 'biurko'} #to ma być na wyjściu

import mysql.connector

class Database(object):


    def __init__(self):
        self.mydb=mysql.connector.connect( #połoczenie z bazą danych'''
            host = 'localhost',
            user = 'root',
            port = '3307',
            passwd ='',
            collation = 'utf8_unicode_ci')
        self.mycursor = self.mydb.cursor()


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
                                                           name_column_2 = name_column_attribute_2))
        self.mydb.commit()

    '''dodawanie do tabeli slowek '''
    def insert_into_table(self):
        pass



bd=Database()
bd.create_data()
bd.create_table('slowka','id','pol VARCHAR(255) NOT NULL,','ang VARCHAR(255) NOT NULL,')


#mycursor.executemany() dodaje całe listy danych

#for db in mycursor: #drukowanie wszystkich baz danych
    #print(db)

#myresult = mycursor.fetchall() # używane do otrzywyania wyrukóœ wyników zapytań
#myresult = mycursor.fetchone()# otrzymuje tylko jeden wynik zapytania

#mydb.commit() # bez tej komendy zapytania nie znają się w bazie danych
