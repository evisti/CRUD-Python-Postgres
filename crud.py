import os

from dotenv import load_env()
load_env()

import psycopg


def connection():
    pass


class CRUD():
    def __init__(self, connection: psycopg.Connection):
        pass

    def _execute_query(self, query: str):
        pass

    def create_table(self):
        pass

    def create_record(self):
        pass

    def read(self):
        pass

    def update_record(self):
        pass

    def delete_record(self):
        pass


def main():
    pass


if __name__=='__main__':
    main()

