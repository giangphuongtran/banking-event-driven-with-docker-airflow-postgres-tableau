{{ config(materialized='view') }}

select
v:id::string as transaction_id,
v:account_id::string as account_id,
v:amount::float as amount,
v:related_account_id::string as related_account_id,
v:transaction_type::string as transaction_type,
v:status::string as status,
v:transaction_date::timestamp as transaction_date,
v:description::string as description,
current_timestamp() as load_timestamp
from {{ source('raw', 'transactions') }}