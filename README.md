# 🚗 API Catálogo de Carros

🔗 [Acesse o projeto online](catalogo-de-carros-production-bfe6.up.railway.app)

Projeto de Backend desenvolvido em Python para gerenciamento e controle de frota de veículos. O objetivo deste projeto é demonstrar a aplicação de boas práticas de desenvolvimento, arquitetura REST e containerização.

---

## 📸 Preview

<img width="1900" height="945" alt="image" src="https://github.com/user-attachments/assets/66e82c3d-c6b7-48f4-aed6-e9600440990f" />


---

## 🛠️ Tecnologias utilizadas

## 🛠 Tecnologias Utilizadas
* **Linguagem:** Python 3.9
* **Framework:** [Flask]
* **Banco de Dados:** [SQLite]
* **Containerização:** Docker
* **Versionamento:** Git

---

## 📄 Descrição

Este projeto permite visualizar uma lista de carros com informações como marca, modelo e ano. O frontend é responsivo e interativo, enquanto o backend em Flask fornece os dados via API.

---

## 🚀 Funcionalidades
* Cadastro de novos veículos (Create)
* Listagem e filtragem de veículos (Read)
* Atualização de dados da frota (Update)
* Remoção de veículos (Delete)

---

## 📦 Como rodar o projeto

### Via Docker (Recomendado)
```bash
docker build -t catalogo-carros .
docker run -p 5000:5000 catalogo-carros

---

## 🚀 Como executar localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/AndreLopes30/catalogo-de-carros.git

2. Instale as dependências:
   pip install -r requirements.txt

3. Execute o servidor:
   python app.py

4. Acesse no navegador:
   http://localhost:5000
