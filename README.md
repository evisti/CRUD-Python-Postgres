# CRUD operations in PostgreSQL and Python

This project demonstrates how to perform the four basic CRUD operations on a PostgreSQL database using Python.

CRUD stands for create, read, update, and delete. These are the four fundamental operations used to manage data in a database.
The project encapsulates the operations in a single class, making it easy to interact with the database through one object. 


## Requirements

Before running the project, ensure the following are installed:
- Python 3.14 or higher
- PostgreSQL


## Setup

### Dependencies 

Run the following command to install all required dependendencies:
```bash
uv sync
```

### Configure environment variables

Create a `.env` file in the project root from the template:
```bash
cp .env.template .env
```
Then edit `.env` and provide your PostgreSQL connection details.


## Example

Run the script in the terminal:
```bash
uv run crud.py
```

This will:
- Create a new table
- Create a few records
- Read all records
- Update a record
- Delete a record
