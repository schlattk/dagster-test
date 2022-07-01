import setuptools

setuptools.setup(
    name="orchestrator_poc",
    packages=setuptools.find_packages(exclude=["orchestrator_poc_tests"]),
    install_requires=[
        "dagster==0.15.0",
        "dagit==0.15.0",
        "pytest",
        "dagster-dbt",
        "dagster-airbyte",
    ],
)
