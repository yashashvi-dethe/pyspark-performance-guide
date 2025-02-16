from setuptools import setup, find_packages
setup(
    name="pyspark-performance-guide",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "pyspark",
        "airflow",
        "google-cloud-bigquery",
        "pandas"
    ]
)
