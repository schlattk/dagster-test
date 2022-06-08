import setuptools

setuptools.setup(
    name="orchestrator_poc",
    packages=setuptools.find_packages(exclude=["orchestrator_poc_tests"]),
    install_requires=[
        "dagster==0.14.19",
        "dagit==0.14.19",
        "pytest",
        "dagster-dbt",
        "dagster-airbyte",
    ],
)
