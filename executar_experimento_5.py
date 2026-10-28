"""
Script para executar o Experimento 5 completo
"""

import sys
from src.experimentos import experimento_1, experimento_5, interpretar_experimento_5
from src.exportacao import exportar_experimento_5_csv, salvar_configuracao_execucao

def main():
    print("=" * 80)
    print("EXPERIMENTO 5: COMPARAÇÃO DE TABELAS DE PAGAMENTO")
    print("=" * 80)
    print()
    print("Simulador acadêmico - somente créditos fictícios")
    print()
    
    # Reutilizar as 10.000 rodadas do Experimento 1 (sem novo sorteio)
    print("Obtendo as rodadas do Experimento 1 (10.000 rodadas, semente 2026)...")
    dados_e1 = experimento_1(n=10000, semente=2026)
    dados = experimento_5(dados_e1['resultados'])
    print("✓ Tabelas base e +10% aplicadas às mesmas rodadas")
    print()
    
    # Tabela comparativa
    nomes = list(dados['tabelas'].keys())
    linhas = [
        ('Probabilidade de prêmio (teórica)', 'prob_premio_teorica', 100, '%'),
        ('Frequência de prêmio (observada)', 'freq_premio_observada', 100, '%'),
        ('Prêmio médio (observado)', 'premio_medio', 1, ''),
        ('Lucro médio (observado)', 'lucro_medio', 1, ''),
        ('Lucro esperado (teórico)', 'lucro_esperado_teorico', 1, ''),
        ('RTP teórico', 'rtp_teorico', 100, '%'),
        ('RTP observado', 'rtp_observado', 100, '%'),
    ]
    print("-" * 80)
    print(f"{'Métrica':<36} | " + " | ".join(f"{n:>15}" for n in nomes))
    print("-" * 80)
    for rotulo, chave, fator, sufixo in linhas:
        valores = " | ".join(f"{dados['tabelas'][n][chave]*fator:14.4f}{sufixo or ' '}" for n in nomes)
        print(f"{rotulo:<36} | {valores}")
    print()
    
    # Exportar
    print("Exportando resultados...")
    csv_tabela = exportar_experimento_5_csv(dados)
    print(f"✓ Tabela comparativa: {csv_tabela}")
    
    config = salvar_configuracao_execucao('experimento_5', {
        'n_rodadas': dados['n_rodadas'],
        'origem_rodadas': 'Experimento 1 (semente 2026)',
        'tabelas': ', '.join(nomes),
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
    interpretacao = interpretar_experimento_5(dados)
    print(interpretacao)
    print()
    
    with open('resultados/experimento_5_interpretacao.txt', 'w', encoding='utf-8') as f:
        f.write("EXPERIMENTO 5: COMPARAÇÃO DE TABELAS DE PAGAMENTO\n")
        f.write("=" * 80 + "\n\n")
        f.write(interpretacao)
    
    print()
    print("=" * 80)
    print("✓ EXPERIMENTO 5 CONCLUÍDO COM SUCESSO!")
    print("=" * 80)
    print()
    print("Arquivos gerados:")
    print(f"  • {csv_tabela}")
    print(f"  • {config}")
    print(f"  • resultados/experimento_5_interpretacao.txt")
    print()
    print("Os resultados podem ser inseridos no relatório (Seção 4.6).")
    print()


if __name__ == "__main__":
    main()
