DROP TABLE IF EXISTS users;

CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country_code TEXT NOT NULL,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  is_admin BOOLEAN
);

-- Assignment

-- Record 1
-- 
--     id: 1
--     name: David
--     age: 34
--     country_code: US
--     username: DavidDev
--     password: insertPractice
--     is_admin: false

INSERT INTO users (id, name, age, country_code, username, password, is_admin)
VALUES (1, 'David', 34, 'US', 'DavidDev', 'insertPractice', false);

-- Record 2
-- 
--     id: 2
--     name: Samantha
--     age: 29
--     country_code: BR
--     username: Sammy93
--     password: addingRecords!
--     is_admin: false

INSERT INTO users (id, name, age, country_code, username, password, is_admin)
VALUES (2, 'Samantha', 29, 'BR', 'Sammy93', 'addingRecords!', false);


-- check
SELECT * FROM users;
