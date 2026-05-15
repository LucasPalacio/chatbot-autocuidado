# 💧 Assistente de Autocuidado e Hidratação (CLI)

[![Validacao Continua (CI)](https://github.com/LucasPalacio/chatbot-autocuidado/actions/workflows/ci.yml/badge.svg)](https://github.com/LucasPalacio/chatbot-autocuidado/actions/workflows/ci.yml)

**Versão Atual:** 1.0.0

---

## 🎯 Visão Geral e Problema Real
Este projeto é uma aplicação de Linha de Comando (CLI) desenvolvida em Python. Ele nasceu para mitigar uma **dor real e altamente relevante na sociedade moderna**: o esquecimento de hábitos básicos de manutenção da saúde (como beber água, fazer pausas ergonômicas e manter uma alimentação mínima) devido ao hiperfoco e à rotina exaustiva de trabalho ou estudos em frente às telas.

O objetivo não é ser um sistema médico complexo, mas sim uma ferramenta de **intervenção comportamental simples e de baixo atrito**, que estimula o usuário a refletir sobre o seu autocuidado diário através de um checklist rápido ao final do dia.

## 👥 Público-Alvo
* Estudantes universitários;
* Desenvolvedores e profissionais de TI;
* Trabalhadores em regime de home-office;
* Qualquer pessoa que passe longas horas ininterruptas no computador.

## ✨ Funcionalidades Principais
1. **Checklist Interativo:** O assistente realiza perguntas objetivas sobre o consumo de água, pausas e alimentação.
2. **Validação de Entrada:** O sistema é imune a respostas inválidas, garantindo que o fluxo não quebre caso o usuário digite comandos não reconhecidos (aceita estritamente `s` ou `n`).
3. **Persistência de Dados em Arquivo:** Utiliza um banco de dados leve e embutido através de arquivos `.json` (`progresso.json`), garantindo que o histórico não se perca entre as sessões, sem a necessidade de instalar SGBDs externos.
4. **Relatório de Progresso:** Feedback visual e imediato do histórico do usuário, gamificando levemente a experiência (atribuindo a insígnia 🌟 para dias perfeitos).

## 🛠️ Stack Tecnológica e Ferramentas
Este projeto foi construído seguindo as melhores práticas da engenharia de software contemporânea:
* **Linguagem:** Python 3.11+
* **Interface:** CLI (Command Line Interface)
* **Armazenamento:** Módulo nativo `json`
* **Testes Automatizados:** `pytest` e `unittest.mock`
* **Análise Estática (Linting):** `flake8` (padrão PEP 8)
* **Integração Contínua (CI):** GitHub Actions (Pipeline automatizada configurada em `.github/workflows/ci.yml`)


## 📁 Estrutura do Projeto
```text
chatbot-autocuidado/
├── .github/
│   └── workflows/
│       └── ci.yml             # Pipeline de Integração Contínua
├── src/
│   ├── __init__.py
│   └── chatbot.py             # Código-fonte principal da aplicação
├── tests/
│   ├── __init__.py
│   └── test_chatbot.py        # Testes unitários automatizados
├── .gitignore                 # Arquivos ignorados pelo Git
├── README.md                  # Documentação do projeto
└── requirements.txt           # Declaração explícita de dependências
```
## 🚀 Como Instalar e Executar (Localmente) Para rodar este projeto na sua máquina, siga os passos abaixo. Você precisará ter o Python e o Git instalados.
| Passo / Tópico | Descrição |
| :--- | :--- |
| **1. Clone o repositório** | `git clone https://github.com/LucasPalacio/chatbot-autocuidado.git`<br>`cd chatbot-autocuidado` |
| **2. Instale as dependências exigidas** | `pip install -r requirements.txt` |
| **3. Inicie o Assistente** | `python src/chatbot.py` |
| **🧪 Qualidade de Código (Testes e Lint)** | Este projeto garante sua estabilidade através de testes automatizados (cobrindo o "caminho feliz", "entradas inválidas" e "casos limite" da interface CLI) e verificação de estilo. |
| **Para executar os Testes Automatizados** | `pytest -v` |
| **Para executar a Análise Estática de Código** | `python -m flake8 src/ tests/` |

## incluir prints, GIF ou exemplos de uso no README
<img width="1920" height="1032" alt="Captura de tela 2026-04-10 021421" src="https://github.com/user-attachments/assets/659e2f1d-8273-477e-b618-aebdfdd3ee6a" />
 <img width="1920" height="1032" alt="Captura de tela 2026-04-10 022008" src="https://github.com/user-attachments/assets/2fda302d-9d11-4f2a-950e-1cacfeb9236d" />
 <img width="1920" height="1032" alt="Captura de tela 2026-04-10 022725" src="https://github.com/user-attachments/assets/89407787-5e52-41a9-8a08-f89aea4e8cf9" />
 



| Tópico | Descrição |
| :--- | :--- |
| **1. sem registro** | isso acontonce quando não temos informações de uma lista de saber do autocuidamento quando não foi adcionado <br>.|
| **2. Registrado** | `conseguimos registrar quando confirmamos a nossa rotina de confirmação de meta de agua ou comidas saudaveis.` |
| **3. Historico** | `Registra todas os relatorios enviados do usuario para ele ver seu progesso.` |
| **❌ Invalido** |no exemplo da imagem 3 temos uma invalides em cima em que só acontece quando não respodemos s ou n. |
| **Sair** | Ao clicar nele saimos do autocuidado |


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 💧 Assistente de Autocuidado e Hidratação

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_svg)](https://chatbot-autocuidado-ncdthw6sjetzqucn8jmae3.streamlit.app/)
[![Validação Contínua (CI)](https://github.com/LucasPalacio/chatbot-autocuidado/actions/workflows/ci.yml/badge.svg)](https://github.com/LucasPalacio/chatbot-autocuidado/actions/workflows/ci.yml)

**Acesse a Aplicação Online:** [Clique aqui para abrir o Assistente](https://chatbot-autocuidado-ncdthw6sjetzqucn8jmae3.streamlit.app/)

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





