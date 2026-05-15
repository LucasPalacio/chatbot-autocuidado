import os
import sys
from unittest.mock import patch

# Força o Python a enxergar a pasta 'src' corretamente na nuvem
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.chatBot import buscar_clima  # noqa: E402


@patch('src.chatBot.requests.get')
def test_comunicacao_api_clima(mock_get):
    """Teste de integracao: valida a comunicacao simulada com a API wttr.in."""
    mock_resposta = mock_get.return_value
    mock_resposta.status_code = 200
    mock_resposta.json.return_value = {
        'current_condition': [{'temp_C': '25'}]
    }

    resultado = buscar_clima("Sao Paulo")

    assert resultado is not None
    assert "main" in resultado
    assert resultado["main"]["temp"] == 25


@patch('src.chatBot.requests.get')
def test_comunicacao_api_falha(mock_get):
    """Teste de integracao: valida como o sistema reage se a API cair."""
    mock_resposta = mock_get.return_value
    mock_resposta.status_code = 404

    resultado = buscar_clima("Atlantida")

    assert resultado is None