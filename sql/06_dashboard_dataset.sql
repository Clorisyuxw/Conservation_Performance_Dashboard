SELECT
    p.[Park Name],
    p.State,

    COUNT(
        CASE
            WHEN s.[Conservation Status]
            IN (
                'Endangered',
                'Threatened',
                'Species of Concern',
                'Proposed Endangered',
                'Proposed Threatened'
            )
            THEN 1
        END
    ) AS Protected_Species_Count,

    SUM(
        CASE
            WHEN s.[Conservation Status] = 'Endangered' THEN 5
            WHEN s.[Conservation Status] = 'Threatened' THEN 4
            WHEN s.[Conservation Status] = 'Proposed Endangered' THEN 4
            WHEN s.[Conservation Status] = 'Proposed Threatened' THEN 3
            WHEN s.[Conservation Status] = 'Species of Concern' THEN 2
            ELSE 0
        END
    ) AS Risk_Score

FROM species s

JOIN parks p
ON s.[Park Name] = p.[Park Name]

GROUP BY
    p.[Park Name],
    p.State

ORDER BY Risk_Score DESC;