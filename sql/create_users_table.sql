CREATE TABLE IF NOT EXISTS new_users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100)
);