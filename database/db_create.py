#! /usr/bin/python
# coding: utf-8


from .settings import DB_HOST, DB_NAME, DB_PWD, DB_USER
import mysql.connector
from mysql.connector import errorcode

db_connexion = mysql.connector.connect(host=DB_HOST, user=DB_USER,
                                       password=DB_PWD)
db_cursor = db_connexion.cursor()


# TODO: make a DB class
def create_database(cursor):
    """ Creates a DB for the application if programme cannot find it """
    try:
        db_cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


try:
    db_cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(db_cursor)
        print("Database {} created successfully.".format(DB_NAME))
        db_connexion.database = DB_NAME
    else:
        print(err)
        exit(1)
