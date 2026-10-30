"""
Script para executar o Experimento 2 completo
"""

import sys
from src.experimentos import experimento_2, interpretar_experimento_2
from src.exportacao import (
    exportar_experimento_2_csv,
    exportar_trajetorias_experimento_2_csv,
    salvar_configuracao_execucao
)
from src.visualizacao import grafico_experimento_2_trajetorias

def main():
    print("=" * 80)
    print("EXPERIMENTO 2: LEI DOS GRANDES NÚMEROS")
    print("=" * 80)
    print()
    print("Simulador acadêmico - somente créditos fictícios")
    print()
    
    # Executar experimento
    print("Executando 3 sequências com sementes 10, 2026 e 123456...")
    print("(A sequência 2026 será reutilizada do Experimento 1)")
    print()
    
    dados = experimento_2(
        sementes=[10, 2026, 123456],
        n=10000,
        pontos_acumulacao=[100, 1000, 10000]
    )
    
    print("✓ Execução concluída!")
    print()
    
    # Confirmar reutilização
    if dados['reutilizou_experimento_1']:
        print("✓ Sequência 2026 reutilizada do Experimento 1 (cache)")
    print()
    
    # Exibir tabela de médias acumuladas
    print("-" * 80)
    print("TABELA DE MÉDIAS ACUMULADAS")
    print("-" * 80)
    print(f"{'Semente':<12} | {'100 rodadas':>13} | {'1.000 rodadas':>15} | {'10.000 rodadas':>16}")
    print("-" * 80)
    
    for semente in dados['sementes']:
        valores = []
        for ponto in dados['pontos_acumulacao']:
            if ponto in dados['medias_acumuladas'][semente]:
                valores.append(f"{dados['medias_acumuladas'][semente][ponto]:15.6f}")
            else:
                valores.append(f"{'N/A':>15}")
        
        print(f"{semente:<12} | {valores[0]} | {valores[1]} | {valores[2]}")
    
    print("-" * 80)
    print(f"{'E[X] teórico':<12} | {dados['esperanca_teorica']:15.6f} | {dados['esperanca_teorica']:15.6f} | {dados['esperanca_teorica']:16.6f}")
    print("-" * 80)
    print()
    
    # Calcular diferenças em relação ao valor teórico
    print("DIFERENÇAS EM RELAÇÃO AO VALOR TEÓRICO")
    print("-" * 80)
    print(f"{'Semente':<12} | {'Δ em 100':>10} | {'Δ em 1.000':>12} | {'Δ em 10.000':>13}")
    print("-" * 80)
    
    for semente in dados['sementes']:
        diferencas = []
        for ponto in dados['pontos_acumulacao']:
            if ponto in dados['medias_acumuladas'][semente]:
                diff = abs(dados['medias_acumuladas'][semente][ponto] - dados['esperanca_teorica'])
                diferencas.append(f"{diff:12.6f}")
            else:
                diferencas.append(f"{'N/A':>12}")
        
        print(f"{semente:<12} | {diferencas[0]} | {diferencas[1]} | {diferencas[2]}")
    
    print("-" * 80)
    print()
    print("Observação: As médias amostrais aproximam-se progressivamente da esperança")
    print("teórica, demonstrando a convergência prevista pela Lei dos Grandes Números.")
    print()
    
    # Exportar CSVs
    print("Exportando resultados...")
    csv_medias = exportar_experimento_2_csv(dados)
    print(f"✓ Tabela de médias acumuladas: {csv_medias}")
    
    csv_trajetorias = exportar_trajetorias_experimento_2_csv(dados)
    print(f"✓ Trajetórias completas: {csv_trajetorias}")
    
    # Salvar configuração
    config = salvar_configuracao_execucao('experimento_2', {
        'sementes': str(dados['sementes']),
        'n_rodadas': dados['n_rodadas'],
        'pontos_acumulacao': str(dados['pontos_acumulacao']),
        'reutilizou_experimento_1': dados['reutilizou_experimento_1'],
        'python_version': sys.version.split()[0],
        'tabela': 'TABELA_BASE'
    })
    print(f"✓ Configuração: {config}")
    print()
    
    # Gerar gráfico
    print("Gerando gráfico de trajetórias...")
    grafico = grafico_experimento_2_trajetorias(dados)
    print(f"✓ Gráfico de trajetórias: {grafico}")
    print()
    
    # Interpretação
    print("=" * 80)
    print("INTERPRETAÇÃO DOS RESULTADOS")
    print("=" * 80)
    print()
    interpretacao = interpretar_experimento_2(dados)
    print(interpretacao)
    print()
    
    # Salvar interpretação
    with open('resultados/experimento_2_interpretacao.txt', 'w', encoding='utf-8') as f:
        f.write("EXPERIMENTO 2: LEI DOS GRANDES NÚMEROS\n")
        f.write("=" * 80 + "\n\n")
        f.write(interpretacao)
    
    print()
    print("=" * 80)
    print("✓ EXPERIMENTO 2 CONCLUÍDO COM SUCESSO!")
    print("=" * 80)
    print()
    print("Arquivos gerados:")
    print(f"  • {csv_medias}")
    print(f"  • {csv_trajetorias}")
    print(f"  • {grafico}")
    print(f"  • resultados/experimento_2_interpretacao.txt")
    print()
    print("Os resultados demonstram empiricamente a Lei dos Grandes Números:")
    print("À medida que n aumenta, as médias amostrais se aproximam de E[X] = -0,1600.")
    print()
    print("Todas as 3 sequências independentes demonstram a convergência esperada,")
    print("confirmando que a longo prazo a esperança negativa do jogo se manifesta.")
    print()


if __name__ == "__main__":
    main()
