import setuptools

setuptools.setup(
    name="orchestrator_poc",
    packages=setuptools.find_packages(exclude=["orchestrator_poc_tests"]),
    install_requires=[
        "dagster",
        "dagit",
        "pytest",
        "dagster-dbt",
        "dagster-airbyte",
        "dagster_ssh",
        "dagster_slack",
        "paramiko"
    ],
)
