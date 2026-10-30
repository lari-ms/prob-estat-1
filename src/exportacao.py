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



def exportar_experimento_2_csv(dados: Dict, caminho: str = "resultados/csvs/experimento2_medias_acumuladas.csv"):
    """
    Exporta a tabela de médias acumuladas do Experimento 2 para CSV.
    
    Args:
        dados: Resultado do experimento_2()
        caminho: Caminho do arquivo CSV
    """
    criar_diretorios_resultados()
    
    # Preparar tabela 3x3
    tabela_dados = []
    
    for semente in dados['sementes']:
        linha = {'Semente': semente}
        for ponto in dados['pontos_acumulacao']:
            if ponto in dados['medias_acumuladas'][semente]:
                media = dados['medias_acumuladas'][semente][ponto]
                linha[f'Média em {ponto:,} rodadas'] = f"{media:.6f}"
            else:
                linha[f'Média em {ponto:,} rodadas'] = 'N/A'
        tabela_dados.append(linha)
    
    # Adicionar linha da esperança teórica
    linha_teorica = {'Semente': 'E[X] teórico'}
    for ponto in dados['pontos_acumulacao']:
        linha_teorica[f'Média em {ponto:,} rodadas'] = f"{dados['esperanca_teorica']:.6f}"
    tabela_dados.append(linha_teorica)
    
    df = pd.DataFrame(tabela_dados)
    df.to_csv(caminho, index=False)
    
    return caminho


def exportar_trajetorias_experimento_2_csv(dados: Dict, caminho: str = "resultados/csvs/experimento2_trajetorias.csv"):
    """
    Exporta as trajetórias completas do Experimento 2 para CSV.
    
    Args:
        dados: Resultado do experimento_2()
        caminho: Caminho do arquivo CSV
    """
    criar_diretorios_resultados()
    
    # Preparar dados: cada coluna é uma semente
    tabela_dados = {'Rodada': list(range(1, dados['n_rodadas'] + 1))}
    
    for semente in dados['sementes']:
        tabela_dados[f'Média Acum. (semente {semente})'] = dados['trajetorias'][semente]
    
    df = pd.DataFrame(tabela_dados)
    df.to_csv(caminho, index=False, float_format='%.6f')
    
    return caminho


def exportar_experimento_3_csv(dados: Dict, caminho: str = "resultados/csvs/experimento3_resumo.csv"):
    """
    Exporta o resumo estatístico do Experimento 3 para CSV.
    
    Args:
        dados: Resultado do experimento_3()
        caminho: Caminho do arquivo CSV
    """
    criar_diretorios_resultados()
    
    # Tabela de resultados agregados
    resumo = {
        'Métrica': [
            'Número de participantes',
            'Saldo inicial (créditos)',
            'Máximo de rodadas',
            '',
            'Participantes que ganharam',
            'Participantes que empataram',
            'Participantes que perderam',
            'Participantes que zeraram',
            '',
            'Proporção que ganhou (%)',
            'Proporção que empatou (%)',
            'Proporção que perdeu (%)',
            'Proporção que zerou (%)',
            '',
            'Média de saldo final (créditos)',
            'Mediana de saldo final (créditos)',
            'Perda média (créditos)',
            'Perda média (%)',
            '',
            'Média de rodadas jogadas',
            'Mediana de rodadas jogadas'
        ],
        'Valor': [
            dados['n_participantes'],
            dados['saldo_inicial'],
            dados['max_rodadas'],
            '',
            dados['ganhou'],
            dados['empatou'],
            dados['perdeu'],
            dados['zerou_saldo'],
            '',
            f"{dados['proporcao_ganhou']*100:.2f}",
            f"{dados['proporcao_empatou']*100:.2f}",
            f"{dados['proporcao_perdeu']*100:.2f}",
            f"{dados['proporcao_zerou']*100:.2f}",
            '',
            f"{dados['media_saldo_final']:.2f}",
            f"{dados['mediana_saldo_final']:.2f}",
            f"{dados['saldo_inicial'] - dados['media_saldo_final']:.2f}",
            f"{(1 - dados['media_saldo_final']/dados['saldo_inicial'])*100:.2f}",
            '',
            f"{dados['media_rodadas']:.1f}",
            f"{dados['mediana_rodadas']:.0f}"
        ]
    }
    
    df = pd.DataFrame(resumo)
    df.to_csv(caminho, index=False)
    
    return caminho


