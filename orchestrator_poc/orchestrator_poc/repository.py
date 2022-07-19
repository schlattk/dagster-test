from dagster import repository

from orchestrator_poc.jobs.say_hello import run_in_order
from orchestrator_poc.jobs.airbyte_jobs import run_dagster_airbyte, run_airbyte_and_then_dbt_cli
from orchestrator_poc.jobs.dbt_jobs import run_dbt_job
from orchestrator_poc.sensors.my_sensor import my_sensor

@repository
def orchestrator_poc():
    """
    The repository definition for this orchestrator_poc Dagster repository.

    For hints on building your Dagster repository, see our documentation overview on Repositories:
    https://docs.dagster.io/overview/repositories-workspaces/repositories
    """
    jobs = [run_in_order, run_dagster_airbyte, run_airbyte_and_then_dbt_cli]
    schedules = []
    sensors = [my_sensor]

    return jobs + schedules + sensors
