# Chapter 2: Table

## Lession 1: Creating a table

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

## Lession 2: Creating table practice

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
