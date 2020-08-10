#! /usr/bin/python
# coding: utf-8

import mysql.connector
from mysql.connector import errorcode, Error
from .settings import *


class PbDatabase:
    """ Database creator class """

    db_connexion = mysql.connector.connect(host=DB_HOST, user=DB_USER,
                                           password=DB_PWD)
    db_cursor = db_connexion.cursor()

    def __init__(self):
        self.host = DB_HOST
        self.user = DB_USER
        self.password = DB_PWD
        self.name = DB_NAME
        self.exists = self.check_db_exists

    def check_db_exists(self, config=DB_USER):
        try:
            mysql.connector.connect(config)
            print('Connected to pur beurre database')
            return True
        except mysql.connector.Error as err:
            print(f'Cannot connect to pur beurre database: {err}')
            return False

    def create_database(self, cursor):
        """ Creates a DB for the application if programme cannot find it """
        if self.exists:
            """ drop OFF tables """
            pass
        else:
            """ create new table """
            self.db_cursor.execute(DB_CREATION)
