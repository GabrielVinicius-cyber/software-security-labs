import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'src', 'vulnerable', 'database.db')

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    cursor.execute("DELETE FROM users")

    cursor.executemany(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        [
            ('admin', 'admin123'),
            ('gabriel', 'senha_forte_2026'),
            ('teste', '12345')
        ]
    )

    conn.commit()
    conn.close()
    print(f"✅ Banco de dados criado/populado em: {DB_PATH}")

if __name__ == '__main__':
    init_db()
