from dagster import job
from dagster_dbt import dbt_rpc_resource, dbt_run_op, dbt_rpc_sync_resource, dbt_rpc_run
from orchestrator_poc.ops.dbt_ops import run_dbt_op

test_dbt_rpc_resource = dbt_rpc_resource.configured({
    "host": { "env": "DBT_HOST" },

})

test_dbt_rpc_sync_resource = dbt_rpc_sync_resource.configured({
    "host": { "env": "DBT_HOST" }
})


@job(resource_defs={ "dbt_rpc": test_dbt_rpc_sync_resource })
def run_dbt_job():
    dbt_run_op()
