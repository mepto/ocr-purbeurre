#! /usr/bin/python
# coding: utf-8

from database.db_create import PbDatabase


def start():
    print('hello')
    new_db = PbDatabase().check_db_exists()
    print(new_db)


if __name__ == "__main__":
    start()
