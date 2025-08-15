from cryptography.fernet import Fernet

# กุญแจแบบ hardcoded (⚠️ ไม่ปลอดภัยมาก แต่ง่าย)
SECRET_KEY = b'B4_4LotxYspP4c--zQuhZi34sMzVhRjG0qBEOxdyKsg='  # จะใส่จริงตอนถัดไป

def generate_key():
    key = Fernet.generate_key()
    print("🔑 Copy and paste this SECRET_KEY into your code:")
    print(key.decode())

def encrypt_file(input_path, output_path, key):
    fernet = Fernet(key)
    with open(input_path, 'rb') as f:
        data = f.read()
    encrypted = fernet.encrypt(data)
    with open(output_path, 'wb') as f:
        f.write(encrypted)
    print(f"✅ Encrypted {input_path} → {output_path}")

if __name__ == "__main__":
    # Step 1: Generate key first time only
    # generate_key()

    # Step 2: After pasting key above, uncomment below:
    encrypt_file("config/config.yml", "config/config.enc", SECRET_KEY)
    pass