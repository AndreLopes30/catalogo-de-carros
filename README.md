# 🚗 API Catálogo de Carros

Projeto de backend desenvolvido em **Python** para gerenciamento e controle de frota de veículos.  
O objetivo deste projeto é demonstrar a aplicação de **boas práticas**, arquitetura **REST** e **containerização** com Docker.

---

## 📸 Preview

<img width="1900" height="945" alt="image" src="https://github.com/user-attachments/assets/66e82c3d-c6b7-48f4-aed6-e9600440990f" />


---

## 🛠️ Tecnologias utilizadas

| Tecnologia | Uso no projeto |
|------------|----------------|
| 🐍 Python | Linguagem principal |
| 🚀 Flask | Framework web para a API |
| 🗃️ SQLite | Banco de dados leve (local) |
| 🐋 Docker | Containerização |
| 🧪 (Opcional) Pytest | Testes automatizados |
| 📦 Flask-RESTful | Organização de rotas REST |

---

## 📄 Descrição

Este projeto permite visualizar e gerenciar uma lista de carros com informações como marca, modelo e ano.  
O backend em Flask fornece os dados via API que pode ser consumida por um frontend ou ferramentas externas.

---

## 🚀 Funcionalidades

| Método | Rota | Descrição |
|--------|------|-----------|
| POST | `/carros` | Adiciona um novo carro |
| GET | `/carros` | Lista todos os carros |
| GET | `/carros/<id>` | Detalha um carro por ID |
| PUT | `/carros/<id>` | Atualiza um carro por ID |
| DELETE | `/carros/<id>` | Remove um carro por ID |

---

## 📦 Como rodar o projeto

### Via Docker (Recomendado)
```bash
docker-compose up --build
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
