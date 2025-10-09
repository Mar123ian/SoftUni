-- language: PLpgSQL
--EXERCISE 14
SELECT
    mountain_range,
    peak_name,
    elevation
FROM mountains AS m JOIN peaks AS p ON m.id = p.mountain_id
WHERE mountain_range='Rila'
ORDER BY elevation DESC;

--EXERCISE 15
SELECT
    count(*) AS countries_without_rivers
FROM countries AS c LEFT JOIN countries_rivers AS cr ON c.country_code=cr.country_code
WHERE river_id IS NULL;

--EXERCISE 13
CREATE TABLE customers (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    customer_name VARCHAR
);

CREATE TABLE contacts(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    contact_name VARCHAR,
    phone VARCHAR,
    email VARCHAR,
    customer_id INT REFERENCES customers ON DELETE SET NULL ON UPDATE CASCADE
);

INSERT INTO customers(customer_name)
VALUES ('BlueBird Inc'),
       ('Dolphin LLC');

INSERT INTO contacts(contact_name, phone, email, customer_id)
VALUES ('John Doe','(408)-111-1234',	'john.doe@bluebird.dev',	1),
       ('Jane Doe','(408)-111-1235',	'jane.doe@bluebird.dev',	1),
       ('David Wright','(408)-222-1234',	'david.wright@dolphin.dev',	2);

DELETE FROM customers
WHERE id=1;

--EXERCISE 8
CREATE TABLE students(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    student_name VARCHAR
);

CREATE TABLE exams(
    id INT GENERATED ALWAYS AS IDENTITY (START WITH 101) PRIMARY KEY,
    exam_name VARCHAR
);

CREATE TABLE students_exams(
    student_id INT REFERENCES students,
    exam_id INT REFERENCES exams
);

CREATE TABLE study_halls(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    study_hall_name VARCHAR,
    exam_id INT REFERENCES exams
);

INSERT INTO students(student_name)
VALUES ('Mila'),
       ('Toni'),
       ('Ron');

INSERT INTO exams(exam_name)
VALUES ('Python Advanced'),
       ('Python OOP'),
       ('PostgreSQL');

INSERT INTO students_exams(student_id, exam_id)
VALUES (1,101),
       (1,102),
       (2,101),
       (3, 103),
       (2,102),
       (2,103);

INSERT INTO study_halls(study_hall_name, exam_id)
VALUES ('Open Source Hall',102),
       ('Inspiration Hall',101),
       ('Creative Hall',103),
       ('Masterclass Hall', 103),
       ('Information Security Hall',103);
