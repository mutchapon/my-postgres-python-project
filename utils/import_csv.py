import csv
from db.db_connection import get_connection

def import_from_csv(csv_path, table_name):
    """
    นำข้อมูลจากไฟล์ CSV เข้าไปยังตารางใน PostgreSQL

    csv_path: path ของไฟล์ CSV
    table_name: ชื่อตารางในฐานข้อมูลที่ต้องการ import ข้อมูลเข้าไป
    """
    conn = get_connection()
    cursor = conn.cursor()

    try:
        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)  # อ่านแถว header เพื่อดึงชื่อคอลัมน์

            # สร้าง SQL INSERT query แบบ dynamic
            columns = ', '.join(headers)
            placeholders = ', '.join(['%s'] * len(headers))
            sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

            for row in reader:
                cursor.execute(sql, row)

        conn.commit()
        print(f"✅ Imported data from '{csv_path}' into table '{table_name}' successfully!")

    except Exception as e:
        conn.rollback()
        print(f"❌ Error importing CSV: {e}")

    finally:
        cursor.close()
        conn.close()