DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
    -- id
    id INTEGER,
    -- image_url
    image_url TEXT,
    -- description
    description TEXT,
    -- author_id
    author_id INTEGER,
    -- is_sponsored
    is_sponsored BOOLEAN
);


SELECT * FROM TABLE_INFO('posts');
