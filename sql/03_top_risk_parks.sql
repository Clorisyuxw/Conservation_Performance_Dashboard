SELECT
    [Park Name],
    COUNT(*) AS Protected_Species_Count
FROM species
WHERE [Conservation Status]
IN (
    'Endangered',
    'Threatened',
    'Species of Concern',
    'Proposed Endangered',
    'Proposed Threatened'
)
GROUP BY [Park Name]
ORDER BY Protected_Species_Count DESC
LIMIT 10;