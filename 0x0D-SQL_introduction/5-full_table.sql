-- Here's a script that prints the full description of the table first_table in the hbtn_0c_0 database:

SELECT column_name, data_type, character_maximum_length, is_nullable, column_default
FROM information_schema.columns
WHERE table_schema = 'hbtn_0c_0' AND table_name = 'first_table';

