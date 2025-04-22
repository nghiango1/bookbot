# Chapter 2: Table

## Lesson 1: Creating a table

Example command:

```sql
CREATE TABLE employees (id INTEGER, name TEXT, age INTEGER, is_manager BOOLEAN, salary INTEGER);
```

Assignment: Let's begin building a table for CashPal database! Create the people table with the following fields:

- `id` - Integer
- `tag` - Text
- `name` - Text
- `age` - Integer
- `balance` - Integer
- `is_admin` - boolean

We will have our own custom table info as how posgress like to represent it table though:

- The output is provided in `postgres-table-full-info.txt`
- Command to be run as bellow

```sql
SELECT
    *
FROM
    information_schema.columns
WHERE
    table_name = 'people';
```

Unless, we still want to see some thing that rather similar to output from boot.dev's UI. I put it inside `CH2-L01-CREATE.sql`, more small chalenge:

- In `information_schema.columns`, we have `yes_or_no` type, which contain literal `'YES'/'NO'` string to representing BOOLEAN before it become a thing in SQL
- We not have `notnull`, but we have `is_nullable`. So in reverse, we check if `is_nullable = 'NO'` (compare in SQL using a single `=`, just like Pascal)
- The same with `pk` and `is_identity`, but we use `is_nullable <> 'NO'` (Not equal is also using `<>`, just like Pascal)
- Next is cast it into `0/1` to make it look the same with SQLite
- `CAST (is_nullable = 'NO' AS INTEGER)`
- The res is to match colume name and value to make them fell the same

```sh
alias run="sudo -u postgres psql -d localdb -f "
# source ../.alias

run CH2-L01-CREATE.sql
```

Expected it to be the same with this table

| cid | name     | type    | notnull | dflt_value | pk  |
| --- | -------- | ------- | ------- | ---------- | --- |
| 0   | id       | INTEGER | 0       |            | 0   |
| 1   | tag      | TEXT    | 0       |            | 0   |
| 2   | name     | TEXT    | 0       |            | 0   |
| 3   | age      | INTEGER | 0       |            | 0   |
| 4   | balance  | INTEGER | 0       |            | 0   |
| 5   | is_admin | BOOLEAN | 0       |            | 0   |

## Lesson 2: Creating table practice

In most relational databases a single table isn't enough to hold all the data we need! We usually create a table-per-entity

Assigment: Create the `transactions` table with the following fields:

- `id` - Integer
- `recipient_id` - Integer
- `sender_id` - Integer
- `note` - Text
- `amount` - Integer

```sh
run CH2-L02-CREATE-2.sql
```

## Lesson 3: Altering tables

Alter table lession:

- Rename table, column
- Add/Drop a column: Each column must be added in a separate ALTER TABLE command

```sql
ALTER TABLE <name>
RENAME TO <new_name>
RENAME COLUMN <col_name> TO <new_col_name>;

ALTER TABLE <name>
ADD COLUMN <col_name> TEXT;

ALTER TABLE <name>
DROP COLUMN <col_name>;
```

The Assignment is simple enough

```sql
-- Assignment

-- 1. Rename the table to users
ALTER TABLE people
RENAME TO users;

-- 2. Rename the tag column to username.
ALTER TABLE users
RENAME COLUMN tag TO username;

-- 3. Add the password (TEXT) column.
ALTER TABLE users
ADD COLUMN password TEXT;
```

So I done aditional side quest here, which is to reduce the need to place the full alternative query for `TABLE_INFO()`:

- Create a PL/SQL function that will return the table_info query result
- We then use the mini-fy function call to show the result using one line `SELECT * FROM TABLE_INFO(<table_name>)`

```sql
CREATE OR REPLACE FUNCTION TABLE_INFO(p_table_name TEXT)
RETURNS TABLE (
    cid INTEGER,
    name TEXT,
    type TEXT,
    notnull INTEGER,
    dflt_value TEXT,
    pk INTEGER
) AS $$
BEGIN
    PERFORM QUERY
    SELECT
        ordinal_position - 1 as cid,
        column_name::TEXT as name,
        upper(data_type) as type,
        (is_nullable = 'NO')::INTEGER as notnull,
        column_default::TEXT as dflt_value,
        (is_identity <> 'NO')::INTEGER as pk
    FROM
        information_schema.columns
    WHERE
        table_name = p_table_name
    ORDER BY cid;
END;
$$ LANGUAGE plpgsql;
```

```sh
# Side quest function
run ../TABLE_INFO.sql

# Assigment using TABLE_INFO() function
run CH2-L03-ALTER_TABLE.sql
```

## Lesson 4-6: Intro to Migrations

A database migration is a set of changes to a relational database, adapting it to new requirement (or just fixing bug really)

We dealing with the structure of data, which generally:

