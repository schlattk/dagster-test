from dagster import job
from dagster_airbyte import airbyte_resource, airbyte_sync_op
from dagster_dbt import dbt_run_op
from orchestrator_poc.jobs.dbt_jobs import test_dbt_rpc_sync_resource
from orchestrator_poc.ops.airbyte_ops import sync_salesforce, sync_salesforce_fund

new_airbyte_resource = airbyte_resource.configured(
    {
        "host": { "env": "AIRBYTE_HOST" },
        "port": { "env": "AIRBYTE_PORT" },
    }
)

@job(resource_defs={"airbyte":new_airbyte_resource})
def run_salesforces_stronger_nudge():
    sync_salesforce()

@job(resource_defs={"airbyte":new_airbyte_resource})
def run_salesforce_fund():
    sync_salesforce_fund()

@job(resource_defs={"airbyte":new_airbyte_resource, "dbt": test_dbt_rpc_sync_resource})
def run_airbyte_and_then_dbt_cli():
    dbt_run_op(start_after=[sync_salesforce(start_after=[sync_salesforce_fund()])])

@job(resource_defs={"airbyte":new_airbyte_resource, "dbt": test_dbt_rpc_sync_resource})
def run_airbyte_and_then_dbt_cli_new():
    sync_salesforce(sync_salesforce_fund())
