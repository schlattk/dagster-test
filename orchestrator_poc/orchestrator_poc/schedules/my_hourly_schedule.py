from dagster import schedule, ScheduleDefinition


from orchestrator_poc.jobs.say_hello import run_in_order


# @schedule(cron_schedule="50 * * * *", job=say_hello_job)
# def my_hourly_schedule():
#     """
#     A schedule definition. This example schedule runs once each hour.
#
#     For more hints on running jobs with schedules in Dagster, see our documentation overview on
#     schedules:
#     https://docs.dagster.io/overview/schedules-sensors/schedules
#     """
#     run_config = {}
#     return run_config

basic_schedule = ScheduleDefinition(job=run_in_order, cron_schedule="30 * * * *")
