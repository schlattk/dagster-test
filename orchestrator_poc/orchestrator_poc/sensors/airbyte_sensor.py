from dagster import sensor, RunRequest
from dagster.core.storage.pipeline_run import RunsFilter, DagsterRunStatus
from orchestrator_poc.jobs.airbyte_jobs import run_airbyte_and_then_dbt_cli_new
from orchestrator_poc.jobs.dbt_jobs import run_dbt_job

@sensor(job=run_dbt_job)
def airbyte_sensor(context):
    run_records = context.instance.get_run_records(
        filters=RunsFilter(
            job_name="run_airbyte_and_then_dbt_cli_new",
            statuses=[DagsterRunStatus.SUCCESS, DagsterRunStatus.FAILURE]
        ),
        order_by="update_timestamp",
        ascending=False,
    )
    for run_record in run_records:
        yield RunRequest(
            run_key=run_record.pipeline_run.run_id,  # avoid double firing for the same run
        )
