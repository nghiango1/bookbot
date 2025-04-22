DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
    id INTEGER,
    image_url TEXT,
    description TEXT,
    author_id INTEGER,
    is_sponsored BOOLEAN
);

-- Assigment
-- The author_id column should be renamed to poster_id
ALTER TABLE posts
RENAME COLUMN author_id TO poster_id;

-- Add a new column named is_edited with a BOOLEAN type
ALTER TABLE posts
ADD COLUMN is_edited BOOLEAN;

-- DROP the is_sponsored column
ALTER TABLE posts
DROP COLUMN is_sponsored;

-- Recheck result
SELECT * FROM TABLE_INFO('posts');
