"""
Script para executar o Experimento 1 completo
"""

import sys
from src.experimentos import experimento_1, interpretar_experimento_1
from src.exportacao import (
    exportar_experimento_1_csv,
    exportar_metricas_experimento_1_csv,
    salvar_configuracao_execucao
)
from src.visualizacao import (
    grafico_experimento_1_frequencias,
    grafico_experimento_1_distribuicao_lucro
)

def main():
    print("=" * 80)
    print("EXPERIMENTO 1: FREQUÊNCIAS E PROBABILIDADES")
    print("=" * 80)
    print()
    print("Simulador acadêmico - somente créditos fictícios")
    print()
    
    # Executar experimento
    print("Executando 10.000 rodadas com semente 2026...")
    dados = experimento_1(n=10000, semente=2026)
    print("✓ Execução concluída!")
    print()
    
    # Exibir métricas principais
    print("-" * 80)
    print("MÉTRICAS PRINCIPAIS")
    print("-" * 80)
    print(f"Número de rodadas:              {dados['n_rodadas']:,}")
    print(f"Semente:                        {dados['semente']}")
    print()
    print(f"Lucro médio observado:          {dados['lucro_medio']:.6f} créditos")
    print(f"Lucro esperado teórico:         -0.160000 créditos")
    print(f"Diferença:                      {abs(dados['lucro_medio'] - (-0.16)):.6f}")
    print()
    print(f"RTP observado:                  {dados['rtp_observado']*100:.2f}%")
    print(f"RTP teórico:                    {dados['rtp_teorico']*100:.2f}%")
    print()
    print(f"Proporção de prêmios observada: {dados['proporcao_premios']*100:.2f}%")
    print(f"Proporção de prêmios teórica:   4.00%")
    print(f"Prêmios observados:             {dados['premios_observados']:,}")
    print(f"Prêmios esperados:              {dados['premios_esperados']:.0f}")
    print()
    print(f"Desvio-padrão amostral:         {dados['desvio_padrao']:.6f} créditos")
    print()
    
    # Exibir tabela de frequências
    print("-" * 80)
    print("FREQUÊNCIAS OBSERVADAS VS PROBABILIDADES TEÓRICAS")
    print("-" * 80)
    print(f"{'Lucro':>6} | {'Prob. Teórica':>14} | {'Contagem':>10} | {'Freq. Relativa':>15} | {'Diferença':>12}")
    print("-" * 80)
    
    for lucro in sorted(dados['contagens'].keys()):
        prob = dados['probabilidades_teoricas'][lucro]
        cont = dados['contagens'][lucro]
        freq = dados['frequencias'][lucro]
        diff = freq - prob
        
        print(f"{lucro:6.0f} | {prob*100:13.4f}% | {cont:10,} | {freq*100:14.4f}% | {diff*100:11.4f}%")
    
    print("-" * 80)
    print(f"{'TOTAL':>6} | {100.00:13.4f}% | {dados['n_rodadas']:10,} | {100.00:14.4f}% |")
    print()
    
    # Exportar CSVs
    print("Exportando resultados...")
    csv_freq = exportar_experimento_1_csv(dados)
    print(f"✓ Tabela de frequências: {csv_freq}")
    
    csv_metricas = exportar_metricas_experimento_1_csv(dados)
    print(f"✓ Métricas resumidas: {csv_metricas}")
    
    # Salvar configuração
    config = salvar_configuracao_execucao('experimento_1', {
        'n_rodadas': dados['n_rodadas'],
        'semente': dados['semente'],
        'tabela': 'TABELA_BASE',
        'python_version': sys.version.split()[0],
        'gerador': 'random.Random()'
    })
    print(f"✓ Configuração: {config}")
    print()
    
    # Gerar gráficos
    print("Gerando gráficos...")
    grafico1 = grafico_experimento_1_frequencias(dados)
    print(f"✓ Gráfico de frequências: {grafico1}")
    
    grafico2 = grafico_experimento_1_distribuicao_lucro(dados)
    print(f"✓ Gráfico de distribuição: {grafico2}")
    print()
    
    # Interpretação
    print("=" * 80)
    print("INTERPRETAÇÃO DOS RESULTADOS")
    print("=" * 80)
    print()
    interpretacao = interpretar_experimento_1(dados)
    print(interpretacao)
    print()
    
    # Salvar interpretação
    with open('resultados/experimento_1_interpretacao.txt', 'w', encoding='utf-8') as f:
        f.write("EXPERIMENTO 1: FREQUÊNCIAS E PROBABILIDADES\n")
        f.write("=" * 80 + "\n\n")
        f.write(interpretacao)
    
    print()
    print("=" * 80)
    print("✓ EXPERIMENTO 1 CONCLUÍDO COM SUCESSO!")
    print("=" * 80)
    print()
    print("Arquivos gerados:")
    print(f"  • {csv_freq}")
    print(f"  • {csv_metricas}")
    print(f"  • {grafico1}")
    print(f"  • {grafico2}")
    print(f"  • resultados/experimento_1_interpretacao.txt")
    print()
    print("Os resultados foram salvos e podem ser inseridos no relatório (Seção 4.2).")
    print()


if __name__ == "__main__":
    main()
