from dagster import job
from dagster_dbt import dbt_rpc_resource, dbt_run_op, dbt_rpc_sync_resource, dbt_rpc_run
from orchestrator_poc.ops.dbt_ops import dbt_run_ssh

test_dbt_rpc_resource = dbt_rpc_resource.configured({
    "host": { "env": "DBT_HOST" },
    "port": { "env": "DBT_PORT" }
})

test_dbt_rpc_sync_resource = dbt_rpc_sync_resource.configured({
    "host": { "env": "DBT_HOST" },
    "port": { "env": "DBT_PORT" }
})


@job(resource_defs={ "dbt": test_dbt_rpc_resource })
def run_dbt_rpc_job():
    dbt_run_op()

@job(resource_defs={"dbt_rpc":test_dbt_rpc_resource})
def run_dbt_rpc_sync_job():
    dbt_rpc_run()

@job
def run_dbt_ssh_job():
    dbt_run_ssh()
