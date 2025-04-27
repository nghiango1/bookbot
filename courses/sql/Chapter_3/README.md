# Chapter 3: Constraints

## Lesson 1: Null value

NULL value: SQL support NULL the value to express that the data is missing

We can specify a COLUMN can or cannot be NULL to allow using this constraint

Assignment: Write a query to `SELECT` all of the fields on all records of the `transactions` table.

```sh
source ../.alias
run CH3_L01_SELECT.sql
```

## Lesson 2: Constraints

A `constraint` is a rule we create on a database that enforces some specific behavior, extremely useful when we need to ensure that certain kinds of data exist within our database

For example:

- Setting a `NOT NULL` constraint on a column ensures that the column will not accept `NULL` values.
- This can be set within `CREATE TABLE` for each `COLUMN` define
- Or `ADD CONSTRAINT` within an `ALTER TABLE` statement (however [SQLite doesn't support this](https://www.sqlite.org/omitted.html))

Assignment: CashPal need to rebuild our database `users` table with the proper constraints!

- `id` - INTEGER, PRIMARY KEY
- `name` - TEXT, NOT NULL
- `age` - INTEGER, NOT NULL
- `country_code` - TEXT, NOT NULL
- `username` - TEXT, UNIQUE, NOT NULL
- `password` - TEXT, NOT NULL
- `is_admin` - BOOLEAN

The creation of table is easy enough

```sh
run CH3_L02_CREATE_TABLE.sql
```

However, I realized that pk collumn from my last implementation [TABLE_INFO](../TABLE_INFO.sql) doesn't work as intended. Which cause me to find out that

- `information_schema.key_column_usage` contain the `constain_name` along with `column_name`, the created `column_name` is the same with what we had defined in `CREATE TABLE`)
- `information_schema.table_constraints` contain the `constain_name` along with `constain_type`, that `constain_type` is the same with the constants name (eg: `PRIMARY KEY`, `UNIQUE`) we had defined in `CREATE TABLE`

My last assumntion about `pk` key is wrong (a non related field from `information_schema.columns` being placed in that instead). So it time to corrected it:

- I create a new FUNCTION return the QUERY if `table`, `column` is a `PRIMARY KEY`. This process behave the same with original `information_schema.columns` covered, we only have to use `JOIN ON` to lineup `constain_name` found between two table.
- Next, is create a FUNCTION that return BOOLEAN if `table`, `column` is a `PRIMARY KEY`: Which use the QUERY above, check if it return at least 1 record row. We use `SELECT EXISTS`, `INTO` and variable `DECLARE`
- Update our original `TABLE_INFO` to use new helper BOOLEAN function. It suppridingly easy though, and behave exactly like any other operation (or builtin function call)

> `DROP FUNCTION` is use, as I messed up the type a lot, which make `CREATE OR REPLACE` failed to overide the previously created `FUNCTION`

## Lesson 3: Primary Keys

A key defines and protects relationships between tables.

A primary key is a special column that uniquely identifies records within a table. Each table can have one, and only one primary key.

- It's very common to have a column named `id` on each table in a database
- And, that `id` is the primary key for that table.
- No two rows in that table can share an `id`.
- A `PRIMARY KEY` constraint can be explicitly specified on a column to ensure uniqueness, rejecting any inserts where you attempt to create a duplicate ID.

> Ehh, I belive we can set two column as a primary key

Assignment: Fixing wrong `INSERT INTO`

Result:

```sh
run CH3_L03_INSERT_INTO.sql
```

## Lesson 4: Foreign Keys

Foreign keys define the relationships between tables. Bring the relational to relational databases.

We will need to and `CONSTRAINT` to define the `FOREIGN KEY` and its `REFERENCES`, either:

- Through `CREATE TABLE`:

```sql
CREATE TABLE departments (
    id INTEGER PRIMARY KEY,
    department_name TEXT NOT NULL
);

CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department_id INTEGER,
    CONSTRAINT fk_departments
    FOREIGN KEY (department_id)
    REFERENCES departments(id)
);
```

- Through `ALTER TABLE`: Look at Lesson 2 on `ADD CONSTRAINT`- SQLite doesn't support this operation though, Added side quest

```sql
CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INTEGER,
  country_code TEXT NOT NULL,
  username TEXT ,
  password TEXT,
  is_admin BOOLEAN
);

ALTER TABLE users
-- ADD CONSTRAINT
ADD FOREIGN KEY (country_code) REFERENCES countries(code);
```

> After added `FOREIGN KEY`, we can't drop the table `countries` as `users` will depended on it. Thus, we need to drop `users` table first

Assignment: Blah, Blah, `INSERT INTO` need fix, error message is as bellow

```
psql:CH3_L04_INSERT_INTO_2.sql:57: ERROR:  insert or update on table "users" violates foreign key constraint "users_country_code_fkey"
DETAIL:  Key (country_code)=(IND) is not present in table "countries".
```

Result:

```sh
run CH3_L04_INSERT_INTO_2.sql
```
