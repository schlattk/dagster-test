from dagster import RunRequest, sensor

from orchestrator_poc.jobs.say_hello import run_in_order


@sensor(job=run_in_order)
def my_sensor(_context):
    """
    A sensor definition. This example sensor always requests a run at each sensor tick.

    For more hints on running jobs with sensors in Dagster, see our documentation overview on
    sensors:
    https://docs.dagster.io/overview/schedules-sensors/sensors
    """
    should_run = True
    if should_run:
        yield RunRequest(run_key=None, run_config={})
