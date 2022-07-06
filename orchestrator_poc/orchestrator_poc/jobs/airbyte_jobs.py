from dagster import job
from dagster_airbyte import airbyte_resource
from orchestrator_poc.ops.airbyte_ops import sync_google, sync_salesforce, ssh_connection, close_connection

new_airbyte_resource = airbyte_resource.configured(
    {
        "host": "localhost",
        "port": "8000"
    }
)


@job(resource_defs={"airbyte":new_airbyte_resource})
def run_airbyte():
    ssh_connection()
    sync_salesforce()
    close_connection()
