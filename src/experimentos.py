"""
Módulo experimentos.py
Implementa os cinco experimentos obrigatórios do trabalho.
"""

from typing import Dict, List, Tuple
import numpy as np
from src.maquina import executar_rodadas, TABELA_BASE, TABELA_AUMENTADA_10PCT
from src.calculos import (
    calcular_probabilidades_teoricas,
    calcular_esperanca_lucro,
    calcular_rtp_teorico,
    calcular_probabilidade_premio
)


def experimento_1(n: int = 10000, semente: int = 2026) -> Dict:
    """
    Experimento 1: Frequências e Probabilidades
    
    Executa n rodadas e compara frequências observadas com probabilidades teóricas.
    
    Args:
        n: Número de rodadas (padrão: 10.000)
        semente: Semente do gerador (padrão: 2026)
        
    Returns:
        dict: {
            'n_rodadas': int,
            'semente': int,
            'resultados': list com todas as rodadas,
            'contagens': dict {lucro: quantidade},
            'frequencias': dict {lucro: frequência relativa},
            'probabilidades_teoricas': dict {lucro: probabilidade},
            'lucro_medio': float,
            'rtp_observado': float,
            'rtp_teorico': float,
            'proporcao_premios': float,
            'desvio_padrao': float,
            'premios_observados': int,
            'premios_esperados': float
        }
    """
    # Executar rodadas
    resultados = executar_rodadas(n, semente, TABELA_BASE)
    
    # Extrair lucros
    lucros = [r['lucro'] for r in resultados]
    premios = [r['premio'] for r in resultados]
    
    # Contar frequências
    lucros_possiveis = [-1, 4, 9, 14, 24, 49]
    contagens = {lucro: lucros.count(lucro) for lucro in lucros_possiveis}
    
    # Calcular frequências relativas
    frequencias = {lucro: contagens[lucro] / n for lucro in lucros_possiveis}
    
    # Probabilidades teóricas
    prob_teoricas = calcular_probabilidades_teoricas(TABELA_BASE)
    
    # Métricas
    lucro_medio = np.mean(lucros)
    soma_premios = sum(premios)
    total_apostado = n * 1  # Aposta unitária
    rtp_observado = soma_premios / total_apostado
    rtp_teorico = calcular_rtp_teorico(TABELA_BASE)
    
    # Proporção de prêmios
    premios_observados = sum(1 for p in premios if p > 0)
    proporcao_premios = premios_observados / n
    
    # Desvio-padrão amostral (divisor N-1)
    desvio_padrao = np.std(lucros, ddof=1)
    
    # Prêmios esperados
    prob_premio_teorica = calcular_probabilidade_premio(TABELA_BASE)
    premios_esperados = n * prob_premio_teorica
    
    return {
        'n_rodadas': n,
        'semente': semente,
        'resultados': resultados,  # Para reutilização em experimentos futuros
        'contagens': contagens,
        'frequencias': frequencias,
        'probabilidades_teoricas': prob_teoricas,
        'lucro_medio': lucro_medio,
        'rtp_observado': rtp_observado,
        'rtp_teorico': rtp_teorico,
        'proporcao_premios': proporcao_premios,
        'desvio_padrao': desvio_padrao,
        'premios_observados': premios_observados,
        'premios_esperados': premios_esperados
    }


def interpretar_experimento_1(dados: Dict) -> str:
    """
    Gera interpretação textual do Experimento 1.
    
    Args:
        dados: Resultado do experimento_1()
        
    Returns:
        str: Texto de interpretação
    """
    interpretacao = []
    
    # Introdução
    interpretacao.append(
        f"Foram executadas {dados['n_rodadas']:,} rodadas com semente {dados['semente']}. "
        f"A Tabela apresenta a comparação entre as probabilidades teóricas e as "
        f"frequências observadas."
    )
    
    # Lucro médio
    diff_lucro = abs(dados['lucro_medio'] - calcular_esperanca_lucro())
    interpretacao.append(
        f"\nO lucro médio observado foi de {dados['lucro_medio']:.4f} créditos, "
        f"com diferença de {diff_lucro:.4f} em relação ao valor teórico de -0,1600. "
        f"Essa diferença é esperada devido à flutuação amostral."
    )
    
    # RTP
    diff_rtp = abs(dados['rtp_observado'] - dados['rtp_teorico'])
    interpretacao.append(
        f"\nO RTP observado foi de {dados['rtp_observado']*100:.2f}%, "
        f"próximo do valor teórico de {dados['rtp_teorico']*100:.2f}%. "
        f"A diferença de {diff_rtp*100:.2f} pontos percentuais está dentro do esperado "
        f"para uma amostra deste tamanho."
    )
    
    # Proporção de prêmios
    interpretacao.append(
        f"\nForam observadas {dados['premios_observados']:,} rodadas premiadas "
        f"({dados['proporcao_premios']*100:.2f}%), enquanto o valor teórico é de 4,00%. "
        f"Esperavam-se {dados['premios_esperados']:.0f} prêmios em média."
    )
    
    # Dispersão
    interpretacao.append(
        f"\nO desvio-padrão amostral foi de {dados['desvio_padrao']:.4f} créditos, "
        f"indicando alta variabilidade nos resultados individuais, mesmo com lucro médio negativo."
    )
    
    # Lei dos Grandes Números
    interpretacao.append(
        f"\n\nAs frequências observadas aproximam-se das probabilidades teóricas, "
        f"conforme esperado pela Lei dos Grandes Números. Com {dados['n_rodadas']:,} rodadas, "
        f"a média amostral converge para a esperança matemática, mas flutuações individuais "
        f"permanecem significativas."
    )
    
    # Distinção RTP vs P(prêmio)
    interpretacao.append(
        f"\n\nÉ fundamental distinguir a proporção de prêmios ({dados['proporcao_premios']*100:.2f}%) "
        f"do RTP ({dados['rtp_observado']*100:.2f}%). O primeiro indica a frequência de vitórias, "
        f"enquanto o segundo mede quanto dos créditos apostados retorna em forma de prêmios. "
        f"Mesmo com RTP de 84%, o jogador tem esperança de perda de 16% por rodada."
    )
    
    return ''.join(interpretacao)


# Armazenamento global dos resultados para reutilização
_cache_experimento_1 = None


def obter_resultados_experimento_1(forcar_nova_execucao: bool = False) -> Dict:
    """
    Retorna os resultados do Experimento 1, executando se necessário ou reutilizando cache.
    
    Args:
        forcar_nova_execucao: Se True, força nova execução mesmo com cache
        
    Returns:
        dict: Resultados do experimento_1()
    """
    global _cache_experimento_1
    
    if _cache_experimento_1 is None or forcar_nova_execucao:
        _cache_experimento_1 = experimento_1()
    
    return _cache_experimento_1
