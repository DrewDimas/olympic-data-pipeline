WITH medal_records AS (
    SELECT
        year,
        season,
        noc,
        team,
        sport,
        CASE
            WHEN medal IN ('Gold', 'Silver', 'Bronze') THEN 1
            ELSE 0
        END AS is_medal
    FROM {{ ref('olympic_all') }}
)

SELECT
    year,
    season,
    noc,
    team,
    sport,
    COUNT(is_medal) AS medal_count
FROM medal_records
WHERE is_medal = 1
GROUP BY
    year,
    season,
    noc,
    team,
    sport
ORDER BY
    year,
    season,
    noc,
    team,
    sport
