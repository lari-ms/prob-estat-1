"""
Script para executar o Experimento 3 completo
"""

import sys
from src.experimentos import experimento_3, interpretar_experimento_3
from src.exportacao import (
    exportar_experimento_3_csv,
    exportar_participantes_experimento_3_csv,
    salvar_configuracao_execucao
)
from src.visualizacao import grafico_experimento_3_trajetorias

def main():
    print("=" * 80)
    print("EXPERIMENTO 3: SALDO LIMITADO")
    print("=" * 80)
    print()
    print("Simulador acadêmico - somente créditos fictícios")
    print()
    
    # Executar experimento
    print("Simulando 100 participantes virtuais...")
    print("  • Saldo inicial: 100 créditos")
    print("  • Máximo de rodadas: 500")
    print("  • Parada: saldo zero ou 500 rodadas")
    print()
    
    dados = experimento_3(
        n_participantes=100,
        saldo_inicial=100,
        max_rodadas=500,
        semente_base=42
    )
    
    print("✓ Simulação concluída!")
    print()
    
    # Exibir resultados agregados
    print("-" * 80)
    print("RESULTADOS AGREGADOS")
    print("-" * 80)
    print(f"Número de participantes:        {dados['n_participantes']}")
    print(f"Saldo inicial:                  {dados['saldo_inicial']} créditos")
    print(f"Máximo de rodadas:              {dados['max_rodadas']}")
    print()
    
    print("DISTRIBUIÇÃO DE RESULTADOS:")
    print(f"  • Ganharam (saldo final > inicial):    {dados['ganhou']:3d} ({dados['proporcao_ganhou']*100:5.1f}%)")
    print(f"  • Empataram (saldo final = inicial):   {dados['empatou']:3d} ({dados['proporcao_empatou']*100:5.1f}%)")
    print(f"  • Perderam (saldo final < inicial):    {dados['perdeu']:3d} ({dados['proporcao_perdeu']*100:5.1f}%)")
    print(f"  • Zeraram o saldo:                      {dados['zerou_saldo']:3d} ({dados['proporcao_zerou']*100:5.1f}%)")
    print()
    
    print("SALDOS FINAIS:")
    perda_media = dados['saldo_inicial'] - dados['media_saldo_final']
    perda_pct = (1 - dados['media_saldo_final']/dados['saldo_inicial']) * 100
    
    print(f"  • Média:     {dados['media_saldo_final']:6.2f} créditos")
    print(f"  • Mediana:   {dados['mediana_saldo_final']:6.2f} créditos")
    print(f"  • Perda média: {perda_media:6.2f} créditos ({perda_pct:.2f}% do capital)")
    print()
    
    print("NÚMERO DE RODADAS:")
    print(f"  • Média:     {dados['media_rodadas']:6.1f} rodadas")
    print(f"  • Mediana:   {dados['mediana_rodadas']:6.0f} rodadas")
    
    # Participantes que atingiram o máximo
    participantes_max = sum(1 for r in dados['rodadas_jogadas'] if r >= dados['max_rodadas'])
    if participantes_max > 0:
        print(f"  • Atingiram o máximo ({dados['max_rodadas']}): {participantes_max} ({participantes_max/dados['n_participantes']*100:.1f}%)")
    print()
    
    # Exemplos individuais
    print("-" * 80)
    print("EXEMPLOS DE PARTICIPANTES (primeiros 10)")
    print("-" * 80)
    print(f"{'ID':>3} | {'Saldo Final':>12} | {'Rodadas':>8} | {'Resultado':>10}")
    print("-" * 80)
    
    for p in dados['participantes'][:10]:
        resultado = 'Zerou' if p['zerou'] else ('Ganhou' if p['ganhou'] else 'Perdeu')
        print(f"{p['id']:3d} | {p['saldo_final']:12.0f} | {p['n_rodadas']:8d} | {resultado:>10}")
    
    print("-" * 80)
    print(f"... e mais {dados['n_participantes'] - 10} participantes (ver CSV completo)")
    print()
    
    # Exportar CSVs
    print("Exportando resultados...")
    csv_resumo = exportar_experimento_3_csv(dados)
    print(f"✓ Resumo estatístico: {csv_resumo}")
    
    csv_participantes = exportar_participantes_experimento_3_csv(dados)
    print(f"✓ Dados individuais: {csv_participantes}")
    
    # Salvar configuração
    config = salvar_configuracao_execucao('experimento_3', {
        'n_participantes': dados['n_participantes'],
        'saldo_inicial': dados['saldo_inicial'],
        'max_rodadas': dados['max_rodadas'],
        'semente_base': dados['semente_base'],
        'python_version': sys.version.split()[0],
        'tabela': 'TABELA_BASE'
    })
    print(f"✓ Configuração: {config}")
    print()
    
    # Gerar gráfico
    print("Gerando gráfico de trajetórias (5 amostras)...")
    grafico = grafico_experimento_3_trajetorias(dados)
    print(f"✓ Gráfico de trajetórias: {grafico}")
    print()
    
    # Interpretação
    print("=" * 80)
    print("INTERPRETAÇÃO DOS RESULTADOS")
    print("=" * 80)
    print()
    interpretacao = interpretar_experimento_3(dados)
    print(interpretacao)
    print()
    
    # Salvar interpretação
    with open('resultados/experimento_3_interpretacao.txt', 'w', encoding='utf-8') as f:
        f.write("EXPERIMENTO 3: SALDO LIMITADO\n")
        f.write("=" * 80 + "\n\n")
        f.write(interpretacao)
    
    print()
    print("=" * 80)
    print("✓ EXPERIMENTO 3 CONCLUÍDO COM SUCESSO!")
    print("=" * 80)
    print()
    print("Arquivos gerados:")
    print(f"  • {csv_resumo}")
    print(f"  • {csv_participantes}")
    print(f"  • {grafico}")
    print(f"  • resultados/experimento_3_interpretacao.txt")
    print()
    print("Este experimento simula de forma realista o comportamento de jogadores com")
    print("saldo limitado. Mesmo com paradas naturais (zeragem), o resultado agregado")
    print(f"é sempre negativo: perda média de {perda_pct:.2f}% do capital inicial.")
    print()
    print(f"Dos {dados['n_participantes']} participantes, {dados['zerou_saldo']} ({dados['proporcao_zerou']*100:.1f}%)")
    print("perderam todo o seu capital antes de completar as 500 rodadas.")
    print()


if __name__ == "__main__":
    main()
