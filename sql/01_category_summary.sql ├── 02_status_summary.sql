SELECT
    Category,
    COUNT(*) AS Species_Count
FROM species
GROUP BY Category
ORDER BY Species_Count DESC;