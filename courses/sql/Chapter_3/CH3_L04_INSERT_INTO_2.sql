DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS countries;

-- PRAGMA foreign_keys = ON;

CREATE TABLE countries(code TEXT PRIMARY KEY, name TEXT);

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

INSERT INTO countries (
  code,
  name
) VALUES (
  'US',
  'United States of America'
);

INSERT INTO countries (
  code,
  name
) VALUES (
  'IN',
  'India'
);


-- Assigment: Fix error

INSERT INTO users (
  id,
  name,
  country_code
) VALUES (
  1,
  'Jerry',
  'US'
);

INSERT INTO users (
  id,
  name,
  country_code
) VALUES (
  2,
  'Amit',
  'IN'
);

-- Check result

SELECT * FROM users;
