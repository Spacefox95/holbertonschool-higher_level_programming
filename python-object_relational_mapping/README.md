# Python - Object-relational Mapping

## Description

This directory is dedicated to learning the fundamentals of **Object-Relational Mapping (ORM)**, which is a technique that allows interaction between Python code and relational databases, such as MySQL. The goal of this project is to understand how to bridge the gap between Python classes and database tables by using ORM techniques, primarily through **SQLAlchemy**. Throughout the project, I'll be writing Python scripts to map classes to database tables, retrieve and manipulate data, and establish connections to MySQL databases. The tasks will cover various SQL operations, secure queries, and ORM concepts, enabling efficient and secure data handling.

## :file_folder: Concepts

- **Object-Relational Mapping (ORM)**: Understanding the principles of ORM and how it connects Python objects with database tables.
- **SQLAlchemy**: Introduction to SQLAlchemy, a powerful ORM library for Python.
- **Database connection**: How to connect Python scripts to MySQL databases.
- **Class-to-table mapping**: Creating Python classes that represent database tables.
- **Data retrieval and manipulation**: Querying, inserting, updating, and deleting records using Python code.
- **SQL Injection**: Learning how to prevent SQL injection vulnerabilities in database queries.
- **SQLAlchemy queries**: Using ORM to perform database queries, with a focus on clean and secure data retrieval.
- **Relationships**: Managing one-to-many and many-to-many relationships between tables through Python objects.


## Tasks

### 0. Get all states

Write a script that lists all states from the database `hbtn_0e_0_usa`.

- Your script should take 3 arguments: `mysql username`, `mysql password`, and `database name` (no argument validation needed).
- You must use the module `MySQLdb` (import `MySQLdb`).
- Your script should connect to a MySQL server running on `localhost` at port `3306`.
- Results must be sorted in ascending order by `states.id`.

---

### 1. Filter states

Write a script that lists all states with a name starting with `N` (upper `N`) from the database `hbtn_0e_0_usa`.

- Your script should take 3 arguments: `mysql username`, `mysql password`, and `database name` (no argument validation needed).
- You must use the module `MySQLdb` (import `MySQLdb`).
- Your script should connect to a MySQL server running on `localhost` at port `3306`.
- Results must be sorted in ascending order by `states.id`.

---

### 2. Filter states by user input

Write a script that takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument.

- Your script should take 4 arguments: `mysql username`, `mysql password`, `database name`, and `state name` searched (no argument validation needed).
- You must use the module `MySQLdb` (import `MySQLdb`).
- Your script should connect to a MySQL server running on `localhost` at port `3306`.
- You must use `format` to create the SQL query with the user input.
- Results must be sorted in ascending order by `states.id`.

---

### 3. SQL Injection...

Write a script that takes in arguments and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument. This time, the script should be safe from MySQL injections!

- Your script should take 4 arguments: `mysql username`, `mysql password`, `database name`, and `state name` searched (safe from MySQL injection).
- You must use the module `MySQLdb` (import `MySQLdb`).
- Your script should connect to a MySQL server running on `localhost` at port `3306`.
- Results must be sorted in ascending order by `states.id`.

---

### 4. Cities by states

Write a script that lists all cities from the database `hbtn_0e_4_usa`.

- Your script should take 3 arguments: `mysql username`, `mysql password`, and `database name`.
- You must use the module `MySQLdb` (import `MySQLdb`).
- Your script should connect to a MySQL server running on `localhost` at port `3306`.
- Results must be sorted in ascending order by `cities.id`.
- You can only use `execute()` once.

---

### 5. All cities by state

Write a script that takes in the name of a state as an argument and lists all cities of that state using the database `hbtn_0e_4_usa`.

- Your script should take 4 arguments: `mysql username`, `mysql password`, `database name`, and `state name` (SQL injection free!).
- You must use the module `MySQLdb` (import `MySQLdb`).
- Your script should connect to a MySQL server running on `localhost` at port `3306`.
- Results must be sorted in ascending order by `cities.id`.

---

### 6. First state model

Write a Python file that contains the class definition of a `State` and an instance `Base = declarative_base()`.

- `State` class:
  - Inherits from `Base`.
  - Links to the MySQL table `states`.
  - Has class attributes `id` (auto-generated, unique integer, primary key) and `name` (string of max 128 characters, can't be null).
- You must use the module `SQLAlchemy`.
- Your script should connect to a MySQL server running on `localhost` at port `3306`.

---

### 7. All states via SQLAlchemy

Write a script that lists all `State` objects from the database `hbtn_0e_6_usa`.

- Your script should take 3 arguments: `mysql username`, `mysql password`, and `database name`.
- You must use the module `SQLAlchemy`.
- You must import `State` and `Base` from `model_state`.
- Results must be sorted in ascending order by `states.id`.

---

### 8. First state

Write a script that prints the first `State` object from the database `hbtn_0e_6_usa`.

- Your script should take 3 arguments: `mysql username`, `mysql password`, and `database name`.
- Results must be displayed as `id: <state id> name: <state name>`.
- If the table `states` is empty, print `Nothing`.

---

### 9. Contains `a`

Write a script that lists all `State` objects that contain the letter `a` from the database `hbtn_0e_6_usa`.

- Your script should take 3 arguments: `mysql username`, `mysql password`, and `database name`.
- Results must be sorted in ascending order by `states.id`.

---

### 10. Get a state

Write a script that prints the `State` object with the name passed as an argument from the database `hbtn_0e_6_usa`.

- Your script should take 4 arguments: `mysql username`, `mysql password`, `database name`, and `state name to search`.
- If no state has the name you searched for, display `Not found`.

---

### 11. Add a new state

Write a script that adds the `State` object "Louisiana" to the database `hbtn_0e_6_usa`.

- Your script should take 3 arguments: `mysql username`, `mysql password`, and `database name`.
- Print the new `states.id` after creation.

---

### 12. Update a state

Write a script that changes the name of a `State` object from the database `hbtn_0e_6_usa`.

- Change the name of the `State` where `id = 2` to `New Mexico`.

---

### 13. Delete states

Write a script that deletes all `State` objects with a name containing the letter `a` from the database `hbtn_0e_6_usa`.

- Your script should take 3 arguments: `mysql username`, `mysql password`, and `database name`.

---

### 14. Cities in state

Write a Python file `model_city.py` that contains the class definition of a `City`.

- `City` class:
  - Inherits from `Base`.
  - Links to the MySQL table `cities`.
  - Has class attributes `id`, `name`, and `state_id` (foreign key to `states.id`).
- Write a script that prints all `City` objects from the database `hbtn_0e_14_usa`.

---

## Author

- **Nathan Raynal**

---

This project is part of the **Holberton School curriculum** to build foundational knowledge in databases and SQL.