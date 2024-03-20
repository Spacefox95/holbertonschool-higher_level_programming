 -- Create a new table 'force_name' on MySQL server if it does not exist
CREATE TABLE IF NOT EXISTS force_name (
    -- id column : type INT
    id INT,
    -- name column : type VARCHAR(256), cannot be NULL
    name VARCHAR(256) NOT NULL
);