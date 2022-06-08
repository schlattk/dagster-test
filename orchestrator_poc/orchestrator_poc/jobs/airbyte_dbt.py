from dagster import job
from orchestrator_poc.jobs.airbyte_jobs import new_airbyte_resource
from orchestrator_poc.ops.airbyte_ops import sync_google
from orchestrator_poc.jobs.dbt_jobs import dbt_cli_resource
from dagster_dbt import dbt_run_op


@job(resource_defs={"airbyte":new_airbyte_resource, "dbt":dbt_cli_resource})
def run_airbyte_dbt():
    dbt_run_op(sync_google())
