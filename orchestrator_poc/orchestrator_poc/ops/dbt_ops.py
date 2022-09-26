from dagster import op
from dagster_dbt import dbt_run_op, dbt_seed_op, dbt_test_op

dbt_run_project_op = dbt_run_op

dbt_seed_project = dbt_seed_op

dbt_test_project = dbt_test_op

@op(required_resource_keys={"dbt"})
def dbt_deps_op(context):
    context.resources.dbt.rpc("deps")
