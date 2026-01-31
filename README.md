# 🚗 API Catálogo de Carros

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![Flask Version](https://img.shields.io/badge/flask-3.0-green)
![Status](https://img.shields.io/badge/status-concluido-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

Projeto de backend desenvolvido em **Python** para gerenciamento e controle de frota de veículos. O objetivo deste projeto é demonstrar a aplicação de **boas práticas**, arquitetura **REST** e **containerização** com Docker.

---

## 📸 Preview do Sistema

<div align="center">
  <img width="100%" alt="Screenshot do Sistema" src="https://github.com/user-attachments/assets/66e82c3d-c6b7-48f4-aed6-e9600440990f" />
  <p><em>Interface de listagem e gerenciamento do catálogo.</em></p>
</div>

---

## 🛠️ Stack Tecnológica

| Tecnologia | Ícone | Uso no projeto |
| :--- | :---: | :--- |
| **Python** | <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="25"> | Linguagem principal |
| **Flask** | <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/flask/flask-original.svg" width="25"> | Framework web para a API |
| **SQLite** | <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/sqlite/sqlite-original.svg" width="25"> | Banco de dados leve (local) |
| **Docker** | <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original.svg" width="25"> | Containerização |
| **SweetAlert2** | 🍬 | Pop-ups e feedbacks visuais |

---

## 🚀 Funcionalidades (Endpoints)

| Método | Rota | Descrição |
| :--- | :--- | :--- |
| `GET` | `/` | Página inicial do sistema |
| `GET` | `/catalogo` | Exibe todos os veículos cadastrados |
| `POST` | `/catalogo` | Adiciona um novo carro |
| `GET/POST` | `/carro/<id>/editar` | Visualiza e salva alterações de um veículo |
| `DELETE` | `/carros/<id>/delete` | Remove um veículo do sistema |

---

## 📦 Como rodar o projeto

### 🐋 Via Docker (Recomendado)
```bash
# Clone o repositório
git clone [https://github.com/AndreLopes30/catalogo-de-carros.git](https://github.com/AndreLopes30/catalogo-de-carros.git)

# Entre na pasta
cd catalogo-de-carros

# Suba os containers
docker-compose up --build
