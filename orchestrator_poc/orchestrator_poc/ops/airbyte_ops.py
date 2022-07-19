from dagster import op
from dagster_airbyte import airbyte_sync_op
import paramiko

sync_salesforce = airbyte_sync_op.configured(
    {"connection_id": "c1a5fdf3-903f-4d86-8601-5b6462afe40e"},
    name="salesforce_stronger_nudge"
)
