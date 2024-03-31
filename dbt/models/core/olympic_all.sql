{{ config(
    materialized='table',
   ) }}
WITH male_athletes AS (
    SELECT 
        name,
        sex,
        CAST(age AS INT64) AS age,
        CAST(height AS INT64) AS height,
        CAST(weight AS INT64) AS weight,
        team,
        noc,
        games,
        year,
        season,
        city,
        sport,
        event,
        medal,
        sex_index,
        season_index
    FROM {{ ref('stg_olympic_data_male') }}
),

female_athletes AS (
    SELECT 
        name,
        sex,
        CAST(age AS INT64) AS age,
        CAST(height AS INT64) AS height,
        CAST(weight AS INT64) AS weight,
        team,
        noc,
        games,
        year,
        season,
        city,
        sport,
        event,
        medal,
        sex_index,
        season_index
    FROM {{ ref('stg_olympic_data_female') }}
),

union_athletes AS (
    SELECT * FROM male_athletes
    UNION ALL
    SELECT * FROM female_athletes
)

SELECT 
    name,
    sex,
    age,
    height AS height_cm,
    weight AS weight_kg,
    team,
    noc,
    games,
    year,
    season,
    city,
    sport,
    event,
    medal,
    sex_index,
    season_index,
    CONCAT(
        CAST(FLOOR((CAST(height AS FLOAT64) * 0.393701) / 12) AS STRING), ' ft ',
        CAST(ROUND(((CAST(height AS FLOAT64) * 0.393701) - FLOOR((CAST(height AS FLOAT64) * 0.393701) / 12) * 12), 0) AS STRING), ' in'
    ) AS height_ft_in,
    ROUND(CAST(weight AS FLOAT64) * 2.20462, 2) AS weight_lb -- Conversion from kg to pounds
FROM union_athletes
