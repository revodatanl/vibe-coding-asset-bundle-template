# Databricks notebook source
# MAGIC %md
# MAGIC # DLT Pipeline: Million Song Dataset Example
# MAGIC
# MAGIC This notebook defines a Delta Live Tables (DLT) pipeline for ingesting and processing a subset of the Million Song Dataset.

# COMMAND ----------

import dlt
from pyspark.sql.functions import desc, expr
from pyspark.sql.types import (
    DoubleType,
    IntegerType,
    StringType,
    StructField,
    StructType,
)

# COMMAND ----------

# Define the path to the source data
file_path = "/databricks-datasets/songs/data-001/"

# COMMAND ----------

# Define the schema for the input data
schema = StructType(
    [
        StructField("artist_id", StringType(), True),
        StructField("artist_lat", DoubleType(), True),
        StructField("artist_long", DoubleType(), True),
        StructField("artist_location", StringType(), True),
        StructField("artist_name", StringType(), True),
        StructField("duration", DoubleType(), True),
        StructField("end_of_fade_in", DoubleType(), True),
        StructField("key", IntegerType(), True),
        StructField("key_confidence", DoubleType(), True),
        StructField("loudness", DoubleType(), True),
        StructField("release", StringType(), True),
        StructField("song_hotnes", DoubleType(), True),
        StructField("song_id", StringType(), True),
        StructField("start_of_fade_out", DoubleType(), True),
        StructField("tempo", DoubleType(), True),
        StructField("time_signature", DoubleType(), True),
        StructField("time_signature_confidence", DoubleType(), True),
        StructField("title", StringType(), True),
        StructField("year", IntegerType(), True),
        StructField("partial_sequence", IntegerType(), True),
    ]
)

# COMMAND ----------


@dlt.table(
    comment="Raw data from a subset of the Million Song Dataset; a collection of features and metadata for contemporary music tracks."
)
def songs_raw():
    return (
        spark.readStream.format("cloudFiles")
        .schema(schema)
        .option("cloudFiles.format", "csv")
        .option("sep", "\t")
        .option("inferSchema", True)
        .load(file_path)
    )


# COMMAND ----------


@dlt.table(comment="Million Song Dataset with data cleaned and prepared for analysis.")
@dlt.expect("valid_artist_name", "artist_name IS NOT NULL")
@dlt.expect("valid_title", "song_title IS NOT NULL")
@dlt.expect("valid_duration", "duration > 0")
def songs_prepared():
    return (
        dlt.read.table("songs_raw")
        .withColumnRenamed("title", "song_title")
        .select(
            "artist_id",
            "artist_name",
            "duration",
            "release",
            "tempo",
            "time_signature",
            "song_title",
            "year",
        )
    )


# COMMAND ----------


@dlt.table(
    comment="A table summarizing counts of songs released by the artists who released the most songs each year."
)
def top_artists_by_year():
    return (
        dlt.read.table("songs_prepared")
        .filter(expr("year > 0"))
        .groupBy("artist_name", "year")
        .count()
        .withColumnRenamed("count", "total_number_of_songs")
        .sort(desc("total_number_of_songs"), desc("year"))
    )
