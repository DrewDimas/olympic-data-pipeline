SELECT 
    REPLACE(Country, '*', '') AS team,
    NOC as noc
FROM {{ ref('noc_code_lookup') }}