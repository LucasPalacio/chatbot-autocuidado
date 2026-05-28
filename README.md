entrega intermediaria 
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 💧 Assistente de Autocuidado e Hidratação

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_svg)](https://chatbot-autocuidado-ncdthw6sjetzqucn8jmae3.streamlit.app/)
[![Validação Contínua (CI)](https://github.com/LucasPalacio/chatbot-autocuidado/actions/workflows/ci.yml/badge.svg)](https://github.com/LucasPalacio/chatbot-autocuidado/actions/workflows/ci.yml)

**Acesse a Aplicação Online:** [Clique aqui para abrir o Assistente](https://chatbot-autocuidado-ncdthw6sjetzqucn8jmae3.streamlit.app/)
**git hub pages:** https://lucaspalacio.github.io/chatbot-autocuidado/

---

## 🎯 Sobre o Projeto
O **Assistente de Autocuidado** foi desenvolvido com o objetivo de resolver um problema real e contemporâneo: o esquecimento de hábitos básicos de saúde, como hidratação, alimentação e pausas ergonômicas, devido à rotina exaustiva de estudos e trabalho em frente ao computador.

O projeto foi construído em etapas, simulando um ambiente real de desenvolvimento de software, evoluindo de uma interface de linha de comando para uma aplicação web interativa.

---

## 🚀 Evolução do Software (Roadmap)

### 🚩 Fase 1: Entrega Inicial (MVP CLI)
O objetivo da primeira etapa foi tirar a ideia do papel e criar a fundação lógica do sistema.
* **Interface:** Interface de Linha de Comando (CLI).
* **Persistência de Dados:** Implementação de um banco de dados local utilizando arquivos `.json` para manter o histórico do usuário.
* **Qualidade:** Criação de testes automatizados básicos (cobrindo caminhos felizes e casos de erro) e configuração de análise estática de código (Linting/Flake8).
* **CI/CD:** Criação da primeira pipeline no GitHub Actions para garantir que nenhum código quebrado fosse para a branch principal.

### 🚩 Fase 2: Entrega Intermediária (Web GUI & API)
Nesta etapa, o foco foi a evolução da interface e a conexão com o mundo exterior.
* **Nova Interface:** Migração total do CLI para uma Interface Gráfica Web (GUI) moderna utilizando o framework **Streamlit**.
* **Integração com API Pública:** O assistente agora consome a API meteorológica `wttr.in` para verificar a temperatura atual da cidade do usuário e recomendar hidratação extra em dias quentes (>28°C).
* **Engenharia de Software:** Uso profissional de controle de versão (desenvolvimento focado na branch `entrega-intermediaria` vinculada a uma Issue).
* **Testes de Integração:** Implementação de testes robustos simulando falhas e sucessos da API externa utilizando a técnica de `Mocking` no Pytest.
* **Deploy:** Publicação da aplicação na nuvem via Streamlit Cloud.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.11
* **Framework Web:** Streamlit
* **Requisições HTTP:** Biblioteca `requests`
* **Testes Automatizados:** Pytest (com `unittest.mock`)
* **Qualidade de Código:** Flake8
* **CI/CD:** GitHub Actions
* **Hospedagem:** Streamlit Cloud

---

## ⚙️ Como Executar o Projeto Localmente

Caso deseje rodar a aplicação na sua própria máquina, siga os passos abaixo:

**1. Clone o repositório:**
```bash
git clone [https://github.com/LucasPalacio/chatbot-autocuidado.git](https://github.com/LucasPalacio/chatbot-autocuidado.git)
cd chatbot-autocuidado





