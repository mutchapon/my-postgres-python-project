from encrypt.decrypt_config import load_encrypted_config
import psycopg2

def get_connection():
    config = load_encrypted_config("config/config.enc")
    db = config["database"]

    connection = psycopg2.connect(
        host=db["host"],
        port=db["port"],
        database=db["name"],
        user=db["user"],
        password=db["password"]
    )
    return connection
