import os
from utils.export_csv import export_to_csv

if __name__ == "__main__":
    sql_path = os.path.join("sql", "select_users.sql")
    csv_path = os.path.join("output", "users_export.csv")

    os.makedirs("output", exist_ok=True)  # สร้างโฟลเดอร์ถ้ายังไม่มี

    export_to_csv(sql_path, csv_path)
