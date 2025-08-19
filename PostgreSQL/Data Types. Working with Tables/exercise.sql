--EXERCISE 0
CREATE DATABASE minions_db;

--EXERCISE 1
CREATE TABLE minions (
	id SERIAL PRIMARY KEY,
	name VARCHAR(30),
	age INT
);

--EXERCISE 2
ALTER TABLE minions
RENAME TO minions_info;

--EXERCISE 3
ALTER TABLE minions_info
ADD COLUMN code CHAR(4);
ALTER TABLE minions_info
ADD COLUMN task TEXT;
ALTER TABLE minions_info
ADD COLUMN salary DECIMAL(8,3);

--EXERCISE 4
ALTER TABLE minions_info
RENAME COLUMN salary TO banana;

--EXERCISE 5
ALTER TABLE minions_info
ADD COLUMN email VARCHAR(20);
ALTER TABLE minions_info
ADD COLUMN equipped BOOLEAN NOT NULL;

--EXERCISE 6
CREATE TYPE type_mood AS ENUM ('happy', 'relaxed', 'stressed', 'sad');
ALTER TABLE minions_info
ADD COLUMN mood type_mood;

--EXERCISE 7
ALTER TABLE minions_info
ALTER COLUMN age SET DEFAULT 0;
ALTER TABLE minions_info
ALTER COLUMN name SET DEFAULT '';
ALTER TABLE minions_info
ALTER COLUMN code SET DEFAULT '';

--EXERCISE 8
ALTER TABLE minions_info
ADD CONSTRAINT unique_containt UNIQUE(email,id);
ALTER TABLE minions_info
ADD CONSTRAINT banana_check CHECK(banana>0);

--EXERCISE 9
ALTER TABLE minions_info
ALTER COLUMN task TYPE VARCHAR(150);

--EXERCISE 10
ALTER TABLE minions_info
ALTER COLUMN equipped 
DROP NOT NULL;

--EXERCISE 11
ALTER TABLE minions_info
DROP COLUMN age;

--EXERCISE 12
CREATE TABLE minions_birthdays (
	id INT NOT NULL PRIMARY KEY,
	name VARCHAR(50),
	date_of_birth DATE,
	age INT,
	present VARCHAR(100),
	party TIMESTAMPTZ
);

--EXERCISE 13
INSERT INTO minions_info(name, code, task, banana, email, equipped, mood)
VALUES 
('Mark', 'GKYA', 'Graphing Points', 3265.265, 'mark@minion.com', false, 'happy'),
('Mel', 'HSK', 'Science Investigation', 54784.996, 'mel@minion.com', true, 'stressed'),
('Bob', 'HF', 'Painting', 35.652, 'bob@minion.com', true, 'happy'),
('Darwin', 'EHND', 'Create a Digital Greeting', 321.958, 'darwin@minion.com', false, 'relaxed'),
('Kevin', 'KMHD', 'Construct with Virtual Blocks', 35214.789, 'kevin@minion.com', false, 'happy'),
('Norbert', 'FEWB', 'Testing', 3265.500, 'norbert@minion.com', true, 'sad'),
('Donny', 'L', 'Make a Map', 8.452, 'donny@minion.com', true, 'happy');

--EXERCISE 14
SELECT name, task, email, banana FROM minions_info;

--EXERCISE 15
TRUNCATE minions_info;

--EXERCISE 16
DROP TABLE minions_birthdays;

--EXERCISE 17
DROP DATABASE minions_db;
