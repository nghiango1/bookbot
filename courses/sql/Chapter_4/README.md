# Chapter 4: CRUD

## Lesson 1: CRUD

Stands for `CREATE`, `READ`, `UPDATE`, and `DELETE`. It goes nicely with HTTP

- HTTP POST - CREATE
- HTTP GET - READ
- HTTP PUT - UPDATE
- HTTP DELETE - DELETE

> Ruby on Rails tutorial will walk through the whole process to create CRUD app, with the help of Rails Route generator/Database migration tool to ship app quickly

Assignment: READ the `crud` table

```sh
# Remember our `run` is an alias for `sudo -u postgres psql -d localdb -f `

# Which run as `postgres` user
# Connect to the postgres local database instance using `psql` command
# Specify "user" created database `localdb`
# Running sql file through `-f ` agrument
source ../.alias

run CH4_L01_READ.sql
```

> I just speed ran through this chapter from now on tbh. I list some problem I faced here

## Lesson 2: Insert Statement

I missed boolean, which set value to 'false' may not auto cast it back to correct type

## Lesson 5: Auto incremental `id`

Won't work on Postgres, need additional setup which is quite complex
