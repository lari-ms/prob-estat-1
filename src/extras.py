"""
Módulo extras.py
Implementa os itens extras do trabalho:
- Extra A: Intervalos de confiança (até 4 pontos)
- Extra B: Mesma média, riscos diferentes (até 4 pontos)

Simulador acadêmico - somente créditos fictícios
"""

import math
import random
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from src.maquina import (
    TABELA_BASE,
    executar_rodada,
    executar_rodadas,
    calcular_premio,
    calcular_lucro
)
from src.calculos import (
    calcular_esperanca_lucro,
    calcular_rtp_teorico,
    calcular_probabilidade_premio
)


# Cores das séries (paleta categorica validada para daltonismo, em ordem fixa)
CORES_SERIES = ['#2a78d6', '#eb6834', '#1baf7a']
COR_REFERENCIA = '#4a4a46'
COR_FORA = '#eb6834'


# ==============================================================================
# EXTRA A: INTERVALOS DE CONFIANÇA
# ==============================================================================

Z_95 = 1.959964  # quantil 0,975 da normal padrão


def intervalo_confianca_media(valores: List[float], z: float = Z_95) -> Dict:
    """
    Intervalo de confiança para a média pela aproximação normal (TCL):
    média ± z · s/√n, com s o desvio-padrão amostral (divisor n-1).

    Args:
        valores: Observações (ex.: lucros de cada rodada)
        z: Quantil da normal padrão (padrão: 1,96 para 95%)

    Returns:
        dict: {'n', 'media', 'desvio_padrao', 'erro_padrao', 'margem', 'inferior', 'superior'}
    """
    n = len(valores)
    if n < 2:
        raise ValueError(f"São necessárias pelo menos 2 observações, recebido: {n}")

    media = float(np.mean(valores))
    desvio = float(np.std(valores, ddof=1))
    erro_padrao = desvio / math.sqrt(n)
    margem = z * erro_padrao

    return {
        'n': n,
        'media': media,
        'desvio_padrao': desvio,
        'erro_padrao': erro_padrao,
        'margem': margem,
        'inferior': media - margem,
        'superior': media + margem
    }


def extra_intervalos_confianca(resultados_e1: List[Dict] = None,
                               n_execucoes: int = 200,
                               n_rodadas: int = 10000,
                               marcos: Tuple[int, ...] = (100, 1000, 10000)) -> Dict:
    """
    Extra A: Intervalos de confiança de 95% para o lucro médio e o RTP.

    1. IC do lucro médio e do RTP com as rodadas do Experimento 1.
    2. IC do lucro médio usando só as primeiras 100, 1.000 e 10.000 rodadas
       (largura diminui com √n).
    3. Verificação do método com execuções independentes: n_execucoes
       sequências de n_rodadas (sementes 1, 2, ..., n_execucoes), cada uma com
       seu IC; conta quantos contêm o valor teórico E[X] = -0,16.

    Args:
        resultados_e1: Rodadas do Experimento 1. Se None, executa 10.000 rodadas com semente 2026
        n_execucoes: Número de execuções independentes para verificar a cobertura
        n_rodadas: Rodadas por execução independente
        marcos: Tamanhos de amostra para comparar a largura do IC

    Returns:
        dict com 'ic_lucro', 'ic_rtp', 'ic_por_n', 'execucoes', 'cobertura',
        'esperanca_teorica', 'rtp_teorico'
    """
    if resultados_e1 is None:
        resultados_e1 = executar_rodadas(10000, 2026, TABELA_BASE)

    esperanca = calcular_esperanca_lucro(TABELA_BASE)
    rtp_teorico = calcular_rtp_teorico(TABELA_BASE)

    lucros = [r['lucro'] for r in resultados_e1]
    premios = [r['premio'] for r in resultados_e1]

    ic_lucro = intervalo_confianca_media(lucros)
    ic_lucro['contem_teorico'] = ic_lucro['inferior'] <= esperanca <= ic_lucro['superior']

    # RTP = prêmio médio por crédito apostado (aposta de 1 crédito)
    ic_rtp = intervalo_confianca_media(premios)
    ic_rtp['contem_teorico'] = ic_rtp['inferior'] <= rtp_teorico <= ic_rtp['superior']

    ic_por_n = {}
    for m in marcos:
        if m <= len(lucros):
            ic = intervalo_confianca_media(lucros[:m])
            ic['contem_teorico'] = ic['inferior'] <= esperanca <= ic['superior']
            ic_por_n[m] = ic

    # Execuções independentes: uma semente por execução, inicializada uma vez
    execucoes = []
    for semente in range(1, n_execucoes + 1):
        lucros_exec = [r['lucro'] for r in executar_rodadas(n_rodadas, semente, TABELA_BASE)]
        ic = intervalo_confianca_media(lucros_exec)
        ic['semente'] = semente
        ic['contem_teorico'] = ic['inferior'] <= esperanca <= ic['superior']
        execucoes.append(ic)

    cobertura = (sum(1 for ic in execucoes if ic['contem_teorico']) / n_execucoes
                 if n_execucoes > 0 else None)

    return {
        'n_rodadas_e1': len(resultados_e1),
        'esperanca_teorica': esperanca,
        'rtp_teorico': rtp_teorico,
        'ic_lucro': ic_lucro,
        'ic_rtp': ic_rtp,
        'ic_por_n': ic_por_n,
        'n_execucoes': n_execucoes,
        'n_rodadas_execucao': n_rodadas,
        'execucoes': execucoes,
        'cobertura': cobertura
    }


