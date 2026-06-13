SELECT
    p.State,
    COUNT(*) AS Protected_Species_Count
FROM species s
JOIN parks p
ON s.[Park Name] = p.[Park Name]
WHERE s.[Conservation Status] IN (
    'Endangered',
    'Threatened',
    'Species of Concern',
    'Proposed Endangered',
    'Proposed Threatened'
)
GROUP BY p.State
ORDER BY Protected_Species_Count DESC;