from dagster import repository

from orchestrator_poc.jobs.say_hello import run_in_order
from orchestrator_poc.jobs.airbyte_jobs import run_airbyte
from orchestrator_poc.jobs.dbt_jobs import run_dbt
from orchestrator_poc.jobs.airbyte_dbt import run_airbyte_dbt
from orchestrator_poc.schedules.my_hourly_schedule import basic_schedule
from orchestrator_poc.sensors.my_sensor import my_sensor

@repository
def orchestrator_poc():
    """
    The repository definition for this orchestrator_poc Dagster repository.

    For hints on building your Dagster repository, see our documentation overview on Repositories:
    https://docs.dagster.io/overview/repositories-workspaces/repositories
    """
    jobs = [run_in_order, run_airbyte, run_dbt, run_airbyte_dbt]
    schedules = [basic_schedule]
    sensors = [my_sensor]

    return jobs + schedules + sensors
