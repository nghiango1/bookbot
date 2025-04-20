-- Drop if table existed
DROP TABLE IF EXISTS transactions;

-- Assignment
CREATE TABLE transactions (
    -- `id` - Integer
    id INTEGER,
    -- `recipient_id` - Integer
    recipient_id INTEGER,
    -- `sender_id` - Integer
    sender_id INTEGER,
    -- `note` - Text
    note TEXT,
    -- `amount` - Integer
    amount INTEGER
);

-- We doesn't have this in postgres though
-- PRAGMA TABLE_INFO('transactions')
-- Still, we can recreate all the field just like in SQLite
-- cid	name	type	notnull	dflt_value	pk

SELECT 
    ordinal_position - 1 as cid,
    column_name as name,
    upper(data_type) as type,
    CAST (is_nullable = 'NO' AS INTEGER) as notnull,
    -- dflt_value mean default value
    column_default as dflt_value,
    CAST (is_identity <> 'NO' AS INTEGER) as pk
FROM
    information_schema.columns
WHERE
    table_name = 'transactions'
ORDER BY cid;
