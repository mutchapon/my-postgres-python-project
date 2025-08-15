from cryptography.fernet import Fernet
import yaml

# กุญแจเดียวกับที่ใช้เข้ารหัส (ใช้เหมือนกัน)
SECRET_KEY = b'B4_4LotxYspP4c--zQuhZi34sMzVhRjG0qBEOxdyKsg='  # ใช้ key เดียวกัน

def load_encrypted_config(path):
    f = Fernet(SECRET_KEY)
    with open(path, 'rb') as enc_file:
        encrypted_data = enc_file.read()
    decrypted_data = f.decrypt(encrypted_data)
    return yaml.safe_load(decrypted_data)