def exportar_extra_intervalos_csv(dados: Dict, pasta: str = "resultados/csvs") -> List[str]:
    """
    Exporta os CSVs do Extra A.

    Returns:
        list: Caminhos dos arquivos gerados
    """
    Path(pasta).mkdir(parents=True, exist_ok=True)

    def linha(nome, ic, referencia):
        return {
            'Estimativa': nome,
            'n': ic['n'],
            'Média': ic['media'],
            'Desvio-padrão (s)': ic['desvio_padrao'],
            'Erro-padrão (s/√n)': ic['erro_padrao'],
            'IC 95% inferior': ic['inferior'],
            'IC 95% superior': ic['superior'],
            'Valor teórico': referencia,
            'Contém o teórico': 'sim' if ic['contem_teorico'] else 'não'
        }

    linhas = [
        linha('Lucro médio (E1, 10.000 rodadas)', dados['ic_lucro'], dados['esperanca_teorica']),
        linha('RTP (E1, 10.000 rodadas)', dados['ic_rtp'], dados['rtp_teorico'])
    ]
    for m, ic in dados['ic_por_n'].items():
        linhas.append(linha(f'Lucro médio (E1, primeiras {m} rodadas)', ic, dados['esperanca_teorica']))

    caminho_resumo = f"{pasta}/extra_intervalos_confianca.csv"
    pd.DataFrame(linhas).to_csv(caminho_resumo, index=False, float_format='%.6f')

    caminho_execucoes = f"{pasta}/extra_intervalos_execucoes.csv"
    pd.DataFrame([{
        'Semente': ic['semente'],
        'Lucro médio': ic['media'],
        'IC 95% inferior': ic['inferior'],
        'IC 95% superior': ic['superior'],
        'Contém -0,16': 'sim' if ic['contem_teorico'] else 'não'
    } for ic in dados['execucoes']]).to_csv(caminho_execucoes, index=False, float_format='%.6f')

    return [caminho_resumo, caminho_execucoes]


