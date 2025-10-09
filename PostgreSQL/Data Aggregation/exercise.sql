-- language: PLpgSQL
--EXERCISE 18
CREATE VIEW view_performance_rating AS
    SELECT
        first_name,
        last_name,
        job_title,
        salary,
        department_id,
        CASE
            WHEN salary>=25000 AND job_title LIKE 'Senior%' THEN 'High-performing Senior'
            WHEN salary>=25000 AND job_title NOT LIKE 'Senior%' THEN 'High-performing Employee'
            ELSE 'Average-performing'
        END AS performance_rating
    FROM employees;

--EXERCISE 17
SELECT
    department_id,
    count(department_id) AS num_employees,
    CASE
        WHEN AVG(salary) > 50000 THEN 'Above average'
        ELSE 'Below average'
    END AS salary_level
FROM employees
GROUP BY department_id
HAVING AVG(salary) > 30000
ORDER BY department_id;

--EXERCISE 16
SELECT
    project_name,
    CASE
        WHEN start_date IS NULL AND end_date IS NULL THEN 'Ready for development'
        WHEN end_date IS NULL THEN 'In Progress'
        ELSE 'Done'
    END AS project_status
FROM projects
WHERE project_name LIKE '%Mountain%';

--EXERCISE 14
UPDATE employees
SET salary =
    CASE
        WHEN hire_date<'2015-01-16' THEN salary+2500
        WHEN hire_date<'2020-03-04' THEN salary+1500
    END,

    job_title =
    CASE
        WHEN hire_date<'2015-01-16' THEN concat('Senior ', job_title)
        WHEN hire_date<'2020-03-04' THEN concat('Mid-', job_title)
    END
WHERE hire_date<'2020-03-04';

--EXERCISE 13
SELECT
	count(CASE WHEN department_id=1 THEN 1 END) AS Engineering,
	count(CASE WHEN department_id=2 THEN 1 END) AS "Tool Design",
	count(CASE WHEN department_id=3 THEN 1 END) AS Sales,
	count(CASE WHEN department_id=4 THEN 1 END) AS Marketing,
	count(CASE WHEN department_id=5 THEN 1 END) AS Purchasing,
	count(CASE WHEN department_id=6 THEN 1 END) AS "Research and Development",
	count(CASE WHEN department_id=7 THEN 1 END) AS Production
FROM employees;
