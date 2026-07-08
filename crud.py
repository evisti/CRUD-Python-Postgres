import os 
import psycopg

from dotenv import load_dotenv
load_dotenv()


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
        print("Connection failed.")
        print(e)


class CRUD():
    def __init__(self, connection: psycopg.Connection):
        self.conn = connection
        self.cur = self.conn.cursor()

    def _run_query(self, query: str) -> None:
        """
        Start a transaction and run a query against the database. COMMIT is executed at the end of the transaction block.
        """
        with self.conn.transaction():
            self.cur.execute(query)

    def create_table(self) -> None:
        """
        Create table, if it doesn't already exist.
        """
        create_table_query = """
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            );"""
        self._run_query(create_table_query)

    def create_record(self, name: str, email: str) -> None:
        """
        Create a new record in the table (C in CRUD)
        """
        # use t-string to process query parameters in a safe way (new in Python 3.14)
        insert_query = t"INSERT INTO users (name, email) VALUES ({name}, {email})"

        # execute query
        try:
            self._run_query(insert_query)
        except psycopg.errors.UniqueViolation as e:
            print(f"Error: Email {email} already exists. You cannot insert a new record with an email that already exists.")
        else:
            print(self.cur.rowcount, "record inserted")


    def read(self):
        """
        Read and print all records from the table (R in CRUD)
        """
        read_query = 'SELECT * FROM users;'
        self.cur.execute(read_query)

        # iterate on the cursor to print the records
        for record in self.cur:
            print(record)


    def update_record(self):
        pass

    def delete_record(self):
        pass


def main():
    database = os.getenv("DATABASE")
    user = os.getenv("USER")
    password = os.getenv("PASSWORD")
    host = os.getenv("HOST")
    port = os.getenv("PORT")

    # connect to database
    with connection(user, password, host, port, database) as conn:
        # initialize
        crud = CRUD(conn)

        # create table, if it doesn't already exist
        crud.create_table()

        # Perform CRUD operations on the table:

        # create a few new records
        crud.create_record("Jessica Hogg", "jess.hogg@example.com")
        crud.create_record("Katrina Parr", "kparr@example.com")
        crud.create_record("Master Robin", "master.robin@example.com")
        crud.create_record("Necrotic Ninja", "necrotic@ninja.com")

        # read all records
        crud.read()



    # The database connection is closed at the end of this block


if __name__=="__main__":
    main()

