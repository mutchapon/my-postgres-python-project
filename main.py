# from db.db_connection import get_connection  # ← ถ้าไฟล์ชื่อ `db_connection.py` ก็แก้ชื่อ
# get_connection()
import os
from db.db_executor import execute_sql_file_with_params

# ✅ สร้างตาราง users
# create_sql_path = os.path.join("sql", "create_users_table.sql")
# execute_sql_file_with_params(create_sql_path)

# ✅ อ่าน users ทั้งหมด
select_sql_path = os.path.join("sql", "select_users.sql")
rows = execute_sql_file_with_params(select_sql_path, fetch_all=True)

print("📄 Users:")
for row in rows:
    print(row)