- Avoid big change, we modify a lot of internal data here
- Adding new column: Is safe for the application, it take a lot of time though, but code should be fine
- Delete: expect it will break anything that depend on the data, code will break need to update imediately.
- Update: The same thing vs Delete, could be really dramatic if we reusing feild, which code may behave in not expected way. Data will be at risk thoughm as we changing them, and it may unreverse-able (There is a case that we using Oracle DB, that because it support 15 mins reverse the UPDATE change, so we can fix the thing)

In my profesional time, we mostly:

- Copy the full database, versionning them base from application version
- Alternative/Migrating the copy database, runing new code with the new database's table
- This allowing rollback the last version way way easier
- We don't really drop old version at all thought

Up-Down migration type: When writing **reversible** migrations, we use the terms "up" and "down" migrations

- Up: mean forward migration change. For example: Create table, Add Col, Rename Col
- Down: mean reverse migration change, it come in pair with each up version. To rollback the above example, we do: Rename back col, Delete Col, Delete Table

Quiz time:

- Which of the following statements about migrations is FALSE? You can be fast and loose when writing migrations - a bad migration is easy to fix
- Will database migrations often be coupled with application code updates? Yes
- Why are 'good' migrations written in a reversible manner? So that if something goes wrong, the changes can be rolled back

## Lesson 7-8: Up/Down Migration Practice

Lesson 7's Assignment: Just another Alter table, we call these change up migration though.

- Add the BOOLEAN was_successful column to the transactions table.
- Add the TEXT transaction_type column to the transactions table.

```sql
ALTER TABLE transactions
ADD COLUMN was_successful BOOLEAN;

ALTER TABLE transactions
ADD COLUMN transaction_type TEXT;
```

Lesson 8's Assignment: Then imedietly reverse the migration that we just did

- Drop the was_successful column from the transactions table.
- Drop the transaction_type column from the transactions table.

```sql
ALTER TABLE transactions
DROP COLUMN was_successful;

ALTER TABLE transactions
DROP COLUMN transaction_type;
```

```sh
run CH2-L07-L08-UP_DOWN_MIGRATION.sql
```

## Lesson 9: Down Migration Review

Up migration:

```sql
ALTER TABLE transactions
ADD COLUMN was_successful BOOLEAN;

ALTER TABLE transactions
ADD COLUMN transaction_type TEXT;
```

Down migration:

```sql
ALTER TABLE transactions
DROP COLUMN was_successful;

ALTER TABLE transactions
DROP COLUMN transaction_type;
```

Quiz time:

- The second block of code is a down migration because it \_\_\_\_. reverts a previous up migration

## Lesson 10-12: SQL Data Types

SQLite type introduction:

- `NULL` - Null value.
- `INTEGER` - A signed integer stored in 0,1,2,3,4,6, or 8 bytes.
- `REAL` - Floating point value stored as an 64-bit IEEE floating point number.
- `TEXT` - Text string stored using database encoding such as UTF-8
- `BLOB` - Short for Binary large object and typically used for images, audio or other multimedia.
- `BOOLEAN` - Boolean values are written in SQLite queries as `true` or `false`, but are recorded as `1` or `0`.

> SQLite still let you write your queries using boolean expressions and true/false keywords, but it will convert the booleans to integers under-the-hood.

On my side, with PostgreSQL, it too complicated (cover all SQLite provided type plus more) and does support Boolean with `t/f` value (don't expect `1/0` in the record).

Quiz time:

- How is a 'true' boolean value stored and presented in SQLite? 1
- All SQL databases support the same datatypes? False
- What type would you use to store a user's email? TEXT

It quite interesting that I seeing TEXT as a type, normally I will saw `VARCHAR(100)` for specific string length. It also normal for me as a programer to understand the structure that record will be store (eg: 100 bytes for the `VARCHAR(100)` string field), TEXT without any limit literally mean the string is store else where to be, just like BLOB

## Lesson 13: Posts Table

`CREATE TABLE` again, create `posts` table: Prepare for CashPal's latest social media feature named "CashPal Chatter", which aims to revolutionize financial discussions online

```sql
CREATE TABLE post (
-- id
-- image_url
-- description
-- author_id
-- is_sponsored
);
```

Notes: Well, string in PostgreSQL need `''` (single quote) encapsulation. Using `""` is a big no no, we will bee throw with this error

```
psql:CH2-L13-CREATE-3.sql:14: ERROR:  column "posts" does not exist
LINE 1: SELECT * FROM TABLE_INFO("posts");
```

Finish this with new `.sql` file:

- I messed up `author_id` with `TEXT`, just can't see the `id` part
- "For ID columns, assume we can just use INTEGER." here is what the description said

```sh
run CH2-L13-CREATE-3.sql
```

## Lesson 14: Posts Table Migration

`ALTER TALBE` practice: CashPal chatter is a huge hit! After several weeks of use, the engineers at CashPal have decided that some changes need to be made to our posts table

Assignment: Write an up migration for the posts table that achieves the following:

- The author_id column should be renamed to poster_id
- Add a new column named is_edited with a BOOLEAN type
- DROP the is_sponsored column

```sh
run CH2-L14-ALTER_TABLE-2.sql
```
