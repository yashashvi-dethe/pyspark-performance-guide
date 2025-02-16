from pyspark.sql import SparkSession

def run_etl():
    spark = SparkSession.builder.appName('ETL').getOrCreate()
    df = spark.read.csv('data/sample.csv', header=True, inferSchema=True)
    df.show()
    print("ETL process completed successfully!")

if __name__ == '__main__':
    run_etl()
