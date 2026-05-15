import pytest
import requests
from unittest.mock import patch

def test_api_clima_conexao():
    # Testa se a API responde (pode usar mock para não gastar sua cota de API)
    url = "http://api.openweathermap.org/data/2.5/weather?q=London&appid=b1b15e88fa7972254124657c11294470"
    response = requests.get(url)
    assert response.status_code == 200 # Garante que a comunicação funciona