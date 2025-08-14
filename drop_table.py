import os
from db.db_executor import execute_sql_file_with_params  # ✅ ใช้ตัวนี้พอ

# Path ไปยังไฟล์ SQL
drop_sql_path = os.path.join("sql", "drop_users_table.sql")

# Execute SQL
execute_sql_file_with_params(drop_sql_path)

print("✅ Dropped users table successfully.")
