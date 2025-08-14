import csv
import os
from db.db_executor import execute_sql_file_with_params
from db.db_connection import get_connection

def export_to_csv(sql_path, output_path):
    # Fetch rows
    rows = execute_sql_file_with_params(sql_path, fetch_all=True)

    if not rows:
        print("⚠️ No data found.")
        return

    # Get column names from cursor.description
    with open(sql_path, "r", encoding="utf-8") as file:
        sql = file.read().strip()

    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(sql)
    column_names = [desc[0] for desc in cursor.description]

    # Write to CSV
    with open(output_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(column_names)  # Write header
        writer.writerows(rows)         # Write data

    print(f"✅ Exported to: {output_path}")

    cursor.close()
    connection.close()