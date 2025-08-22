--EXERCISE 1
SELECT * FROM cities
ORDER BY id;

--EXERCISE 2
SELECT concat(name, ' ' ,state) AS cities_information,
       area AS area_km2
    FROM cities;

--EXERCISE 3
SELECT
        DISTINCT name,
        area AS area_km2
    FROM cities
ORDER BY name DESC;

--EXERCISE 4
SELECT
    id,
    concat(first_name, ' ', last_name) AS full_name,
    job_title
FROM employees
ORDER BY first_name
LIMIT 50;

--EXERCISE 5
SELECT
    id AS id,
    concat(first_name, ' ', middle_name, ' ', last_name) AS full_name,
    hire_date
FROM employees
ORDER BY hire_date
OFFSET 9;

--EXERCISE 6
SELECT
    id,
    concat(number, ' ', street) AS adress,
    city_id
    FROM addresses
WHERE id >= 20;

--EXERCISE 7
SELECT
    concat(number, ' ', street) AS adress,
    city_id
    FROM addresses
WHERE city_id%2=0 AND city_id>=0
ORDER BY city_id;

--EXERCISE 8
SELECT
    name,
    start_date,
    end_date
    FROM projects
WHERE start_date>='2016-06-01 07:00:00' AND end_date<'2023-06-04 00:00:00'
ORDER BY start_date;

--EXERCISE 9
SELECT
    number,
    street
    FROM addresses
WHERE id BETWEEN 50 AND 100 OR number < 1000;

--EXERCISE 10
SELECT
    employee_id,
    project_id
    FROM employees_projects
WHERE employee_id IN (200, 250) AND project_id NOT IN (50, 100);

--EXERCISE 11
SELECT
    name,
    start_date
    FROM projects
WHERE name IN ('Mountain', 'Road', 'Touring')
LIMIT 20;

--EXERCISE 12
SELECT
    concat(first_name,' ', last_name) AS full_name,
    job_title,
    salary
FROM employees
WHERE salary IN (12500, 14000, 23600, 25000)
ORDER BY salary DESC;

--EXERCISE 13
SELECT
    id,
    first_name,
    last_name
FROM employees
WHERE middle_name IS NULL
LIMIT 3;

--EXERCISE 14
INSERT INTO departments(department, manager_id)
VALUES ('Finance', 3),

('Information Services', 42),

('Document Control', 90),

('Quality Assurance', 274),

('Facilities and Maintenance', 218),

('Shipping and Receiving', 85),

('Executive', 109);

--EXERCISE 15
CREATE TABLE company_chart AS
    SELECT
        concat(first_name,' ', last_name) AS full_name,
        job_title,
        department_id,
        manager_id
        FROM employees;

--EXERCISE 16
UPDATE projects
SET end_date=start_date+ INTERVAL '5 months'
WHERE end_date IS NULL;

--EXERCISE 17
UPDATE employees
SET salary=salary+1500,
    job_title=concat('Senior ',job_title)
WHERE hire_date BETWEEN 'January 1, 1998' AND 'January 5, 2000';

--EXERCISE 18
DELETE FROM addresses
WHERE city_id IN (5, 17, 20, 30);

--EXERCISE 19
CREATE VIEW view_company_chart AS
    SELECT
        full_name,
        job_title
        FROM company_chart
    WHERE manager_id=184;

--EXERCISE 20
CREATE VIEW view_addresses AS
    SELECT
        concat(e.first_name,' ', e.last_name) AS full_name,
        e.department_id,
        concat(a.number, ' ', a.street) AS address
        FROM employees AS e, addresses AS a
    WHERE e.address_id=a.id
    ORDER BY address;

--EXERCISE 21
ALTER VIEW view_addresses
RENAME TO view_employee_addresses_info;

--EXERCISE 22
DROP VIEW view_company_chart;

--EXERCISE 23
UPDATE projects
SET name = upper(name);

--EXERCISE 24
CREATE VIEW view_initials AS
    SELECT
        LEFT(first_name,2) AS initial,
        last_name
        FROM employees
    ORDER BY last_name;

--EXERCISE 25
SELECT
    name,
    start_date
    FROM projects
WHERE starts_with(name, 'MOUNT')
ORDER BY id;










