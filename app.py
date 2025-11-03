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

    if request.method == 'POST':
        modelo = request.form['modelo']
        ano = int(request.form['ano'])
        preco = int(request.form['preco'])
        imagem = request.form['imagem']

        if modelo == '' or ano < 1900 or ano > 2025 or preco < 0:
            return render_template('index.html', carros=carros, erro="Algum dos campos inválido.")

            

        cursor.execute("""
            INSERT INTO carros (modelo, ano, preco, imagem)
            VALUES (?, ?, ?, ?)
        """, (modelo, ano, preco, imagem))
        conn.commit()
        conn.close()
        return redirect('/catalogo')

    cursor.execute("SELECT modelo, ano, preco, imagem FROM carros")
    carros = [
    {'modelo': modelo, 'ano': ano, 'preco': preco, 'imagem': imagem}
    for modelo, ano, preco, imagem in cursor.fetchall()]
    conn.close()
    return render_template('catalogo.html', carros=carros)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

