from dagster import job
from dagster_dbt import dbt_cli_resource, dbt_run_op


dbt_cli_resource = dbt_cli_resource.configured({"project-dir": "path/to/my/dbt_project"})

@job(resource_defs={"dbt":dbt_cli_resource})
def run_dbt():
    dbt_run_op()
