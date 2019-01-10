#!/usr/bin/env python3
#-*- coding: utf-8 -*-


import mysql.connector
'''kwerendy do obsługi baz danych'''
class Database:


    def __init__(self):
        self.mydb=mysql.connector.connect( #połoczenie z bazą danych'''
            host = 'localhost',
            user = 'root',
            port = '3307',
            passwd ='',
            collation = 'utf8_unicode_ci',
            database = 'slowka')
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
        self.mycursor.execute("INSERT INTO {name_table} (pol,ang) VALUES ("
                              "'{word_pol}','{word_ang}');".format(
                                                                name_table = name_table,
                                                                word_pol = word_pol,
                                                                word_ang = word_ang
                                                                ))
        self.mydb.commit()

    '''poprawianie wartości w bd'''
    def update_databases(self,name_table,pol,value_pol,ang,value_ang,index_value):
        self.mycursor.execute("UPDATE {name_table} SET {column_name_pol} = '{value_name_pol}',"
                              " {column_name_ang} = '{value_name_ang}' where id = {index_value}".format(
                                                                name_table = name_table,
                                                                column_name_pol = pol,
                                                                value_name_pol = value_pol,
                                                                column_name_ang = ang,
                                                                value_name_ang = value_ang,
                                                                index_value = index_value
                                                                ))
        self.mydb.commit()

    '''drukowanie wszystkich wartosci wraz z id tabeli'''
    def show_all_values(self,name_table):
        list_table = list()
        self.mycursor.execute("SELECT * FROM {name_table}".format(name_table = name_table))
        myresult = self.mycursor.fetchall()
        for words in myresult:
            list_table.append(str(words))
        return list_table

    '''drukowanie wartosci z tabeli pol i ang'''
    def show_pol_ang_values(self, name_table,pol,ang):
        list_table = list()
        self.mycursor.execute("SELECT {column_name_pol}, {column_name_ang} FROM {name_table}".format(name_table=name_table,
                                                                         column_name_pol=pol,
                                                                         column_name_ang=ang
                                                                         ))
        myresult = self.mycursor.fetchall()
        for words in myresult:
            list_table.append(words)
        return list_table

    '''drukowanie wszytich tabel'''
    def show_tables(self):
        list_table=list()
        self.mycursor.execute("SHOW TABLES;")
        myresult = self.mycursor.fetchall()
        for table in myresult:
            list_table.append(''.join(table))
        return list_table


'''odczyt wszystkich slowek z tabeli w postaci słownika'''
class Data1(Database):
    def show_words_in_dict(self,name_table,pol,ang):
        dict_words = dict()
        self.mycursor.execute("SELECT {version_lang_ang}, {version_lang_pol} FROM {name_table};".format(
                                                                    name_table = name_table,
                                                                    version_lang_pol = pol,
                                                                    version_lang_ang = ang
                                                                    ))
        myresult_words = self.mycursor.fetchall()
        self.mydb.commit()
        for key,values in myresult_words:
            dict_words.update({key:values})
        return dict_words

'''utorzenie zbioru zaczynajacego sie na litere '''
class Data2(Database):

    def database_like(self,name_table, pol, ang, sort_pol, letter):
        dict_words = dict()
        self.mycursor.execute("SELECT {version_lang_pol}, {version_lang_ang} "
                              "FROM {name_table} WHERE {sort_word} LIKE '{sort_letter}%'".format(
                                                                    name_table = name_table,
                                                                    version_lang_pol = pol,
                                                                    version_lang_ang = ang,
                                                                    sort_word = sort_pol,
                                                                    sort_letter = letter
                                                                    ))
        myresult_words = self.mycursor.fetchall()
        self.mydb.commit()
        for key, values in myresult_words:
            dict_words.update({key: values})
        return dict_words



bd=Database()
bd_main = Data1()
bd_letter = Data2()