def exportar_participantes_experimento_3_csv(dados: Dict, caminho: str = "resultados/csvs/experimento3_participantes.csv"):
    """
    Exporta os dados individuais de cada participante do Experimento 3 para CSV.
    
    Args:
        dados: Resultado do experimento_3()
        caminho: Caminho do arquivo CSV
    """
    criar_diretorios_resultados()
    
    # Preparar dados individuais
    tabela_dados = []
    
    for p in dados['participantes']:
        tabela_dados.append({
            'ID': p['id'],
            'Saldo Inicial': p['saldo_inicial'],
            'Saldo Final': p['saldo_final'],
            'Número de Rodadas': p['n_rodadas'],
            'Zerou': 'Sim' if p['zerou'] else 'Não',
            'Resultado': 'Ganhou' if p['ganhou'] else ('Empatou' if p['empatou'] else 'Perdeu'),
            'Variação Saldo': p['saldo_final'] - p['saldo_inicial'],
            'Variação %': f"{((p['saldo_final'] / p['saldo_inicial']) - 1) * 100:.2f}"
        })
    
    df = pd.DataFrame(tabela_dados)
    df.to_csv(caminho, index=False)
    
    return caminho


def exportar_experimento_4_csv(dados: Dict, caminho: str = "resultados/csvs/experimento4_condicional.csv"):
    """
    Exporta a tabela do Experimento 4 (probabilidade condicional) para CSV.
    
    Args:
        dados: Resultado do experimento_4()
        caminho: Caminho do arquivo CSV
    """
    criar_diretorios_resultados()
    
    nomes = {'apos_premio': 'Prêmio (P > 0)', 'apos_nao_premio': 'Sem prêmio (P = 0)'}
    
    tabela_dados = []
    for chave, nome in nomes.items():
        g = dados['grupos'][chave]
        tabela_dados.append({
            'Resultado anterior': nome,
            'Total de pares': g['total_pares'],
            'Prêmios na rodada seguinte': g['premios_seguinte'],
            'Proporção': ('não estimável' if g['proporcao'] is None
                          else f"{g['proporcao']:.6f}"),
            'Referência do modelo': f"{dados['probabilidade_teorica']:.6f}"
        })
    
    df = pd.DataFrame(tabela_dados)
    df.to_csv(caminho, index=False)
    
    return caminho


def exportar_experimento_5_csv(dados: Dict, caminho: str = "resultados/csvs/experimento5_comparacao.csv"):
    """
    Exporta a comparação entre tabelas de pagamento do Experimento 5 para CSV.
    
    Args:
        dados: Resultado do experimento_5()
        caminho: Caminho do arquivo CSV
    """
    criar_diretorios_resultados()
    
    tabela_dados = []
    for nome, m in dados['tabelas'].items():
        tabela_dados.append({
            'Tabela': nome,
            'Probabilidade de prêmio (teórica)': m['prob_premio_teorica'],
            'Frequência de prêmio (observada)': m['freq_premio_observada'],
            'Prêmio médio (observado)': m['premio_medio'],
            'Lucro médio (observado)': m['lucro_medio'],
            'Lucro esperado (teórico)': m['lucro_esperado_teorico'],
            'RTP teórico (%)': m['rtp_teorico'] * 100,
            'RTP observado (%)': m['rtp_observado'] * 100
        })
    
    df = pd.DataFrame(tabela_dados)
    df.to_csv(caminho, index=False, float_format='%.6f')
    
    return caminho
