from dagster import job, graph
from dagster_airbyte import airbyte_resource, airbyte_sync_op
from dagster_dbt import dbt_rpc_run
from orchestrator_poc.jobs.dbt_jobs import test_dbt_rpc_resource, test_dbt_rpc_sync_resource, run_dbt_rpc_sync_job, test_dbt_cli_resource
from orchestrator_poc.ops.airbyte_ops import sync_google, sync_salesforce, airbyte_ssh, ssh
from orchestrator_poc.ops.dbt_ops import dbt_rpc_op, dbt_rpc_run_op, dbt_op

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

@graph
def run_dbt_after_airbyte():
    dbt_rpc_run_op(start=sync_salesforce())

@job(resource_defs={"airbyte":new_airbyte_resource})
def run_dagster_airbyte():
    sync_salesforce()

@job(resource_defs={"airbyte":new_airbyte_resource, "dbt_rpc": test_dbt_rpc_sync_resource})
def run_airbyte_and_then_dbt():
    dbt_rpc_op(start_after=sync_salesforce())
    # run_dbt_after_airbyte()

@job(resource_defs={"airbyte":new_airbyte_resource, "dbt": test_dbt_rpc_sync_resource})
def run_airbyte_and_then_dbt_cli():
    dbt_op(start_after=sync_salesforce())
    # run_dbt_after_airbyte()
