# scripts/process_csv_with_spark.py
import sys
import os
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pyspark.sql import SparkSession
from utils.export_csv import export_to_csv

os.environ["JAVA_HOME"] = "C:\\Program Files\\Eclipse Adoptium\\jdk-17.0.16.8-hotspot"

# ===== 1. Export CSV ก่อน =====
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_csv_path = f"output/user_{timestamp}.csv"

export_to_csv("sql/select_users.sql", output_csv_path)  # <- ให้ export ออกมาก่อน

# ===== 2. ใช้ Spark อ่าน CSV =====
spark = SparkSession.builder.appName("CSV Processing").getOrCreate()

df = spark.read.csv(output_csv_path, header=True, inferSchema=True)

# ===== 3. ประมวลผล =====
df_filtered = df.select("username", "email")

# ===== 4. เขียนผลลัพธ์ =====
df_filtered.write.csv("output/processed_output", header=True)

spark.stop()
