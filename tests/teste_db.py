import sqlite3
import os

# Simula como o database.py deve localizar o banco
base_dir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(base_dir, 'carros.db')

def testar_conexao():
    print(f"🔍 Verificando banco em: {db_path}")
    
    if not os.path.exists(db_path):
        print("❌ ERRO: O arquivo 'carros.db' não foi encontrado na raiz!")
        return

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='carros';")
        tabela = cursor.fetchone()
        
        if tabela:
            print("✅ SUCESSO: Conexão estabelecida e tabela 'carros' localizada!")
            cursor.execute("SELECT COUNT(*) FROM carros")
            total = cursor.fetchone()[0]
            print(f"📊 Total de registros encontrados: {total}")
        else:
            print("⚠️ AVISO: Banco conectado, mas a tabela 'carros' não existe.")
            
        conn.close()
    except Exception as e:
        print(f"💥 Falha crítica ao conectar: {e}")

if __name__ == "__main__":
    testar_conexao()