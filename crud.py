import os

from dotenv import load_dotenv
load_dotenv()

import psycopg


def connection(user: str, password: str, host: str, port: str, database: str) -> psycopg.Connection:
    """
    Connect to the PostgreSQL database using psycopg.
    """
    try: 
        conn = psycopg.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            dbname=database,
            autocommit=True
        )
        return conn
    except psycopg.Error as e:
        print('Connection failed.')
        print(e)


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
    database = os.getenv('DATABASE')
    user = os.getenv('USER')
    password = os.getenv('PASSWORD')
    host = os.getenv('HOST')
    port = os.getenv('PORT')

    print(database, user, password, host, port)

    # connect to database
    with connection(user, password, host, port, database) as conn:
        print(conn)


if __name__=='__main__':
    main()

