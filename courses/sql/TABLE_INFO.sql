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
        (is_identity <> 'NO')::INTEGER as pk
    FROM
        information_schema.columns
    WHERE
        table_name = p_table_name
    ORDER BY cid;
END;
$$ LANGUAGE plpgsql;
