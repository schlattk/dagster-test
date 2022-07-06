from dagster import job
from dagster_airbyte import airbyte_resource, airbyte_sync_op
from orchestrator_poc.ops.airbyte_ops import sync_google, sync_salesforce, ssh

new_airbyte_resource = airbyte_resource.configured(
    {
        "host": "localhost",
        "port": "8000"
    }
)


@job(resource_defs={"airbyte":new_airbyte_resource})
def run_airbyte():
    ssh()
    