def grafico_extra_intervalos(dados: Dict, caminho: str = "resultados/graficos/extra_intervalos_confianca.png",
                             n_mostrar: int = 50) -> str:
    """
    Gráfico dos IC 95% das primeiras n_mostrar execuções independentes, com a
    referência E[X] = -0,16. Intervalos que não contêm a referência em destaque.
    """
    Path(caminho).parent.mkdir(parents=True, exist_ok=True)
    execucoes = dados['execucoes'][:n_mostrar]
    esperanca = dados['esperanca_teorica']

    fig, ax = plt.subplots(figsize=(10, 6))
    for i, ic in enumerate(execucoes, start=1):
        cor = CORES_SERIES[0] if ic['contem_teorico'] else COR_FORA
        ax.plot([ic['inferior'], ic['superior']], [i, i], color=cor, linewidth=2,
                solid_capstyle='round')
        ax.plot(ic['media'], i, 'o', color=cor, markersize=4)

    ax.axvline(esperanca, color=COR_REFERENCIA, linestyle='--', linewidth=1.2)
    ax.text(esperanca + 0.004, len(execucoes) + 1.2, f'E[X] = {esperanca:.2f}'.replace('.', ','),
            ha='left', va='bottom', fontsize=9, color=COR_REFERENCIA)

    fora = sum(1 for ic in execucoes if not ic['contem_teorico'])
    ax.plot([], [], color=CORES_SERIES[0], linewidth=2, label='Contém E[X]')
    ax.plot([], [], color=COR_FORA, linewidth=2, label=f'Não contém E[X] ({fora} de {len(execucoes)})')
    ax.legend(loc='lower left', bbox_to_anchor=(0, 1.0), ncol=2, fontsize=9, frameon=False)

    ax.set_xlabel('Lucro médio por rodada (créditos)')
    ax.set_ylabel('Execução (semente)')
    ax.set_ylim(0, len(execucoes) + 3)
    ax.grid(axis='x', alpha=0.3, linestyle='--', linewidth=0.5)
    for lado in ('top', 'right'):
        ax.spines[lado].set_visible(False)

    plt.tight_layout()
    plt.savefig(caminho, dpi=300, bbox_inches='tight')
    plt.close()
    return caminho


# ==============================================================================
# EXTRA B: MESMA MÉDIA, RISCOS DIFERENTES
# ==============================================================================

# Mesmo RTP da base (84%): soma dos pagamentos = 105, pois E[P] = soma/125
TABELA_BAIXO_RISCO = {
    ('A', 'A', 'A'): 21,
    ('B', 'B', 'B'): 21,
    ('C', 'C', 'C'): 21,
    ('D', 'D', 'D'): 21,
    ('E', 'E', 'E'): 21,
}

TABELA_ALTO_RISCO = {
    ('E', 'E', 'E'): 105,
}

TABELAS_EXTRA_B = {
    'Base': TABELA_BASE,
    'Baixo risco (todas pagam 21)': TABELA_BAIXO_RISCO,
    'Alto risco (só E-E-E paga 105)': TABELA_ALTO_RISCO
}


def momentos_teoricos(tabela: Dict) -> Dict:
    """
    Esperança, variância e desvio-padrão teóricos do lucro X = P - 1.

    Var(X) = Var(P) = E[P²] - E[P]², com cada tripla de probabilidade 1/125.
    """
    e_p = sum(tabela.values()) / 125
    e_p2 = sum(v ** 2 for v in tabela.values()) / 125
    variancia = e_p2 - e_p ** 2

    return {
        'prob_premio': calcular_probabilidade_premio(tabela),
        'esperanca_premio': e_p,
        'esperanca_lucro': e_p - 1,
        'rtp': e_p,
        'variancia_lucro': variancia,
        'desvio_padrao_lucro': math.sqrt(variancia),
        'maior_lucro': max(tabela.values()) - 1
    }


def gerar_linhas_participantes(n_participantes: int, max_rodadas: int, semente: int) -> List[List[Tuple]]:
    """
    Sorteia as linhas centrais de todos os participantes com UM gerador,
    inicializado uma única vez com a semente. Cada participante recebe
    max_rodadas linhas consecutivas da sequência.
    """
    rng = random.Random(semente)
    return [[executar_rodada(rng)['linha_central'] for _ in range(max_rodadas)]
            for _ in range(n_participantes)]


def simular_sessao(linhas: List[Tuple], tabela: Dict, saldo_inicial: float) -> Dict:
    """
    Joga as linhas centrais em ordem até acabarem ou o saldo ficar abaixo de 1
    (aposta de 1 crédito, sem empréstimo ou reposição).
    """
    saldo = saldo_inicial
    trajetoria = [saldo]
    for linha in linhas:
        if saldo < 1:
            break
        saldo += calcular_lucro(calcular_premio(linha, tabela))
        trajetoria.append(saldo)

    return {
        'saldo_final': saldo,
        'rodadas': len(trajetoria) - 1,
        'esgotou': saldo < 1,
        'trajetoria': trajetoria
    }


