from dagster import op
from dagster_dbt import dbt_rpc_resource, dbt_run_op, dbt_rpc_sync_resource, dbt_rpc_run

@op
def run_dbt_op():
    dbt_run_op()
