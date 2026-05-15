import os
import sys
from unittest.mock import patch

# Garante que a pasta 'src' seja encontrada sem erros
caminho_base = os.path.dirname(__file__)
caminho_absoluto = os.path.abspath(os.path.join(caminho_base, '..'))
sys.path.insert(0, caminho_absoluto)

from src.chatbot import buscar_clima  # noqa: E402


@patch('src.chatbot.requests.get')
def test_comunicacao_api_clima(mock_get):
    """Teste de integracao: valida a comunicacao simulada com a API wttr.in."""
    # Preparamos o nosso "robô" para fingir que a API respondeu perfeitamente
    mock_resposta = mock_get.return_value
    mock_resposta.status_code = 200
    mock_resposta.json.return_value = {
        'current_condition': [{'temp_C': '25'}]
    }

    # Rodamos a função passando uma cidade
    resultado = buscar_clima("Sao Paulo")

    # Verificamos se o nosso código montou a temperatura certinha
    assert resultado is not None
    assert "main" in resultado
    assert resultado["main"]["temp"] == 25


@patch('src.chatbot.requests.get')
def test_comunicacao_api_falha(mock_get):
    """Teste de integracao: valida como o sistema reage se a API cair."""
    # Simulamos que o site da API está fora do ar (Erro 404)
    mock_resposta = mock_get.return_value
    mock_resposta.status_code = 404

    # Rodamos a função
    resultado = buscar_clima("Atlantida")

    # Se a API cair, o nosso bot não deve quebrar, deve apenas retornar None
    assert resultado is None
    