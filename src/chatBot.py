import streamlit as st
import requests
import json
from datetime import datetime

# Configuração da API (Use sua chave ou uma pública de teste)
API_KEY = "b1b15e88fa7972254124657c11294470" # Exemplo

def buscar_clima(cidade):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric"
    try:
        res = requests.get(url)
        return res.json()
    except:
        return None

st.set_page_config(page_title="Assistente de Autocuidado", page_icon="💧")

st.title("💧 Assistente de Autocuidado")

# --- INTEGRAÇÃO COM API ---
cidade = st.text_input("Em qual cidade você está?", "Sao Paulo")
dados_clima = buscar_clima(cidade)

if dados_clima and dados_clima.get("main"):
    temp = dados_clima["main"]["temp"]
    st.info(f"🌡️ Temperatura atual em {cidade}: {temp}°C")
    if temp > 28:
        st.warning("Está calor! Recomendamos beber 500ml de água extra agora.")

# --- FORMULÁRIO GUI ---
st.subheader("Checklist de Hoje")
with st.form("meu_form"):
    agua = st.checkbox("Bebeu 2L de água?")
    pausas = st.checkbox("Fez pausas para alongar?")
    alimentacao = st.checkbox("Comeu frutas/vegetais?")
    
    submetido = st.form_submit_button("Salvar Progresso")
    
    if submetido:
        novo_registro = {
            "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "agua": agua,
            "pausas": pausas,
            "alimentacao": alimentacao,
            "temp_local": temp if dados_clima else None
        }
        # Aqui você pode manter sua lógica de salvar em JSON ou apenas mostrar na tela
        st.success("✅ Registrado com sucesso!")
        st.balloons()