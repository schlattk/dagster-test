from dagster import op
from dagster_airbyte import airbyte_sync_op

sync_salesforce = airbyte_sync_op.configured(
    {"connection_id": "c1a5fdf3-903f-4d86-8601-5b6462afe40e"},
    name="salesforce_stronger_nudge"
)

sync_salesforce_fund = airbyte_sync_op.configured(
    {"connection_id": "dd66a499-7881-4e08-a63a-21dc63925ebb"},
    name="salesforce_fund"
)
