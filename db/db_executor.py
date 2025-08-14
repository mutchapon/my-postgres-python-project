from db.db_connection import get_connection
import os

def execute_sql_file_with_params(sql_path, params=None, fetch_one=False, fetch_all=False):
    connection = None
    result = None
    try:
        # อ่าน SQL จากไฟล์
        with open(sql_path, "r", encoding="utf-8") as file:
            sql = file.read()

        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(sql, params)

        if fetch_one:
            result = cursor.fetchone()
        elif fetch_all:
            result = cursor.fetchall()

        connection.commit()
        return result

    except Exception as error:
        print("❌ Error executing SQL file:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
