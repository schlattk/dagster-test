from dagster import job
from dagster_airbyte import airbyte_resource, airbyte_sync_op
from dagster_dbt import dbt_rpc_run
from orchestrator_poc.jobs.dbt_jobs import test_dbt_rpc_resource, test_dbt_rpc_sync_resource, run_dbt_job
from orchestrator_poc.ops.airbyte_ops import sync_google, sync_salesforce, airbyte_ssh, ssh

new_airbyte_resource = airbyte_resource.configured(
    {
        "host": { "env": "AIRBYTE_HOST" },
        "port": { "env": "AIRBYTE_PORT" },
    }
)

run_staging_models = dbt_rpc_run.configured(
{"models": ["staging"]},
name="dbt_test_model",
)

@job(resource_defs={"airbyte":new_airbyte_resource})
def run_airbyte():
    airbyte_ssh()

@job(resource_defs={"airbyte":new_airbyte_resource})
def run_dagster_airbyte():
    sync_salesforce()

@job(resource_defs={"airbyte":new_airbyte_resource, "dbt": test_dbt_rpc_sync_resource})
def run_airbyte_dbt():
    sync_salesforce()
