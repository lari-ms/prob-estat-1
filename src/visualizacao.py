"""
Módulo visualizacao.py
Implementa funções para gerar gráficos dos experimentos.
"""

import matplotlib.pyplot as plt
import numpy as np
from typing import Dict
from pathlib import Path


def configurar_estilo_grafico():
    """Configura estilo padrão para os gráficos - visual acadêmico profissional."""
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.rcParams['figure.figsize'] = (10, 6)
    plt.rcParams['figure.facecolor'] = 'white'
    plt.rcParams['axes.facecolor'] = '#f8f9fa'
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans']
    plt.rcParams['font.size'] = 10
    plt.rcParams['axes.labelsize'] = 11
    plt.rcParams['axes.titlesize'] = 12
    plt.rcParams['axes.titleweight'] = 'bold'
    plt.rcParams['xtick.labelsize'] = 10
    plt.rcParams['ytick.labelsize'] = 10
    plt.rcParams['legend.fontsize'] = 9
    plt.rcParams['legend.framealpha'] = 0.95
    plt.rcParams['grid.alpha'] = 0.3
    plt.rcParams['grid.linestyle'] = '--'
    plt.rcParams['grid.linewidth'] = 0.5


def criar_diretorios_graficos():
    """Cria o diretório para salvar gráficos se não existir."""
    Path("resultados/graficos").mkdir(parents=True, exist_ok=True)


