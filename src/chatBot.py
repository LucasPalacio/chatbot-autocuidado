import streamlit as st
import requests
import json
import os
from datetime import datetime

DATA_FILE = "progresso.json"
API_KEY = "b1b15e88fa7972254124657c11294470"  # Chave de teste do OpenWeatherMap


def carregar_dados():
    """Carrega dados do JSON ou cria lista vazia se não existir."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def salvar_dados(dados):
    """Guarda a lista de registros no arquivo JSON."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4)


def buscar_clima(cidade):
    """Busca os dados do clima na API do OpenWeatherMap."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric"
    try:
        res = requests.get(url)
        if res.status_code == 200:
            return res.json()
        return None
    except Exception:
        return None


# --- CONFIGURAÇÃO DA PÁGINA STREAMLIT ---
st.set_page_config(page_title="Assistente de Autocuidado", page_icon="💧")

st.title("💧 Assistente de Autocuidado")

# --- INTEGRAÇÃO COM API ---
cidade = st.text_input("Em qual cidade você está?", "Sao Paulo")
dados_clima = buscar_clima(cidade)

# A variável é iniciada vazia para evitar o NameError que deu no seu Streamlit
temp = None 

if dados_clima and dados_clima.get("main"):
    temp = dados_clima["main"]["temp"]
    st.info(f"🌡️ Temperatura atual em {cidade}: {temp}°C")
    if temp > 28:
        st.warning("Está calor! Recomendamos beber 500ml de água extra agora. 🥵")


# --- FORMULÁRIO GUI ---
st.subheader("Checklist de Hoje")
with st.form("meu_form"):
    agua = st.checkbox("Bebeu 2L de água?")
    pausas = st.checkbox("Fez pausas para alongar?")
    alimentacao = st.checkbox("Comeu frutas/vegetais?")
    
    submetido = st.form_submit_button("Salvar Progresso")
    
    if submetido:
        # Pega os dados antigos, adiciona o novo e salva
        dados_antigos = carregar_dados()
        
        novo_registro = {
            "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "agua": agua,
            "pausas": pausas,
            "alimentacao": alimentacao,
            "temp_local": temp  # Usando a variável de forma segura
        }
        
        dados_antigos.append(novo_registro)
        salvar_dados(dados_antigos)
        
        st.success("✅ Registrado com sucesso! Orgulhe-se de cuidar de si.")
        st.balloons()


# --- MOSTRAR RELATÓRIO NA TELA ---
st.write("---")
st.subheader("📊 Seu Histórico")
historico = carregar_dados()

if historico:
    # Mostra do registro mais novo para o mais velho
    for r in reversed(historico): 
        status = "🌟" if r['agua'] and r['pausas'] and r['alimentacao'] else "✅"
        temperatura = f"{r['temp_local']}°C" if r.get('temp_local') else "N/A"
        
        st.write(f"**{r['data']}** | {status} | Temp: {temperatura}")
else:
    st.write("📭 Ainda não tem registros. Comece hoje mesmo!")