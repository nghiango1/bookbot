DROP TABLE IF EXISTS transactions;

-- Assignment

CREATE TABLE transactions (
-- id - INTEGER PRIMARY KEY
    id INTEGER PRIMARY KEY,
-- sender_id - INTEGER
    sender_id INTEGER,
-- recipient_id - INTEGER
    recipient_id INTEGER,
-- memo - TEXT - NOT NULL
    memo TEXT NOT NULL,
-- amount - INTEGER - NOT NULL
    amount INTEGER NOT NULL,
-- balance - INTEGER - NOT NULL
    balance INTEGER NOT NULL
);


-- Check
-- PRAGMA TABLE_INFO('transactions');

-- Side quest recheck, fix bug
-- SELECT
--     a.column_name
-- FROM
--     information_schema.key_column_usage AS a
-- JOIN (
--         SELECT
--             *
--         FROM
--             information_schema.table_constraints
--         WHERE
--             table_name = 'transactions'
--     ) AS b
-- ON
--     b.constraint_name = a.constraint_name
-- WHERE
--     a.table_name = 'transactions' AND a.column_name = 'id' AND b.constraint_type = 'PRIMARY KEY';

-- SELECT * FROM QUERY_PRIMARY_KEY('transactions', 'id');
-- SELECT * FROM IS_PRIMARY_KEY('transactions', 'id');

SELECT * FROM TABLE_INFO('transactions');
