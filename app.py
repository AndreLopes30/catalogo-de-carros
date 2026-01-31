from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os
from urllib.parse import urlparse
import requests
from PIL import Image
from io import BytesIO
from datetime import datetime

app = Flask(__name__)

def validar_url_imagem(url, timeout=3):
    try:
        resultado = urlparse(url)
        if not all([resultado.scheme, resultado.netloc]):
            return False
        
        response = requests.head(url, timeout=timeout, allow_redirects=True)
        content_type = response.headers.get('content-type', '')
        
        if 'image' not in content_type.lower():
            return False
            
        return True
    except:
        return False

def normalizar_preco(valor_str):
    valor_str = valor_str.strip()
    valor_str = valor_str.replace('.', '')
    valor_str = valor_str.replace(',', '.')
    return float(valor_str)

def formatar_preco(valor):
    return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/catalogo', methods=['GET', 'POST'])
def catalogo():
    conn = sqlite3.connect('carros.db')
    cursor = conn.cursor()

    if request.method == 'POST':
        modelo = request.form['modelo']
        ano = int(request.form['ano'])
        try:
            preco = normalizar_preco(request.form['preco'])
        except ValueError:
            conn.close()
            return redirect('/catalogo')
        
        imagem = request.form['imagem']
        ano_atual = datetime.now().year
        
        if modelo == '' or ano < 1900 or ano > ano_atual + 1 or preco < 0:
            conn.close()
            return redirect('/catalogo')
        
        cursor.execute("""
            INSERT INTO carros (modelo, ano, preco, imagem)
            VALUES (?, ?, ?, ?)
        """, (modelo, ano, preco, imagem))
        conn.commit()
        conn.close()
        return redirect('/catalogo')

    pagina = request.args.get('pagina', 1, type=int)
    busca = request.args.get('busca', '').strip()
    por_pagina = 12
    offset = (pagina - 1) * por_pagina

    if busca:
        filtro_sql = "WHERE modelo LIKE ? OR ano LIKE ? OR preco LIKE ?"
        params = (f'%{busca}%', f'%{busca}%', f'%{busca}%')
    else:
        filtro_sql = ""
        params = ()

    cursor.execute(f"SELECT COUNT(*) FROM carros {filtro_sql}", params)
    total_carros = cursor.fetchone()[0]
    total_paginas = max(1, (total_carros + por_pagina - 1) // por_pagina)

    query = f"SELECT id, modelo, ano, preco, imagem FROM carros {filtro_sql} LIMIT ? OFFSET ?"
    cursor.execute(query, params + (por_pagina, offset))
    rows = cursor.fetchall()
    
    carros = []
    for id, modelo, ano, preco, imagem in rows:
        carros.append({
            'id': id,
            'modelo': modelo,
            'ano': ano,
            'preco': formatar_preco(preco),
            'imagem': imagem
        })

    conn.close()
    return render_template('catalogo.html', 
                           carros=carros, 
                           pagina=pagina, 
                           total_paginas=total_paginas,
                           busca=busca)

@app.route('/carro/<int:id>')
def infos(id):
    conn = sqlite3.connect('carros.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, modelo, ano, preco, imagem FROM carros WHERE id = ?", (id,))
    row = cursor.fetchone()
    conn.close()

    if row is None:
        return "Carro não encontrado", 404

    carro = {
        'id': row[0], 'modelo': row[1], 'ano': row[2],
        'preco': formatar_preco(row[3]), 'imagem': row[4]
    }
    return render_template('carro.html', carro=carro)

@app.route('/carros/<int:id>/delete', methods=['POST'])
def delete(id):
    pagina_atual = request.args.get('pagina', 1, type=int)
    conn = sqlite3.connect('carros.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM carros WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('catalogo', pagina=pagina_atual))

@app.route('/carro/<int:id>/editar', methods=['GET', 'POST'])
def editar(id):
    conn = sqlite3.connect('carros.db')
    cursor = conn.cursor()
    
    if request.method == 'POST':
        modelo = request.form['modelo']
        ano = int(request.form['ano'])
        try:
            preco = normalizar_preco(request.form['preco'])
        except ValueError:
            conn.close()
            return redirect(f'/carro/{id}/editar')
        
        imagem = request.form['imagem']
        ano_atual = datetime.now().year
        
        if modelo == '' or ano < 1900 or ano > ano_atual + 1 or preco < 0 or not validar_url_imagem(imagem):
            conn.close()
            return redirect(f'/carro/{id}/editar')
        
        cursor.execute("""
            UPDATE carros 
            SET modelo = ?, ano = ?, preco = ?, imagem = ?
            WHERE id = ?
        """, (modelo, ano, preco, imagem, id))
        conn.commit()
        conn.close()
        return redirect(f'/carro/{id}')
    
    cursor.execute("SELECT id, modelo, ano, preco, imagem FROM carros WHERE id = ?", (id,))
    row = cursor.fetchone()
    conn.close()
    
    if row is None:
        return "Carro não encontrado", 404
    
    carro = {'id': row[0], 'modelo': row[1], 'ano': row[2], 'preco': row[3], 'imagem': row[4]}
    return render_template('editar.html', carro=carro)

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

if __name__ == '__main__':
    init_db()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)