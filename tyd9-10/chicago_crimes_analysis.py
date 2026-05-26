from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StringType
from pyspark.ml.feature import StringIndexer, OneHotEncoder, VectorAssembler
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml import Pipeline
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

spark = (
    SparkSession.builder
    .appName("ChicagoCrimesAnalysis")
    .config("spark.driver.memory", "4g")
    .config("spark.executor.memory", "4g")
    .getOrCreate()
)

df_crimes = (
    spark.read
    .option("header", True)
    .option("inferSchema", False)
    .csv("chicago_crimes_sample.csv")
)

df_crimes.show(5, truncate=False)
df_crimes.printSchema()

key_cols = ["date", "primary_type", "location_description", "year"]

df_clean = (
    df_crimes
    .dropDuplicates()
    .dropna(subset=key_cols)
)

df_clean = df_clean.withColumn(
    "ParsedDate",
    F.to_timestamp("date", "yyyy-MM-dd'T'HH:mm:ss.SSS")
)

df_clean = df_clean.filter(F.col("ParsedDate").isNotNull())

df_clean = (
    df_clean
    .withColumn("Hour", F.hour("ParsedDate"))
    .withColumn("Weekday", F.date_format("ParsedDate", "E"))
)

def classify_daytime(hour: int) -> str:
    if hour is None:
        return "unknown"
    if 0 <= hour < 6:
        return "noc"
    elif 6 <= hour < 12:
        return "rano"
    elif 12 <= hour < 18:
        return "dzien"
    else:
        return "wieczor"

udf_daytime = F.udf(classify_daytime, StringType())

df_clean = df_clean.withColumn("Daytime", udf_daytime(F.col("Hour")))

df_clean = df_clean.cache()
df_clean.count()

crime_type_map = [
    ("THEFT", "property"),
    ("BATTERY", "violent"),
    ("CRIMINAL DAMAGE", "property"),
    ("NARCOTICS", "drug"),
]

df_dict = spark.createDataFrame(crime_type_map, ["primary_type", "CrimeCategory"])

df_enriched = (
    df_clean
    .join(F.broadcast(df_dict), on="primary_type", how="left")
    .withColumn("CrimeCategory", F.coalesce(F.col("CrimeCategory"), F.lit("other")))
)

df_enriched.select("primary_type", "CrimeCategory").show(10, truncate=False)

(
    df_enriched
    .write
    .mode("overwrite")
    .partitionBy("year")
    .parquet("output/chicago_crimes_parquet_by_year")
)

df_analysis = (
    df_enriched
    .groupBy("location_description", "Daytime", "primary_type")
    .agg(F.count("*").alias("CrimeCount"))
)

df_analysis.orderBy(F.desc("CrimeCount")).show(20, truncate=False)

df_heavy_agg = (
    df_enriched
    .groupBy("year", "CrimeCategory", "Daytime")
    .agg(
        F.count("*").alias("TotalCrimes"),
        F.countDistinct("location_description").alias("DistinctLocations")
    )
)

df_heavy_agg.orderBy("year", "CrimeCategory", "Daytime").show(30, truncate=False)

df_heavy_agg.explain(mode="extended")

df_ml = df_enriched.select(
    "primary_type",
    "location_description",
    "Daytime",
    "CrimeCategory",
    "arrest",
    "domestic",
    "Hour"
).dropna()

cat_cols = ["location_description", "Daytime", "CrimeCategory"]
bool_cols = ["arrest", "domestic"]
num_cols = ["Hour"]

indexers = [
    StringIndexer(inputCol=c, outputCol=f"{c}_idx", handleInvalid="keep")
    for c in cat_cols + bool_cols + ["primary_type"]
]

encoders = [
    OneHotEncoder(inputCol=f"{c}_idx", outputCol=f"{c}_vec")
    for c in cat_cols + bool_cols
]

assembler = VectorAssembler(
    inputCols=[f"{c}_vec" for c in cat_cols + bool_cols] + num_cols,
    outputCol="features"
)

rf = RandomForestClassifier(
    labelCol="primary_type_idx",
    featuresCol="features",
    numTrees=30,  
    maxDepth=5,   
    seed=42
)

pipeline = Pipeline(stages=indexers + encoders + [assembler, rf])

train_df, test_df = df_ml.randomSplit([0.8, 0.2], seed=42)

model = pipeline.fit(train_df)
predictions = model.transform(test_df)

predictions.select(
    "primary_type",
    "prediction",
    "probability"
).show(20, truncate=False)

evaluator = MulticlassClassificationEvaluator(
    labelCol="primary_type_idx",
    predictionCol="prediction",
    metricName="accuracy"
)

accuracy = evaluator.evaluate(predictions)
print(f"\n=================================")
print(f"Accuracy modelu: {accuracy:.4f}")
print(f"=================================\n")

spark.stop()