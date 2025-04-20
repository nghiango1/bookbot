-- Drop table if existed
DROP TABLE IF EXISTS users;

-- Create user table
CREATE TABLE users (id INTEGER, name TEXT, age INTEGER);
INSERT into users (id, name, age) values (1, 'John Doe', 21);
INSERT into users (id, name, age) values (2, 1, 33);
SELECT * FROM users;

-- Check type?

SELECT
    column_name,
    data_type,
    character_maximum_length AS max_length,
    character_octet_length AS octet_length
FROM
    information_schema.columns
WHERE
    table_schema = 'public' AND 
    table_name = 'users';
