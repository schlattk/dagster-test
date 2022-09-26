from dagster import job
from dagster_dbt import dbt_run_op, dbt_seed_op, dbt_test_op, dbt_rpc_sync_resource
from orchestrator_poc.ops.dbt_ops import dbt_deps_op


test_dbt_rpc_sync_resource = dbt_rpc_sync_resource.configured({
    "host": { "env": "DBT_HOST" },
    "port": { "env": "DBT_PORT" }
})

@job(resource_defs={ "dbt": test_dbt_rpc_sync_resource })
def run_dbt_job():
    dbt_run_op()

@job(resource_defs={ "dbt": test_dbt_rpc_sync_resource })
def test_dbt_job():
    dbt_test_op()

@job(resource_defs={ "dbt": test_dbt_rpc_sync_resource })
def seed_dbt_job():
    dbt_seed_op()

@job(resource_defs={ "dbt": test_dbt_rpc_sync_resource })
def deps_dbt_job():
    dbt_deps_op()

@job(resource_defs={ "dbt": test_dbt_rpc_sync_resource })
def full_dbt_job():
    dbt_test_op(start_after=[dbt_run_op(start_after=[dbt_seed_op(start_after=[dbt_deps_op()])])])
