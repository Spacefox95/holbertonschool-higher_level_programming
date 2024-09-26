# SQL - More Queries

## General Objectives

- Create a new MySQL user
- Manage privileges for a user on a database or table
- Understand and use `PRIMARY KEY` and `FOREIGN KEY` constraints
- Use `NOT NULL` and `UNIQUE` constraints
- Retrieve data from multiple tables in a single query
- Understand subqueries
- Work with `JOIN` and `UNION` clauses

## Tasks

### 0. My privileges!
Write a script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (in `localhost`).


### 1. Root user
Write a script that creates the MySQL server user `user_0d_1`.

- `user_0d_1` should have all privileges on your MySQL server.
- The password for `user_0d_1` should be `user_0d_1_pwd`.

### 2. Read user
Write a script that creates the database `hbtn_0d_2` and the user `user_0d_2`.

- `user_0d_2` should have only `SELECT` privileges in the `hbtn_0d_2` database.
- The password for `user_0d_2` should be `user_0d_2_pwd`.

### 3. Always a name
Write a script that creates a table `force_name` with the following properties:
- `id` of type `INT`
- `name` of type `VARCHAR(256)` and cannot be `NULL`

### 4. ID can't be null
Write a script that creates a table `id_not_null` with the following properties:
- `id` of type `INT`, default value is `1`
- `name` of type `VARCHAR(256)`

### 5. Unique ID
Write a script that creates a table `unique_id` with the following properties:
- `id` of type `INT`, default value is `1`, and it must be unique.
- `name` of type `VARCHAR(256)`

### 6. States table
Write a script that creates the database `hbtn_0d_usa` and a table `states`.

- `id` should be `INT`, unique, auto-generated, cannot be `NULL`, and should be the primary key.
- `name` should be `VARCHAR(256)` and cannot be `NULL`.

### 7. Cities table
Write a script that creates the database `hbtn_0d_usa` and a table `cities`.

- `id` should be `INT`, unique, auto-generated, cannot be `NULL`, and should be the primary key.
- `state_id` should be an `INT`, cannot be `NULL`, and must be a foreign key that references the `id` field of the `states` table.
- `name` should be `VARCHAR(256)` and cannot be `NULL`.

### 8. Cities of California
Write a script that lists all the cities of California from the `hbtn_0d_usa` database.

- Results should be sorted by `cities.id` in ascending order.
- You are not allowed to use the `JOIN` keyword.

### 9. Cities by States
Write a script that lists all cities from the `hbtn_0d_usa` database, including the corresponding state.

- Results should display: `cities.id - cities.name - states.name`
- Results should be sorted by `cities.id` in ascending order.
- You can use only one `SELECT` statement.

### 10. Genre ID by show
Import the database dump `hbtn_0d_tvshows` and write a script that lists all shows that have at least one genre linked.

- Results should display: `tv_shows.title - tv_show_genres.genre_id`
- Results should be sorted by `tv_shows.title` and `tv_show_genres.genre_id` in ascending order.

### 11. Genre ID for all shows
Write a script that lists all shows from the `hbtn_0d_tvshows` database. If a show doesn’t have a genre, display `NULL`.

- Results should display: `tv_shows.title - tv_show_genres.genre_id`
- Results should be sorted by `tv_shows.title` and `tv_show_genres.genre_id` in ascending order.

### 12. No genre
Write a script that lists all shows from `hbtn_0d_tvshows` that don’t have any genre linked.

- Results should display: `tv_shows.title - tv_show_genres.genre_id`
- Results should be sorted by `tv_shows.title` and `tv_show_genres.genre_id` in ascending order.

### 13. Number of shows by genre
Write a script that lists all genres from `hbtn_0d_tvshows` and displays the number of shows linked to each.

- Results should display: `<TV Show genre> - <Number of shows linked to this genre>`
- The first column should be called `genre` and the second column `number_of_shows`.
- Results should be sorted in descending order by the number of shows linked.

---

## Author

- **Nathan Raynal**

---

This project is part of the **Holberton School curriculum** to build foundational knowledge in databases and SQL.