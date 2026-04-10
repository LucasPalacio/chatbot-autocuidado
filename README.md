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
## 🚀 Como Instalar e Executar (Localmente)
| **1. Clone o repositório** | `git clone https://github.com/LucasPalacio/chatbot-autocuidado.git`<br>`cd chatbot-autocuidado` |
| **2. Instale as dependências exigidas** | `pip install -r requirements.txt` |
| **3. Inicie o Assistente** | `python src/chatbot.py` |
 ## **  🧪 Qualidade de Código (Testes e Lint) **
| Este projeto garante sua estabilidade através de testes automatizados (cobrindo o "caminho feliz", "entradas inválidas" e "casos limite" da interface CLI) e verificação de estilo. |
| **Para executar os Testes Automatizados** | `pytest -v` |
| **Para executar a Análise Estática de Código** | `python -m flake8 src/ tests/` |




