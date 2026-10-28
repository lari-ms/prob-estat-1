"""
Script para executar o Experimento 4 completo
"""

import sys
from src.experimentos import experimento_1, experimento_4, interpretar_experimento_4
from src.exportacao import exportar_experimento_4_csv, salvar_configuracao_execucao

def main():
    print("=" * 80)
    print("EXPERIMENTO 4: PROBABILIDADE CONDICIONAL")
    print("=" * 80)
    print()
    print("Simulador acadêmico - somente créditos fictícios")
    print()
    
    # Reutilizar as 10.000 rodadas do Experimento 1
    print("Obtendo as rodadas do Experimento 1 (10.000 rodadas, semente 2026)...")
    dados_e1 = experimento_1(n=10000, semente=2026)
    dados = experimento_4(dados_e1['resultados'])
    print(f"✓ {dados['n_pares']:,} pares consecutivos analisados")
    print()
    
    # Tabela condicional
    print("-" * 80)
    print(f"{'Resultado anterior':<22} | {'Total de pares':>14} | {'Prêmios seguinte':>16} | {'Proporção':>10}")
    print("-" * 80)
    nomes = {'apos_premio': 'Prêmio (P > 0)', 'apos_nao_premio': 'Sem prêmio (P = 0)'}
    for chave, nome in nomes.items():
        g = dados['grupos'][chave]
        prop = 'não estim.' if g['proporcao'] is None else f"{g['proporcao']*100:9.2f}%"
        print(f"{nome:<22} | {g['total_pares']:14,} | {g['premios_seguinte']:16,} | {prop:>10}")
    print("-" * 80)
    total = sum(g['total_pares'] for g in dados['grupos'].values())
    print(f"{'TOTAL':<22} | {total:14,} |")
    print()
    print(f"Referência do modelo (independência): {dados['probabilidade_teorica']*100:.2f}%")
    print()
    
    # Exportar
    print("Exportando resultados...")
    csv_tabela = exportar_experimento_4_csv(dados)
    print(f"✓ Tabela condicional: {csv_tabela}")
    
    config = salvar_configuracao_execucao('experimento_4', {
        'n_rodadas': dados['n_rodadas'],
        'n_pares': dados['n_pares'],
        'origem_rodadas': 'Experimento 1 (semente 2026)',
        'tabela': 'TABELA_BASE',
        'python_version': sys.version.split()[0],
        'gerador': 'random.Random()'
    })
    print(f"✓ Configuração: {config}")
    print()
    
    # Interpretação (rascunho)
    print("=" * 80)
    print("RASCUNHO DE INTERPRETAÇÃO (revisar antes de usar no relatório)")
    print("=" * 80)
    print()
    interpretacao = interpretar_experimento_4(dados)
    print(interpretacao)
    print()
    
    with open('resultados/experimento_4_interpretacao.txt', 'w', encoding='utf-8') as f:
        f.write("EXPERIMENTO 4: PROBABILIDADE CONDICIONAL\n")
        f.write("=" * 80 + "\n\n")
        f.write(interpretacao)
    
    print()
    print("=" * 80)
    print("✓ EXPERIMENTO 4 CONCLUÍDO COM SUCESSO!")
    print("=" * 80)
    print()
    print("Arquivos gerados:")
    print(f"  • {csv_tabela}")
    print(f"  • {config}")
    print(f"  • resultados/experimento_4_interpretacao.txt")
    print()
    print("Os resultados podem ser inseridos no relatório (Seção 4.5).")
    print()


if __name__ == "__main__":
    main()
