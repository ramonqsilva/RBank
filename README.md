# 💰 RBank - Sistema Bancário (FastAPI & Jinja2)

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-00a393.svg)
![Jinja2](https://img.shields.io/badge/Jinja2-3.1+-red.svg)
![Arquitetura](https://img.shields.io/badge/Arquitetura-Em_Camadas-8a2be2.svg)

O **RBank** é uma aplicação de simulação bancária desenvolvida em Python. O projeto demonstra a transição de uma interface de linha de comando (CLI) para uma interface Web moderna, aplicando os princípios de **Arquitetura em Camadas** (Model, View, Controller/Service) e o padrão **PRG (Post/Redirect/Get)**.

## 🚀 Funcionalidades

- **Dashboard Web Interativo:** Interface construída com HTML/CSS (Glassmorphism), renderizada via servidor.
- **Múltiplos Clientes:** Alternância dinâmica de contas ativas no painel.
- **Transações Financeiras:** Operações de Saque e Depósito com atualização de saldo em tempo real (Mock na memória).
- **Separação de Responsabilidades:** Camadas de dados, regras de negócio e rotas de apresentação estritamente isoladas.

## 📂 Estrutura do Projeto

A arquitetura do sistema foi desenhada para garantir baixo acoplamento e alta coesão:

```text
RBANK/
├── main.py                  # Ponto de entrada e montagem de arquivos estáticos
├── routes/
│   └── route.py             # Controladores (Endpoints web e injeção do Jinja2)
├── business/
│   └── service.py           # Regras de negócio (Validações de saque/depósito)
├── data/
│   └── mock_data.py         # Banco de dados simulado em memória
├── models/
│   └── conta.py             # Entidades do sistema
├── templates/
│   └── index.html           # Interface visual dinâmica (Jinja2)
└── static/
    └── css/
        └── style.css        # Folha de estilos separada