def grafico_experimento_1_frequencias(dados: Dict, caminho: str = "resultados/graficos/experimento1_frequencias.png"):
    """
    Gera gráfico com dois painéis comparando probabilidades teóricas e frequências observadas.
    Visual profissional e acadêmico - Identidade visual consistente.
    Painel superior: perda (-1 crédito)
    Painel inferior: prêmios (4, 9, 14, 24, 49 créditos)
    
    Args:
        dados: Resultado do experimento_1()
        caminho: Caminho para salvar o gráfico
        
    Returns:
        str: Caminho do arquivo salvo
    """
    criar_diretorios_graficos()
    configurar_estilo_grafico()
    
    # Separar dados: perda vs prêmios
    lucro_perda = -1
    lucros_premios = [4, 9, 14, 24, 49]
    
    # Perda
    prob_perda_teorica = dados['probabilidades_teoricas'][lucro_perda] * 100
    freq_perda_observada = dados['frequencias'][lucro_perda] * 100
    
    # Prêmios
    prob_premios_teoricas = [dados['probabilidades_teoricas'][l] * 100 for l in lucros_premios]
    freq_premios_observadas = [dados['frequencias'][l] * 100 for l in lucros_premios]
    
    # Criar figura com 2 subplots - proporções equilibradas
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8.5), 
                                     gridspec_kw={'height_ratios': [1, 1.4]})
    
    # CORES CONSISTENTES com Gráfico 1
    cor_teorica = '#2980b9'      # Azul profissional
    cor_observada = '#e67e22'    # Laranja profissional
    
    largura = 0.32
    
    # ========== PAINEL 1: PERDA (-1 crédito) ==========
    x_perda = [0]
    
    b1 = ax1.bar([x_perda[0] - largura/2], [prob_perda_teorica], 
                 largura, label='Probabilidade Teórica', 
                 color=cor_teorica, alpha=0.85, edgecolor='#2c3e50', linewidth=1.2)
    
    b2 = ax1.bar([x_perda[0] + largura/2], [freq_perda_observada], 
                 largura, label='Frequência Observada', 
                 color=cor_observada, alpha=0.85, edgecolor='#2c3e50', linewidth=1.2)
    
    ax1.set_ylabel('Porcentagem (%)', fontsize=11, fontweight='bold', labelpad=10)
    ax1.set_title('Perda: Lucro = −1 crédito',
                  fontsize=11, fontweight='bold', pad=12)
    ax1.set_xticks([0])
    ax1.set_xticklabels(['Perda\n(−1)'], fontsize=10)
    ax1.legend(loc='upper right', fontsize=9, frameon=True, 
              fancybox=False, shadow=False, edgecolor='#95a5a6')
    ax1.grid(True, alpha=0.25, axis='y', linestyle='--', linewidth=0.5)
    ax1.set_ylim(0, 100)
    ax1.set_axisbelow(True)
    
    # Remover bordas superiores e direita
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['left'].set_color('#7f8c8d')
    ax1.spines['bottom'].set_color('#7f8c8d')
    
    # Valores acima das barras com espaçamento
    for barra in b1:
        altura = barra.get_height()
        ax1.text(barra.get_x() + barra.get_width()/2., altura + 1.5,
                f'{altura:.2f}%',
                ha='center', va='bottom', fontsize=9, fontweight='600')
    
    for barra in b2:
        altura = barra.get_height()
        ax1.text(barra.get_x() + barra.get_width()/2., altura + 1.5,
                f'{altura:.2f}%',
                ha='center', va='bottom', fontsize=9, fontweight='600')
    
    # ========== PAINEL 2: PRÊMIOS (4, 9, 14, 24, 49) ==========
    x_premios = np.arange(len(lucros_premios))
    
    b3 = ax2.bar(x_premios - largura/2, prob_premios_teoricas, 
                 largura, label='Probabilidade Teórica (0,80% cada)', 
                 color=cor_teorica, alpha=0.85, edgecolor='#2c3e50', linewidth=1.2)
    
    b4 = ax2.bar(x_premios + largura/2, freq_premios_observadas, 
                 largura, label='Frequência Observada', 
                 color=cor_observada, alpha=0.85, edgecolor='#2c3e50', linewidth=1.2)
    
    ax2.set_xlabel('Lucro por rodada (créditos)', fontsize=11, fontweight='bold', labelpad=10)
    ax2.set_ylabel('Porcentagem (%)', fontsize=11, fontweight='bold', labelpad=10)
    ax2.set_title('Prêmios: Lucros positivos',
                  fontsize=11, fontweight='bold', pad=12)
    ax2.set_xticks(x_premios)
    ax2.set_xticklabels([f'+{l}' for l in lucros_premios], fontsize=10)
    ax2.legend(loc='upper left', fontsize=9, frameon=True,
              fancybox=False, shadow=False, edgecolor='#95a5a6')
    ax2.grid(True, alpha=0.25, axis='y', linestyle='--', linewidth=0.5)
    ax2.set_axisbelow(True)
    
    # Remover bordas superiores e direita
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.spines['left'].set_color('#7f8c8d')
    ax2.spines['bottom'].set_color('#7f8c8d')
    
    # Valores acima das barras com espaçamento adequado
    max_altura = max(max(prob_premios_teoricas), max(freq_premios_observadas))
    
    for barra in b3:
        altura = barra.get_height()
        ax2.text(barra.get_x() + barra.get_width()/2., altura + max_altura*0.03,
                f'{altura:.2f}%',
                ha='center', va='bottom', fontsize=8.5)
    
    for barra in b4:
        altura = barra.get_height()
        ax2.text(barra.get_x() + barra.get_width()/2., altura + max_altura*0.03,
                f'{altura:.2f}%',
                ha='center', va='bottom', fontsize=8.5)
    
    # Nota explicativa discreta abaixo do gráfico
    nota = (f'Nota: P(algum prêmio) = 4,00% teórico (soma das 5 combinações premiadas) | '
            f'Observado: {dados["proporcao_premios"]*100:.2f}% ({dados["premios_observados"]} prêmios em 10.000 rodadas)')
    fig.text(0.5, 0.01, nota, ha='center', va='bottom', fontsize=8, style='italic',
             color='#34495e',
             bbox=dict(boxstyle='round,pad=0.4', facecolor='#ecf0f1', 
                      edgecolor='#bdc3c7', alpha=0.9, linewidth=0.8))
    
    # Título geral da figura
    fig.suptitle('Comparação: Probabilidades Teóricas vs Frequências Observadas\n' +
                 'Experimento 1 — 10.000 rodadas (semente 2026)',
                 fontsize=12, fontweight='bold', y=0.98)
    
    # Ajustar layout - espaço reduzido entre painéis
    plt.tight_layout(rect=[0, 0.04, 1, 0.96])
    plt.subplots_adjust(hspace=0.28)
    plt.savefig(caminho, dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()
    
    return caminho


def grafico_experimento_1_distribuicao_lucro(dados: Dict, caminho: str = "resultados/graficos/experimento1_distribuicao.png"):
    """
    Gera gráfico de barras da distribuição de lucros observados (valores discretos).
    Visual profissional e acadêmico.
    
    Args:
        dados: Resultado do experimento_1()
        caminho: Caminho para salvar o gráfico
        
    Returns:
        str: Caminho do arquivo salvo
    """
    criar_diretorios_graficos()
    configurar_estilo_grafico()
    
    # Preparar dados discretos
    lucros = sorted(dados['contagens'].keys())
    contagens = [dados['contagens'][l] for l in lucros]
    porcentagens = [dados['frequencias'][l] * 100 for l in lucros]
    
    # Criar figura com espaço para legenda abaixo
    fig, ax = plt.subplots(figsize=(12, 7))
    
    # Cores consistentes - perda em destaque, prêmios em tom único
    cores = ['#e74c3c' if l == -1 else '#3498db' for l in lucros]
    
    # Criar barras com largura otimizada
    posicoes = np.arange(len(lucros))
    barras = ax.bar(posicoes, contagens, color=cores, 
                    alpha=0.85, edgecolor='#2c3e50', linewidth=1.2, width=0.65)
    
    # Configurar eixos com clareza
    ax.set_xlabel('Lucro por rodada (créditos)', fontsize=11, fontweight='bold', labelpad=10)
    ax.set_ylabel('Frequência Absoluta', fontsize=11, fontweight='bold', labelpad=10)
    ax.set_title('Distribuição dos Lucros Observados — Experimento 1\n' +
                 f'10.000 rodadas simuladas (semente 2026)',
                 fontsize=12, fontweight='bold', pad=20)
    
    ax.set_xticks(posicoes)
    ax.set_xticklabels([f'{int(l):+d}' for l in lucros], fontsize=10)
    ax.set_xlim(-0.6, len(lucros) - 0.4)
    
    # Grade apenas no eixo Y
    ax.grid(True, alpha=0.25, axis='y', linestyle='--', linewidth=0.5)
    ax.set_axisbelow(True)
    
    # Adicionar valores nas barras de forma limpa
    for i, (barra, contagem, pct) in enumerate(zip(barras, contagens, porcentagens)):
        altura = barra.get_height()
        
        # Valores absolutos acima das barras
        ax.text(barra.get_x() + barra.get_width()/2., altura + max(contagens)*0.01,
               f'{int(contagem):,}',
               ha='center', va='bottom', fontsize=9, fontweight='600')
        
        # Porcentagem dentro das barras (apenas para valores visíveis)
        if pct >= 1.0:  # Só mostrar % se >= 1%
            ax.text(barra.get_x() + barra.get_width()/2., altura * 0.5,
                   f'{pct:.2f}%',
                   ha='center', va='center', fontsize=8, 
                   color='white', fontweight='bold')
    
    # Estatísticas organizadas abaixo do gráfico
    media = dados['lucro_medio']
    stats_text = (
        f"Média: {media:.4f} (teórico: −0,1600) | "
        f"Desvio-padrão: {dados['desvio_padrao']:.4f} | "
        f"RTP: {dados['rtp_observado']*100:.2f}% (teórico: 84,00%) | "
        f"Prêmios: {dados['premios_observados']} ({dados['proporcao_premios']*100:.2f}%)"
    )
    
    fig.text(0.5, 0.02, stats_text,
             ha='center', va='bottom', fontsize=8.5, style='italic',
             color='#34495e',
             bbox=dict(boxstyle='round,pad=0.5', facecolor='#ecf0f1', 
                      edgecolor='#bdc3c7', alpha=0.9, linewidth=1))
    
    # Legenda discreta no canto superior direito
    from matplotlib.patches import Patch
    legenda_elementos = [
        Patch(facecolor='#e74c3c', edgecolor='#2c3e50', alpha=0.85, label='Perda (−1)'),
        Patch(facecolor='#3498db', edgecolor='#2c3e50', alpha=0.85, label='Prêmios (+)')
    ]
    ax.legend(handles=legenda_elementos, loc='upper right', 
             frameon=True, fancybox=False, shadow=False,
             edgecolor='#95a5a6', fontsize=9)
    
    # Remover bordas superiores e direita (estilo acadêmico)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#7f8c8d')
    ax.spines['bottom'].set_color('#7f8c8d')
    
    # Validação silenciosa
    soma_contagens = sum(contagens)
    soma_pct = sum(porcentagens)
    if soma_contagens != dados['n_rodadas']:
        print(f"⚠️ Validação: Soma contagens = {soma_contagens}")
    if abs(soma_pct - 100.0) > 0.01:
        print(f"⚠️ Validação: Soma porcentagens = {soma_pct:.2f}%")
    
    # Ajustar layout e salvar
    plt.tight_layout(rect=[0, 0.06, 1, 1])
    plt.savefig(caminho, dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()
    
    return caminho
