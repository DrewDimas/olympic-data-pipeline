with 

source as (

    select * from {{ source('olympic_data', 'male_data') }}

),

olympic_male as (

    select
        name,
        sex,
        age,
        height,
        weight,
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

    from source

)

select * from olympic_male

