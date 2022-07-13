from dagster import job
from dagster_dbt import dbt_rpc_resource, dbt_run_op, dbt_rpc_sync_resource, dbt_rpc_run

test_dbt_rpc_resource = dbt_rpc_resource.configured({
    "host": { "env": "DBT_HOST" },
    
})

test_dbt_rpc_sync_resource = dbt_rpc_sync_resource.configured({
    "host": { "env": "DBT_HOST" },
    "port": { "env": "DBT_PORT" },
})


@job(resource_defs={ "dbt_rpc": test_dbt_rpc_resource })
def run_dbt():
    dbt_rpc_run()
