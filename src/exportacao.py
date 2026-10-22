"""
Módulo exportacao.py
Implementa funções para exportar resultados em CSV e salvar gráficos.
"""

import os
import pandas as pd
from typing import Dict, Any
from pathlib import Path


def criar_diretorios_resultados():
    """Cria os diretórios para armazenar resultados se não existirem."""
    Path("resultados/csvs").mkdir(parents=True, exist_ok=True)
    Path("resultados/graficos").mkdir(parents=True, exist_ok=True)


def exportar_experimento_1_csv(dados: Dict, caminho: str = "resultados/csvs/experimento1_frequencias.csv"):
    """
    Exporta os resultados do Experimento 1 para CSV.
    
    Args:
        dados: Resultado do experimento_1()
        caminho: Caminho do arquivo CSV
    """
    criar_diretorios_resultados()
    
    # Preparar dados para tabela
    lucros = sorted(dados['contagens'].keys())
    
    tabela_dados = []
    for lucro in lucros:
        tabela_dados.append({
            'Lucro (X)': lucro,
            'Probabilidade Teórica': dados['probabilidades_teoricas'][lucro],
            'Contagem Observada': dados['contagens'][lucro],
            'Frequência Relativa': dados['frequencias'][lucro],
            'Diferença (Freq - Prob)': dados['frequencias'][lucro] - dados['probabilidades_teoricas'][lucro]
        })
    
    df = pd.DataFrame(tabela_dados)
    df.to_csv(caminho, index=False, float_format='%.6f')
    
    return caminho


def exportar_metricas_experimento_1_csv(dados: Dict, caminho: str = "resultados/csvs/experimento1_metricas.csv"):
    """
    Exporta as métricas resumidas do Experimento 1 para CSV.
    
    Args:
        dados: Resultado do experimento_1()
        caminho: Caminho do arquivo CSV
    """
    criar_diretorios_resultados()
    
    metricas = {
        'Métrica': [
            'Número de rodadas',
            'Semente',
            'Lucro médio observado (créditos)',
            'Lucro esperado teórico (créditos)',
            'RTP observado (%)',
            'RTP teórico (%)',
            'Proporção de prêmios observada (%)',
            'Proporção de prêmios teórica (%)',
            'Prêmios observados',
            'Prêmios esperados',
            'Desvio-padrão amostral (créditos)'
        ],
        'Valor': [
            dados['n_rodadas'],
            dados['semente'],
            f"{dados['lucro_medio']:.6f}",
            "-0.160000",
            f"{dados['rtp_observado']*100:.2f}",
            f"{dados['rtp_teorico']*100:.2f}",
            f"{dados['proporcao_premios']*100:.2f}",
            "4.00",
            dados['premios_observados'],
            f"{dados['premios_esperados']:.0f}",
            f"{dados['desvio_padrao']:.6f}"
        ]
    }
    
    df = pd.DataFrame(metricas)
    df.to_csv(caminho, index=False)
    
    return caminho


def salvar_configuracao_execucao(experimento: str, parametros: Dict, caminho: str = None):
    """
    Salva a configuração de execução de um experimento.
    
    Args:
        experimento: Nome do experimento (ex: 'experimento_1')
        parametros: Dicionário com parâmetros usados
        caminho: Caminho do arquivo. Se None, usa padrão.
    """
    criar_diretorios_resultados()
    
    if caminho is None:
        caminho = f"resultados/csvs/{experimento}_configuracao.csv"
    
    config_dados = []
    for chave, valor in parametros.items():
        config_dados.append({
            'Parâmetro': chave,
            'Valor': valor
        })
    
    df = pd.DataFrame(config_dados)
    df.to_csv(caminho, index=False)
    
    return caminho
