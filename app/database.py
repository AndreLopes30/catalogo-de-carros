import sqlite3

def init_db():
    with sqlite3.connect('carros.db') as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS carros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                modelo TEXT NOT NULL,
                ano INTEGER NOT NULL,
                preco REAL NOT NULL,
                imagem TEXT NOT NULL
            )
        ''')