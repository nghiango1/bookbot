DROP TABLE IF EXISTS users;

CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  is_admin BOOLEAN
);

-- Assigment: Fix error

INSERT INTO users (
  id,
  name,
  age,
  username,
  password,
  is_admin
) VALUES (
  1,
  'Rudolf',
  33,
  'rudolf1234',
  'thisisnotsecure',
  false
);

INSERT INTO users (
  id,
  name,
  age,
  username,
  password,
  is_admin
) VALUES (
  2,
  'Jerry',
  25,
  'jerrysmith',
  'mypasswordis1234',
  true
);

-- Check result

SELECT * FROM users;
