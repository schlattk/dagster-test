from dagster import job
from dagster_airbyte import airbyte_resource, airbyte_sync_op
from orchestrator_poc.ops.airbyte_ops import sync_google, sync_salesforce, airbyte_ssh, ssh

new_airbyte_resource = airbyte_resource.configured(
    {
        "host": { "env": "AIRBYTE_HOST" },
        "port": { "env": "AIRBYTE_PORT" },
    }
)


@job(resource_defs={"airbyte":new_airbyte_resource})
def run_airbyte():
    airbyte_ssh()

@job(resource_defs={"airbyte":new_airbyte_resource})
def run_dagster_airbyte():
    sync_salesforce()
