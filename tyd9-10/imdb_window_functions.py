from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window
import matplotlib.pyplot as plt
from datasets import load_dataset

spark = SparkSession.builder \
    .appName("IMDBWindowFunctions") \
    .config("spark.driver.memory", "4g") \
    .getOrCreate()

ds = load_dataset("stanfordnlp/imdb", split="train").select(range(2000))
pdf = ds.to_pandas()
df = spark.createDataFrame(pdf)

df = df.withColumn("id", F.monotonically_increasing_id())
df = df.withColumn("word_count", F.size(F.split("text", " ")))

w_rank = Window.partitionBy("label").orderBy(F.col("word_count").desc())
df_ranked = df.withColumn("rank", F.row_number().over(w_rank))

df_top3 = df_ranked.filter(F.col("rank") <= 3)
df_top3.select("id", "label", "word_count", "rank").show()

w_avg = Window.partitionBy("label")
df_diff = df_ranked.withColumn("diff_from_avg", F.col("word_count") - F.avg("word_count").over(w_avg))

df_diff.select("id", "label", "word_count", "diff_from_avg").show(5)

w_ma = Window.partitionBy("label").orderBy("id").rowsBetween(-50, 0)
df_ma = df_diff.withColumn("moving_avg_50", F.avg("word_count").over(w_ma))

df_ma.select("id", "label", "word_count", "moving_avg_50").show(5)

pdf_ma = df_ma.select("id", "label", "moving_avg_50").orderBy("id").toPandas()
pos = pdf_ma[pdf_ma["label"] == 1]
neg = pdf_ma[pdf_ma["label"] == 0]

plt.figure(figsize=(12, 6))
plt.plot(pos["id"], pos["moving_avg_50"], label="Positive", color="green")
plt.plot(neg["id"], neg["moving_avg_50"], label="Negative", color="red")
plt.legend()
plt.grid(True)
plt.show()

spark.stop()
