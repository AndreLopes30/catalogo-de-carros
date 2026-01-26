from flask import Flask, render_template, request, redirect, send_file
import sqlite3
import os
import io

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/catalogo', methods=['GET', 'POST'])
def catalogo():
    conn = sqlite3.connect('carros.db')
    cursor = conn.cursor()

    cursor.execute("SELECT id, modelo, ano, preco, imagem FROM carros")
    carros = [
    {
        'id': id,
        'modelo': modelo,
        'ano': ano,
        'preco': preco,
        'imagem': imagem
    }
    for id, modelo, ano, preco, imagem in cursor.fetchall()
]

    if request.method == 'POST':
        modelo = request.form['modelo']
        ano = int(request.form['ano'])
        preco = float(request.form['preco'])
        imagem = request.form['imagem']

        if modelo == '' or ano < 1900 or ano > 2026 or preco < 0:
            conn.close()
            return render_template('index.html', carros=carros, erro="Algum dos campos inválido.")

        cursor.execute("""
            INSERT INTO carros (modelo, ano, preco, imagem)
            VALUES (?, ?, ?, ?)
        """, (modelo, ano, preco, imagem))
        conn.commit()
        conn.close()
        return redirect('/catalogo')

    conn.close()
    return render_template('catalogo.html', carros=carros)

@app.route('/carro/<int:id>')
def infos(id):
    conn = sqlite3.connect('carros.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, modelo, ano, preco, imagem
        FROM carros
        WHERE id = ?
    """, (id,))

    row = cursor.fetchone()
    conn.close()

    if row is None:
        return "Carro não encontrado", 404

    carro = {
        'id': row[0],
        'modelo': row[1],
        'ano': row[2],
        'preco': row[3],
        'imagem': row[4]
    }

    return render_template('carro.html', carro=carro)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
