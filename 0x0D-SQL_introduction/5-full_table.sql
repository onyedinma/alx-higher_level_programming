<<<<<<< HEAD
-- Here's a script that prints the full description of the table first_table in the hbtn_0c_0 database:

SELECT CONCAT('Table: ', TABLE_NAME, '\n\n', 'Create Table: ', CREATE_STATEMENT, '\n', ENGINE, ' ', CHARSET, '\n')
FROM information_schema.tables
WHERE TABLE_SCHEMA = 'hbtn_0c_0'
AND TABLE_NAME = 'first_table';


=======
-- print full description of the table first_table
-- from the database hbtn_0c_0
SHOW CREATE TABLE first_table;
>>>>>>> af956157b46d2d02a78f90c00b0f4dfc6ce4d9d2
