{{ config(
    materialized='table',
    partition_by={
        "field": "year",
        "data_type": "int64",
        "range": {
            "start": 1896,
            "end": 2016,
            "interval": 1
        }
    },
    cluster_by=['noc', 'season', 'sport']
) }}

SELECT *
FROM {{ ref('olympic_all') }}


