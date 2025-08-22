--EXERCISE 12
SELECT
    population,
    length(population::TEXT) AS length
    FROM countries;

--EXERCISE 15
UPDATE countries
SET iso_code=UPPER(LEFT(country_name,3))
WHERE iso_code IS NULL;

--EXERCISE 14
SELECT
    peak_name,
    RIGHT(peak_name,4) AS positive_right,
    substring(peak_name, 5, length(peak_name)) AS negative_right
    FROM peaks;

--EXERCISE 7
SELECT
    capital,
    translate(capital,'áãåçéíñóú', 'aaaceinou') AS translated_name
    FROM countries;
