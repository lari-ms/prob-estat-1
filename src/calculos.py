"""
Módulo calculos.py
Implementa cálculos de probabilidades teóricas, esperanças e métricas estatísticas.
"""

from typing import Dict, Tuple
from src.maquina import SIMBOLOS, TABELA_BASE


def calcular_probabilidades_teoricas(tabela: Dict = None) -> Dict[float, float]:
    """
    Calcula as probabilidades teóricas de cada lucro possível.
    
    O espaço amostral tem 5³ = 125 combinações centrais equiprováveis.
    Cada tripla específica tem probabilidade 1/125.
    
    Args:
        tabela: Tabela de pagamentos. Se None, usa TABELA_BASE
        
    Returns:
        dict: {lucro: probabilidade} para todos os lucros possíveis
    """
    if tabela is None:
        tabela = TABELA_BASE
    
    # Probabilidade de cada tripla premiada: 1/125
    prob_tripla = 1 / 125
    
    # Contagem de triplas para cada lucro
    distribuicao = {}
    
    # Triplas premiadas
    for combinacao, premio in tabela.items():
        lucro = premio - 1
        distribuicao[lucro] = distribuicao.get(lucro, 0) + prob_tripla
    
    # Triplas não premiadas: 125 - 5 = 120
    lucro_perda = -1.0
    distribuicao[lucro_perda] = 120 / 125
    
    return distribuicao


def calcular_esperanca_premio(tabela: Dict = None) -> float:
    """
    Calcula o prêmio esperado E[P].
    
    Args:
        tabela: Tabela de pagamentos. Se None, usa TABELA_BASE
        
    Returns:
        float: Esperança do prêmio bruto
    """
    if tabela is None:
        tabela = TABELA_BASE
    
    prob_tripla = 1 / 125
    
    soma = 0
    for premio in tabela.values():
        soma += premio * prob_tripla
    
    return soma


def calcular_esperanca_lucro(tabela: Dict = None) -> float:
    """
    Calcula o lucro esperado E[X] = E[P] - 1.
    
    Args:
        tabela: Tabela de pagamentos. Se None, usa TABELA_BASE
        
    Returns:
        float: Esperança do lucro líquido
    """
    return calcular_esperanca_premio(tabela) - 1


def calcular_rtp_teorico(tabela: Dict = None) -> float:
    """
    Calcula o RTP (Return to Player) teórico.
    
    RTP = E[P] / aposta
    Com aposta fixa de 1 crédito, RTP = E[P]
    
    Args:
        tabela: Tabela de pagamentos. Se None, usa TABELA_BASE
        
    Returns:
        float: RTP como proporção (ex: 0.84 = 84%)
    """
    return calcular_esperanca_premio(tabela)


def calcular_probabilidade_premio(tabela: Dict = None) -> float:
    """
    Calcula a probabilidade de receber algum prêmio.
    
    Args:
        tabela: Tabela de pagamentos. Se None, usa TABELA_BASE
        
    Returns:
        float: P(prêmio > 0) como proporção
    """
    if tabela is None:
        tabela = TABELA_BASE
    
    n_triplas_premiadas = len(tabela)
    return n_triplas_premiadas / 125


def obter_valores_teoricos_referencia(tabela: Dict = None) -> Dict:
    """
    Retorna todos os valores teóricos de referência do modelo.
    
    Args:
        tabela: Tabela de pagamentos. Se None, usa TABELA_BASE
        
    Returns:
        dict: Dicionário com todos os valores teóricos
    """
    prob_premio = calcular_probabilidade_premio(tabela)
    
    return {
        'espaco_amostral': 125,
        'n_triplas_premiadas': 5 if tabela is None or tabela == TABELA_BASE else len(tabela),
        'prob_premio': prob_premio,
        'prob_sem_premio': 1 - prob_premio,
        'esperanca_premio': calcular_esperanca_premio(tabela),
        'esperanca_lucro': calcular_esperanca_lucro(tabela),
        'rtp': calcular_rtp_teorico(tabela),
        'vantagem_operador': 1 - calcular_rtp_teorico(tabela),
        'distribuicao_lucro': calcular_probabilidades_teoricas(tabela)
    }


def validar_valores_teoricos_tabela_base() -> Tuple[bool, str]:
    """
    Valida se os cálculos produzem os valores teóricos esperados para a tabela base.
    
    Valores de referência do enunciado:
    - E[P] = 0.84
    - E[X] = -0.16
    - RTP = 84%
    - P(prêmio) = 4%
    - P(sem prêmio) = 96%
    
    Returns:
        tuple: (validação_ok: bool, mensagem: str)
    """
    valores = obter_valores_teoricos_referencia(TABELA_BASE)
    
    tolerancia = 1e-10
    
    # Validações
    validacoes = [
        (abs(valores['esperanca_premio'] - 0.84) < tolerancia, 
         f"E[P] = {valores['esperanca_premio']:.10f}, esperado 0.84"),
        
        (abs(valores['esperanca_lucro'] - (-0.16)) < tolerancia,
         f"E[X] = {valores['esperanca_lucro']:.10f}, esperado -0.16"),
        
        (abs(valores['rtp'] - 0.84) < tolerancia,
         f"RTP = {valores['rtp']:.10f}, esperado 0.84"),
        
        (abs(valores['prob_premio'] - 0.04) < tolerancia,
         f"P(prêmio) = {valores['prob_premio']:.10f}, esperado 0.04"),
        
        (abs(valores['prob_sem_premio'] - 0.96) < tolerancia,
         f"P(sem prêmio) = {valores['prob_sem_premio']:.10f}, esperado 0.96"),
        
        (valores['espaco_amostral'] == 125,
         f"Espaço amostral = {valores['espaco_amostral']}, esperado 125"),
    ]
    
    erros = [msg for ok, msg in validacoes if not ok]
    
    if erros:
        return False, "Erros de validação:\n" + "\n".join(erros)
    
    return True, "Todos os valores teóricos validados com sucesso!"


def validar_valores_teoricos_tabela_aumentada() -> Tuple[bool, str]:
    """
    Valida os valores teóricos para a tabela com pagamentos aumentados em 10%.
    
    Valores de referência do enunciado:
    - E[P] = 0.924
    - E[X] = -0.076
    - RTP = 92.4%
    - P(prêmio) = 4% (inalterada)
    
    Returns:
        tuple: (validação_ok: bool, mensagem: str)
    """
    from src.maquina import TABELA_AUMENTADA_10PCT
    
    valores = obter_valores_teoricos_referencia(TABELA_AUMENTADA_10PCT)
    
    tolerancia = 1e-10
    
    validacoes = [
        (abs(valores['esperanca_premio'] - 0.924) < tolerancia,
         f"E[P] = {valores['esperanca_premio']:.10f}, esperado 0.924"),
        
        (abs(valores['esperanca_lucro'] - (-0.076)) < tolerancia,
         f"E[X] = {valores['esperanca_lucro']:.10f}, esperado -0.076"),
        
        (abs(valores['rtp'] - 0.924) < tolerancia,
         f"RTP = {valores['rtp']:.10f}, esperado 0.924"),
        
        (abs(valores['prob_premio'] - 0.04) < tolerancia,
         f"P(prêmio) = {valores['prob_premio']:.10f}, esperado 0.04 (inalterada)"),
    ]
    
    erros = [msg for ok, msg in validacoes if not ok]
    
    if erros:
        return False, "Erros de validação:\n" + "\n".join(erros)
    
    return True, "Tabela aumentada validada com sucesso!"
