-- Drop if table existed
DROP TABLE IF EXISTS people;
DROP TABLE IF EXISTS users;

CREATE TABLE people (
  id INTEGER,
  tag TEXT,
  name TEXT,
  age INTEGER,
  balance INTEGER,
  is_admin BOOLEAN
);


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

-- We doesn't have this in postgres though, use our alternative function instead
-- PRAGMA TABLE_INFO('transactions')
SELECT * FROM TABLE_INFO('users');
