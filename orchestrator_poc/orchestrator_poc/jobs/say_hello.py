from dagster import job

from orchestrator_poc.ops.hello import first, second, third

# @job
# def say_hello_job():
#     """
#     A job definition. This example job has a single op.
#
#     For more hints on writing Dagster jobs, see our documentation overview on Jobs:
#     https://docs.dagster.io/concepts/ops-jobs-graphs/jobs-graphs
#     """
#     hello()
#
# @job
# def goodbye_job():
#     """
#     A job definition. This example job has a single op.
#
#     For more hints on writing Dagster jobs, see our documentation overview on Jobs:
#     https://docs.dagster.io/concepts/ops-jobs-graphs/jobs-graphs
#     """
#     goodbye()

@job
def run_in_order() -> str:
    third(second(first()))
