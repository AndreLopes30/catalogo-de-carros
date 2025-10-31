from flask import Flask, render_template, request, redirect, send_file
from fpdf import FPDF
import json
import os
import io

app = Flask(__name__)
ARQUIVO_CARROS = 'carros.json'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/catalogo', methods=['GET', 'POST'])
def catalogo():

    if os.path.exists(ARQUIVO_CARROS):
        with open(ARQUIVO_CARROS, 'r', encoding='utf-8') as f:
            carros = json.load(f)
    else:
        carros = []

    if request.method == 'POST':
        # Pegando os valores do formulário
        modelo = request.form['modelo']
        ano = int(request.form['ano'])
        preco = int(request.form['preco'])
        imagem = request.form['imagem']

        if modelo == '' or ano < 1900 or ano > 2025 or preco < 0:
            return render_template('index.html', carros=carros, erro="Algum dos campos inválido.")

            

        carro = {
            'modelo': modelo,
            'ano': ano,
            'preco': preco,
            'imagem': imagem
        }

        carros.append(carro)
        with open(ARQUIVO_CARROS, 'w', encoding='utf-8') as f:
            json.dump(carros, f, indent=4, ensure_ascii=False)

        return redirect('/catalogo')

    return render_template('catalogo.html', carros=carros)

@app.route('/relatorio')
def relatorio():
    with open(ARQUIVO_CARROS, 'r', encoding='utf-8') as f:
        carros = json.load(f)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Relatório de Carros", ln=True, align='C')

    for carro in carros:
        pdf.cell(200, 10, txt=f"Modelo: {carro['modelo']} - Ano: {carro['ano']} - Preço: R$ {carro['preco']}", ln=True)

    pdf_output = pdf.output(dest='S').encode('latin1')

    pdf_buffer = io.BytesIO(pdf_output)

    return send_file(
        pdf_buffer,
        as_attachment=True,
        download_name="relatorio_carros.pdf",
        mimetype='application/pdf'
    )





if __name__ == '__main__':
    app.run(debug=True)

