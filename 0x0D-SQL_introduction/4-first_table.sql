-- creating table called first_table in current database in my MySQL.
-- database name will be passed as argument of mysql command
-- first_table description:
--             id INT
--             name VARCHAR(256)
-- The database name Will passed as argument of mysql command
-- If the table first_table already exists, your script should not fail
-- You are not allowed to use the SELECT or SHOW statements

CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
