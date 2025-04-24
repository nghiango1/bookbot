DROP TABLE IF EXISTS users;

-- Assignment

CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country_code TEXT NOT NULL,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    is_admin BOOLEAN
);

-- PRAGMA TABLE_INFO('users');
-- New infomation table for PRIMARY KEY constaint
SELECT
    a.column_name
FROM
    information_schema.key_column_usage AS a
JOIN (
        SELECT
            *
        FROM
            information_schema.table_constraints
        WHERE
            table_name = 'users'
    ) AS b
ON
    b.constraint_name = a.constraint_name
WHERE
    a.table_name = 'users' AND a.column_name = 'id' AND b.constraint_type = 'PRIMARY KEY';

-- Side quest: Using new table infomation and update into TABLE_INFO query
-- SELECT * FROM QUERY_PRIMARY_KEY('users', 'id');
-- SELECT * FROM IS_PRIMARY_KEY('users', 'id');
SELECT * FROM TABLE_INFO('users');