def resumir_sessoes(sessoes: List[Dict], saldo_inicial: float) -> Dict:
    """Proporções de ganho/empate/perda, esgotamento e resumo dos saldos finais."""
    n = len(sessoes)
    saldos = np.array([s['saldo_final'] for s in sessoes], dtype=float)

    return {
        'n_participantes': n,
        'proporcao_ganho': float(np.mean(saldos > saldo_inicial)),
        'proporcao_empate': float(np.mean(saldos == saldo_inicial)),
        'proporcao_perda': float(np.mean(saldos < saldo_inicial)),
        'proporcao_esgotamento': sum(1 for s in sessoes if s['esgotou']) / n,
        'media_saldo_final': float(np.mean(saldos)),
        'mediana_saldo_final': float(np.median(saldos)),
        'desvio_saldo_final': float(np.std(saldos, ddof=1)),
        'percentil_10': float(np.percentile(saldos, 10)),
        'percentil_90': float(np.percentile(saldos, 90)),
        'maior_saldo_final': float(np.max(saldos)),
        'media_rodadas': float(np.mean([s['rodadas'] for s in sessoes]))
    }


def extra_mesma_media(resultados_e1: List[Dict] = None,
                      tabelas: Dict[str, Dict] = None,
                      n_participantes: int = 100,
                      saldo_inicial: float = 100,
                      max_rodadas: int = 500,
                      semente_sessoes: int = 42) -> Dict:
    """
    Extra B: Mesma média, riscos diferentes.

    Compara tabelas com o mesmo RTP teórico (84%) e dispersões diferentes:
    1. Momentos teóricos (esperança igual, variância diferente).
    2. Lucro médio e desvio-padrão observados nas mesmas 10.000 rodadas do E1.
    3. Saldos finais de sessões limitadas (mesmos parâmetros do E3) jogadas com
       os MESMOS sorteios em todas as tabelas: só os pagamentos mudam.
    """
    if resultados_e1 is None:
        resultados_e1 = executar_rodadas(10000, 2026, TABELA_BASE)
    if tabelas is None:
        tabelas = TABELAS_EXTRA_B

    linhas_e1 = [r['linha_central'] for r in resultados_e1]
    linhas_participantes = gerar_linhas_participantes(n_participantes, max_rodadas, semente_sessoes)

    comparacao = {}
    for nome, tabela in tabelas.items():
        lucros = [calcular_lucro(calcular_premio(l, tabela)) for l in linhas_e1]
        sessoes = [simular_sessao(linhas, tabela, saldo_inicial) for linhas in linhas_participantes]

        comparacao[nome] = {
            'teorico': momentos_teoricos(tabela),
            'observado_e1': {
                'lucro_medio': float(np.mean(lucros)),
                'desvio_padrao': float(np.std(lucros, ddof=1)),
                'freq_premio': sum(1 for x in lucros if x > -1) / len(lucros)
            },
            'sessoes': resumir_sessoes(sessoes, saldo_inicial),
            'saldos_finais': [s['saldo_final'] for s in sessoes]
        }

    return {
        'n_rodadas_e1': len(resultados_e1),
        'n_participantes': n_participantes,
        'saldo_inicial': saldo_inicial,
        'max_rodadas': max_rodadas,
        'semente_sessoes': semente_sessoes,
        'tabelas': comparacao
    }


