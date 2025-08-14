import psycopg2
import yaml
import os

def load_config():
    config_path = os.path.join("config", "config.yml")
    with open(config_path, "r") as file:
        return yaml.safe_load(file)

def get_connection():

    config = load_config()
    db = config["database"]

    # print("🔑 Loaded password from config:", db["password"])

    connection = psycopg2.connect(
        host=db["host"],
        port=db["port"],
        database=db["name"],
        user=db["user"],
        password=db["password"]
    )
    return connection