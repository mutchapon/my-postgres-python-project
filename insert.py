import os
from db.db_executor import execute_sql_file_with_params

# เตรียม path ไปยังไฟล์ SQL
insert_sql_path = os.path.join("sql", "insert_user.sql")

# ข้อมูลที่จะ insert
username = "john_doe"
email = "john@example.com"
params = (username, email)

# เรียกฟังก์ชัน insert
execute_sql_file_with_params(insert_sql_path, params=params)

print("✅ User inserted successfully!")
