import json
import os
from datetime import datetime

# Nome do ficheiro onde os dados serão guardados
DATA_FILE = "progresso.json"

def carregar_dados():
    """Carrega os dados do ficheiro JSON ou cria uma lista vazia se não existir."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_dados(dados):
    """Guarda a lista de registos no ficheiro JSON."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4)

def exibir_menu():
    print("\n--- 💧 ASSISTENTE DE AUTOCUIDADO ---")
    print("1. Registar hábitos de hoje")
    print("2. Ver meu relatório de progresso")
    print("3. Sair")
    return input("Escolha uma opção: ")

def fazer_perguntas():
    """Realiza o chatbot interactivo com validação de dados."""
    print("\nOlá! Vamos verificar os seus hábitos de hoje.")
    
    perguntas = [
        ("Bebeu pelo menos 2L de água hoje? (s/n): ", "agua"),
        ("Fez pausas para alongar durante o trabalho/estudo? (s/n): ", "pausas"),
        ("Consumiu frutas ou vegetais nas refeições? (s/n): ", "alimentacao")
    ]
    
    respostas_hoje = {"data": datetime.now().strftime("%d/%m/%Y")}
    
    for enunciado, chave in perguntas:
        while True:
            resposta = input(enunciado).lower().strip()
            if resposta in ['s', 'n']:
                respostas_hoje[chave] = (resposta == 's')
                break
            else:
                print("⚠️ Resposta inválida! Por favor, digite apenas 's' para sim ou 'n' para não.")
    
    dados = carregar_dados()
    dados.append(respostas_hoje)
    salvar_dados(dados)
    print("\n✅ Registado com sucesso! Orgulhe-se de cuidar de si.")

def exibir_relatorio():
    dados = carregar_dados()
    if not dados:
        print("\n📭 Ainda não tem registos. Comece hoje mesmo!")
        return

    print("\n--- 📊 O SEU PROGRESSO ---")
    for registo in dados:
        status = "🌟" if all([registo['agua'], registo['pausas'], registo['alimentacao']]) else "✅"
        print(f"Data: {registo['data']} | Status: {status}")
    print("--------------------------")

def main():
    while True:
        opcao = exibir_menu()
        if opcao == '1':
            fazer_perguntas()
        elif opcao == '2':
            exibir_relatorio()
        elif opcao == '3':
            print("Até logo! Continue a beber água! 💧")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()