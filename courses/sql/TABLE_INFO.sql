DROP FUNCTION IF EXISTS QUERY_PRIMARY_KEY(TEXT,TEXT);
DROP FUNCTION IF EXISTS IS_PRIMARY_KEY(TEXT,TEXT);
DROP FUNCTION IF EXISTS TABLE_INFO(TEXT);

-- Create function to query if exist a record for PRIMARY_KEY constants of table_name, column_name
CREATE OR REPLACE FUNCTION QUERY_PRIMARY_KEY(p_table_name TEXT, p_column_name TEXT)
RETURNS TABLE (
    col_name TEXT
) AS $$
BEGIN
    RETURN QUERY 
    SELECT
        a.column_name::TEXT as col_name
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
        a.table_name = p_table_name AND a.column_name = p_column_name AND b.constraint_type = 'PRIMARY KEY';
END;
$$ LANGUAGE plpgsql;

-- Convert above query to a boolean value
CREATE OR REPLACE FUNCTION IS_PRIMARY_KEY(p_table_name TEXT, p_column_name TEXT)
RETURNS BOOLEAN AS $$
DECLARE 
    is_pk BOOLEAN;
BEGIN
    SELECT EXISTS (
        SELECT * FROM QUERY_PRIMARY_KEY(p_table_name, p_column_name)
    ) INTO is_pk;

    RETURN is_pk;
END
$$ LANGUAGE plpgsql;

-- Update table_info to also include PRIMARY_KEY infomation
CREATE OR REPLACE FUNCTION TABLE_INFO(p_table_name TEXT)
RETURNS TABLE (
    cid INTEGER,
    name TEXT,
    type TEXT,
    notnull INTEGER,
    dflt_value TEXT,
    pk INTEGER
) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        ordinal_position - 1 as cid,
        column_name::TEXT as name,
        upper(data_type) as type,
        (is_nullable = 'NO')::INTEGER as notnull,
        column_default::TEXT as dflt_value,
        IS_PRIMARY_KEY(p_table_name, column_name)::INTEGER AS pk 
    FROM
        information_schema.columns
    WHERE
        table_name = p_table_name
    ORDER BY cid;
END;
$$ LANGUAGE plpgsql;
