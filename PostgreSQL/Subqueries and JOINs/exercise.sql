--EXERCISE 20
WITH row_number AS(
    SELECT
    *,
    row_number()  over (PARTITION BY c.country_code ORDER BY elevation DESC,country_name ) AS rn
    FROM countries AS c
    LEFT JOIN mountains_countries AS mc ON c.country_code=mc.country_code
    LEFT JOIN mountains AS m ON mc.mountain_id=m.id
    LEFT JOIN peaks AS p ON p.mountain_id=m.id

)

SELECT
    country_name ,
    coalesce(peak_name,'(no highest peak)') AS highest_peak_name,
    coalesce(elevation,0) AS highest_peak_elevation,
    CASE
        WHEN coalesce(elevation,0)=0 THEN '(no mountain)'
        ELSE mountain_range
    END AS mountain
FROM row_number
WHERE rn=1
ORDER BY country_name;

--EXERCISE 19
CREATE VIEW continent_currency_usage AS
    SELECT co.continent_code,
           cntr.currency_code,
           count(*) AS currency_usage

    FROM continents AS co
    JOIN countries AS cntr ON co.continent_code = cntr.continent_code
    GROUP BY co.continent_code, cntr.currency_code
    HAVING count(*) >1;

SELECT * FROM continent_currency_usage
ORDER BY currency_usage DESC;

--EXERCISE 14
WITH continents_avg_area AS (SELECT
    continent_code,
    avg(area_in_sq_km) as avg_area
FROM countries
GROUP BY continent_code)

SELECT
    min(avg_area) as min_average_area
FROM continents_avg_area;

