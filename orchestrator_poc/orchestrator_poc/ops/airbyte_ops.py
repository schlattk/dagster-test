from dagster_airbyte import airbyte_sync_op

sync_google = airbyte_sync_op.configured(
    {"connection_id": "some-connection-id"},
    name="google"
)
