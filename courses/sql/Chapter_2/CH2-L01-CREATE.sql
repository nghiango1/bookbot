-- Drop if table existed
DROP TABLE IF EXISTS people;

-- Assignment
CREATE TABLE people (
    -- `id` - Integer
    id INTEGER,
    -- `tag` - Text
    tag TEXT,
    -- `name` - Text
    name TEXT,
    -- `age` - Integer
    age INTEGER,
    -- `balance` - Integer
    balance INTEGER,
    -- `is_admin` - boolean
    is_admin BOOLEAN
);

-- We doesn't have this in postgres though
-- PRAGMA TABLE_INFO('people')
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
    table_name = 'people'
ORDER BY cid;
