from dagster import schedule, ScheduleDefinition
from orchestrator_poc.jobs.airbyte_jobs import run_airbyte_and_then_dbt_cli
from orchestrator_poc.jobs.dbt_jobs import full_dbt_job

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

basic_schedule = ScheduleDefinition(job=run_airbyte_and_then_dbt_cli, cron_schedule="40 14 * * *")

dbt_schedule = ScheduleDefinition(job=full_dbt_job, cron_schedule="40 16 * * *")