def exportar_extra_mesma_media_csv(dados: Dict, pasta: str = "resultados/csvs") -> List[str]:
    """
    Exporta os CSVs do Extra B.

    Returns:
        list: Caminhos dos arquivos gerados
    """
    Path(pasta).mkdir(parents=True, exist_ok=True)

    linhas = []
    for nome, d in dados['tabelas'].items():
        t, o, s = d['teorico'], d['observado_e1'], d['sessoes']
        linhas.append({
            'Tabela': nome,
            'P(prêmio) teórica': t['prob_premio'],
            'E[X] teórico': t['esperanca_lucro'],
            'RTP teórico (%)': t['rtp'] * 100,
            'Desvio-padrão teórico de X': t['desvio_padrao_lucro'],
            'Maior lucro numa rodada': t['maior_lucro'],
            'Lucro médio observado (E1)': o['lucro_medio'],
            'Desvio-padrão observado (E1)': o['desvio_padrao'],
            'Sessões: ganho (%)': s['proporcao_ganho'] * 100,
            'Sessões: empate (%)': s['proporcao_empate'] * 100,
            'Sessões: perda (%)': s['proporcao_perda'] * 100,
            'Sessões: esgotamento (%)': s['proporcao_esgotamento'] * 100,
            'Saldo final: média': s['media_saldo_final'],
            'Saldo final: mediana': s['mediana_saldo_final'],
            'Saldo final: desvio-padrão': s['desvio_saldo_final'],
            'Saldo final: percentil 10': s['percentil_10'],
            'Saldo final: percentil 90': s['percentil_90'],
            'Saldo final: maior': s['maior_saldo_final']
        })

    caminho_resumo = f"{pasta}/extra_mesma_media_riscos.csv"
    pd.DataFrame(linhas).to_csv(caminho_resumo, index=False, float_format='%.6f')

    colunas = {'Participante': range(1, dados['n_participantes'] + 1)}
    for nome, d in dados['tabelas'].items():
        colunas[f'Saldo final - {nome}'] = d['saldos_finais']
    caminho_saldos = f"{pasta}/extra_mesma_media_saldos.csv"
    pd.DataFrame(colunas).to_csv(caminho_saldos, index=False)

    return [caminho_resumo, caminho_saldos]


def grafico_extra_mesma_media(dados: Dict, caminho: str = "resultados/graficos/extra_mesma_media_riscos.png") -> str:
    """
    Distribuição dos saldos finais por tabela (um ponto por participante),
    com média e mediana marcadas e o saldo inicial como referência.
    """
    Path(caminho).parent.mkdir(parents=True, exist_ok=True)
    nomes = list(dados['tabelas'].keys())
    rng = np.random.default_rng(0)  # apenas para espalhar os pontos na horizontal

    fig, ax = plt.subplots(figsize=(10, 6))
    for i, (nome, cor) in enumerate(zip(nomes, CORES_SERIES)):
        saldos = np.array(dados['tabelas'][nome]['saldos_finais'], dtype=float)
        x = i + rng.uniform(-0.18, 0.18, size=len(saldos))
        ax.scatter(x, saldos, s=22, color=cor, alpha=0.75, edgecolor='white', linewidth=0.6)

        s = dados['tabelas'][nome]['sessoes']
        ax.plot([i - 0.3, i + 0.3], [s['media_saldo_final']] * 2, color=COR_REFERENCIA, linewidth=2)
        ax.plot([i - 0.3, i + 0.3], [s['mediana_saldo_final']] * 2, color=COR_REFERENCIA,
                linewidth=2, linestyle=':')
        ax.text(i + 0.33, s['media_saldo_final'], f"média {s['media_saldo_final']:.1f}".replace('.', ','),
                va='center', fontsize=8, color=COR_REFERENCIA)
        ax.text(i + 0.33, s['mediana_saldo_final'], f"mediana {s['mediana_saldo_final']:.1f}".replace('.', ','),
                va='center', fontsize=8, color=COR_REFERENCIA)
        esgotados = round(s['proporcao_esgotamento'] * s['n_participantes'])
        ax.text(i, -30, f"{esgotados} de {s['n_participantes']} esgotaram o saldo",
                ha='center', va='top', fontsize=8, color=COR_REFERENCIA)

    ax.axhline(dados['saldo_inicial'], color=COR_REFERENCIA, linestyle='--', linewidth=1, alpha=0.7)
    ax.text(len(nomes) - 0.5, dados['saldo_inicial'], 'saldo inicial', va='bottom', ha='right',
            fontsize=8, color=COR_REFERENCIA)

    ax.set_xticks(range(len(nomes)))
    ax.set_xticklabels(nomes)
    ax.set_xlim(-0.5, len(nomes) - 0.3)
    ax.set_ylim(bottom=-70)
    ax.set_ylabel('Saldo final (créditos)')
    ax.grid(axis='y', alpha=0.3, linestyle='--', linewidth=0.5)
    for lado in ('top', 'right'):
        ax.spines[lado].set_visible(False)

    plt.tight_layout()
    plt.savefig(caminho, dpi=300, bbox_inches='tight')
    plt.close()
    return caminho
