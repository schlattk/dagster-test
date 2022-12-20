import os
from dagster import RunRequest, sensor, RunFailureSensorContext
from dagster_slack import make_slack_on_run_failure_sensor

def my_message_fn(context: RunFailureSensorContext) -> str:
    return (
        f"Error: {context.failure_event.message}"
    )

slack_on_run_failure = make_slack_on_run_failure_sensor(
    channel="#data-stream-alerts",
    slack_token=os.getenv("slack_token"),
    text_fn=my_message_fn,
    dagit_base_url="http://localhost:3000",
)
