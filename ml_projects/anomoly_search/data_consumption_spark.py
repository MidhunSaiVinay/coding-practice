from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, DoubleType, StringType, LongType

spark = SparkSession.builder \
    .appName("RealTimeAnomalyDetection") \
    .config("spark.sql.streaming.checkpointLocation", "./checkpoint") \
    .config("spark.jars.packages", 
            "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1," + 
            "org.apache.kafka:kafka-clients:3.5.1") \
    .config("spark.scala.version", "2.12.18") \
    .config("spark.driver.memory", "2g") \
    .getOrCreate()

schema = StructType()\
    .add("timestamp", DoubleType())\
    .add("transaction_id", LongType())\
    .add("amount", DoubleType())\
    .add("account_id", LongType())\
    .add("transaction_type", StringType())

df = spark.readStream.format("kafka")\
    .option("kafka.bootstrap.servers", "localhost:9092")\
    .option("subscribe", "transaction_data")\
    .option("startingOffsets", "earliest")\
    .load()

parsed_df = df.select(from_json(col("value").cast("string"), schema).alias("data")).select("data.*")

query = parsed_df.writeStream.format("console").start()
query.awaitTermination()