from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os
from urllib.parse import urlparse

app = Flask(__name__)

def validar_url_imagem(url):
    try:
        resultado = urlparse(url)
        return all([resultado.scheme, resultado.netloc])
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

    pagina = request.args.get('pagina', 1, type=int)
    por_pagina = 12
    offset = (pagina - 1) * por_pagina

    cursor.execute("SELECT COUNT(*) FROM carros")
    total_carros = cursor.fetchone()[0]
    total_paginas = (total_carros + por_pagina - 1) // por_pagina

    cursor.execute("SELECT id, modelo, ano, preco, imagem FROM carros LIMIT ? OFFSET ?", (por_pagina, offset))
    
    carros = []
    for id, modelo, ano, preco, imagem in cursor.fetchall():
        carros.append({
            'id': id,
            'modelo': modelo,
            'ano': ano,
            'preco': formatar_preco(preco),
            'imagem': imagem
        })

    if request.method == 'POST':
        modelo = request.form['modelo']
        ano = int(request.form['ano'])
        try:
            preco = normalizar_preco(request.form['preco'])
        except ValueError:
            conn.close()
            return redirect('/')

        imagem = request.form['imagem']

        if modelo == '' or ano < 1900 or ano > 2026 or preco < 0 or not validar_url_imagem(imagem):
            conn.close()
            return redirect('/')

        cursor.execute("""
            INSERT INTO carros (modelo, ano, preco, imagem)
            VALUES (?, ?, ?, ?)
        """, (modelo, ano, preco, imagem))
        conn.commit()
        conn.close()
        return redirect('/catalogo')

    conn.close()
    return render_template('catalogo.html', 
                           carros=carros, 
                           pagina=pagina, 
                           total_paginas=total_paginas)

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
        
        if modelo == '' or ano < 1900 or ano > 2026 or preco < 0 or not validar_url_imagem(imagem):
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

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)