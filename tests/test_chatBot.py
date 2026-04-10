import os
import sys
from unittest.mock import patch

caminho_base = os.path.dirname(__file__)
caminho_absoluto = os.path.abspath(os.path.join(caminho_base, '..'))
sys.path.insert(0, caminho_absoluto)

from src import chatbot  # noqa: E402


# 1. TESTE DE CAMINHO FELIZ
@patch('src.chatbot.salvar_dados')
@patch('src.chatbot.carregar_dados', return_value=[])
@patch('builtins.input', side_effect=['s', 's', 'n'])
def test_fazer_perg_feliz(mock_input, mock_carregar, mock_salvar):
    chatbot.fazer_perguntas()
    assert mock_salvar.called
    args, _ = mock_salvar.call_args
    dados_salvos = args[0]
    assert len(dados_salvos) == 1
    assert dados_salvos[0]['agua'] is True
    assert dados_salvos[0]['pausas'] is True
    assert dados_salvos[0]['alimentacao'] is False


# 2. TESTE DE ENTRADA INVÁLIDA
@patch('src.chatbot.salvar_dados')
@patch('src.chatbot.carregar_dados', return_value=[])
@patch('builtins.input', side_effect=['x', 's', 'n', 's'])
def test_fazer_perg_invalida(mock_input, mock_carregar, mock_salvar):
    chatbot.fazer_perguntas()
    assert mock_input.call_count == 4
    assert mock_salvar.called


# 3. TESTE DE CASO LIMITE
@patch('builtins.print')
@patch('src.chatbot.carregar_dados', return_value=[])
def test_relatorio_sem_dados(mock_carregar, mock_print):
    chatbot.exibir_relatorio()
    msg = "\n📭 Ainda não tem registos. Comece hoje mesmo!"
    mock_print.assert_called_with(msg)