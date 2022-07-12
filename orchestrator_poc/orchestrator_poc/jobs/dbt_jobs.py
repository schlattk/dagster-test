from dagster import job
from dagster_dbt import dbt_rpc_resource, dbt_run_op

dbt_rpc_resource = dbt_rpc_resource.configured(
    "host": "$DBT_HOST" ,
    "port": "$DBT_PORT",
)

@job(resource_defs={"dbt":dbt_rpc_resource})
def run_dbt():
    dbt_run_op()
