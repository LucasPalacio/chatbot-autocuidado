import pytest
from unittest.mock import patch
import sys
import os

# Isso garante que a pasta 'src' seja encontrada pelos testes
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src import chatbot

# 1. TESTE DE CAMINHO FELIZ (Comportamento Correto)
# Simulamos o usuário digitando 's', 's' e 'n'
@patch('src.chatbot.salvar_dados')
@patch('src.chatbot.carregar_dados', return_value=[])
@patch('builtins.input', side_effect=['s', 's', 'n'])
def test_fazer_perguntas_caminho_feliz(mock_input, mock_carregar, mock_salvar):
    chatbot.fazer_perguntas()
    
    # Verifica se a função de salvar foi chamada
    assert mock_salvar.called
    
    # Verifica se os dados salvos estão corretos
    args, kwargs = mock_salvar.call_args
    dados_salvos = args[0]
    
    assert len(dados_salvos) == 1
    assert dados_salvos[0]['agua'] == True
    assert dados_salvos[0]['pausas'] == True
    assert dados_salvos[0]['alimentacao'] == False


# 2. TESTE DE ENTRADA INVÁLIDA
# Simulamos o usuário digitando 'x' (errado), e depois acertando com 's', 'n', 's'
@patch('src.chatbot.salvar_dados')
@patch('src.chatbot.carregar_dados', return_value=[])
@patch('builtins.input', side_effect=['x', 's', 'n', 's'])
def test_fazer_perguntas_entrada_invalida(mock_input, mock_carregar, mock_salvar):
    chatbot.fazer_perguntas()
    
    # Se ele digitou 'x' primeiro, o bot deve ter repetido a pergunta
    # Logo, o input deve ter sido chamado 4 vezes no total, e não 3.
    assert mock_input.call_count == 4
    assert mock_salvar.called


# 3. TESTE DE CASO LIMITE
# O que acontece se o usuário pedir o relatório, mas não houver nenhum dado salvo?
@patch('builtins.print')
@patch('src.chatbot.carregar_dados', return_value=[])
def test_exibir_relatorio_sem_dados(mock_carregar, mock_print):
    chatbot.exibir_relatorio()
    
    # Verifica se o bot imprimiu a mensagem correta avisando que não há registros
    mock_print.assert_called_with("\n📭 Ainda não tem registos. Comece hoje mesmo!")