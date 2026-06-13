SELECT
    [Conservation Status],
    COUNT(*) AS Record_Count
FROM species
GROUP BY [Conservation Status]
ORDER BY Record_Count DESC;