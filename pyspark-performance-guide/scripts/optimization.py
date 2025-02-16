from pyspark.sql import SparkSession

def optimize_queries():
    spark = SparkSession.builder.appName('Optimization').getOrCreate()
    df = spark.read.csv('data/sample.csv', header=True, inferSchema=True)
    df = df.repartition(10)
    df.cache()
    df.show()
    print("Optimization completed successfully!")

if __name__ == '__main__':
    optimize_queries()
