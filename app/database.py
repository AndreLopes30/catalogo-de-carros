import sqlite3
import os

base_dir = os.path.abspath(os.path.dirname(__file__) + "/..")
db_path = os.path.join(base_dir, 'carros.db')

def init_db():
    with sqlite3.connect(db_path) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS carros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                modelo TEXT NOT NULL,
                ano INTEGER NOT NULL,
                preco REAL NOT NULL,
                imagem TEXT NOT NULL
            )
        ''')