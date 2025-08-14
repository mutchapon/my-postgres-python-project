import os
from datetime import datetime
from utils.export_csv import export_to_csv

def main():
    today = datetime.today().strftime("%Y-%m-%d")
    sql_path = os.path.join("sql", "select_users.sql")
    csv_filename = f"user_{today}.csv"
    csv_path = os.path.join("output", csv_filename)
    os.makedirs("output", exist_ok=True)
    print(f"Exporting to: {csv_path}")
    export_to_csv(sql_path, csv_path)
if __name__ == "__main__":
    main()