from utils.import_csv import import_from_csv

if __name__ == "__main__":
    csv_path = "output/user_2025-08-14_14-52-29.csv"
    table_name = "new_users"
    import_from_csv(csv_path, table_name)