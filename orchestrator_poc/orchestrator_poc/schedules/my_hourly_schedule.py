from dagster import schedule, ScheduleDefinition
from orchestrator_poc.jobs.airbyte_jobs import run_airbyte_and_then_dbt_cli





@schedule(cron_schedule="50 * * * *", job=run_airbyte_and_then_dbt_cli)
def my_hourly_schedule():
    """
    A schedule definition. This example schedule runs once each hour.

    For more hints on running jobs with schedules in Dagster, see our documentation overview on
    schedules:
    https://docs.dagster.io/overview/schedules-sensors/schedules
    """
    run_config = {}
    return run_config

basic_schedule = ScheduleDefinition(job=run_airbyte_and_then_dbt_cli, cron_schedule="0 12 * * *")
