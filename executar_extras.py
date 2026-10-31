"""
Script para executar os itens extras:
- Extra A: Intervalos de confiança
- Extra B: Mesma média, riscos diferentes
"""

import sys
from src.experimentos import experimento_1
from src.exportacao import salvar_configuracao_execucao
from src.extras import (
    extra_intervalos_confianca,
    exportar_extra_intervalos_csv,
    grafico_extra_intervalos,
    extra_mesma_media,
    exportar_extra_mesma_media_csv,
    grafico_extra_mesma_media
)


def fmt(valor, casas=4):
    """Formata número com vírgula decimal."""
    return f"{valor:.{casas}f}".replace('.', ',')


def main():
    print("=" * 80)
    print("ITENS EXTRAS")
    print("=" * 80)
    print()
    print("Simulador acadêmico - somente créditos fictícios")
    print()
    
    dados_e1 = experimento_1(n=10000, semente=2026)
    arquivos = []
    
    # --------------------------------------------------------------------------
    print("-" * 80)
    print("EXTRA A: INTERVALOS DE CONFIANÇA (95%)")
    print("-" * 80)
    print("Executando 200 sequências independentes de 10.000 rodadas (sementes 1 a 200)...")
    a = extra_intervalos_confianca(dados_e1['resultados'], n_execucoes=200)
    print()
    for rotulo, ic, ref in [('Lucro médio', a['ic_lucro'], a['esperanca_teorica']),
                            ('RTP', a['ic_rtp'], a['rtp_teorico'])]:
        print(f"{rotulo} (E1, n = {ic['n']:,}): {fmt(ic['media'])}  "
              f"IC 95% = [{fmt(ic['inferior'])}; {fmt(ic['superior'])}]  "
              f"teórico {fmt(ref, 2)} {'dentro' if ic['contem_teorico'] else 'FORA'}")
    print()
    print("Largura do IC do lucro médio conforme o tamanho da amostra (E1):")
    for m, ic in a['ic_por_n'].items():
        print(f"  n = {m:>6,}: [{fmt(ic['inferior'])}; {fmt(ic['superior'])}]  "
              f"largura {fmt(ic['superior'] - ic['inferior'])}")
    print()
    dentro = round(a['cobertura'] * a['n_execucoes'])
    print(f"Cobertura: {dentro} de {a['n_execucoes']} intervalos contêm E[X] = -0,16 "
          f"({fmt(a['cobertura'] * 100, 1)}%; esperado em torno de 95%)")
    print()
    arquivos += exportar_extra_intervalos_csv(a)
    arquivos.append(grafico_extra_intervalos(a))
    
    # --------------------------------------------------------------------------
    print("-" * 80)
    print("EXTRA B: MESMA MÉDIA, RISCOS DIFERENTES")
    print("-" * 80)
    b = extra_mesma_media(dados_e1['resultados'])
    print(f"Sessões: {b['n_participantes']} participantes, saldo inicial {b['saldo_inicial']:.0f}, "
          f"até {b['max_rodadas']} rodadas, semente {b['semente_sessoes']} (mesmos sorteios nas três tabelas)")
    print()
    for nome, d in b['tabelas'].items():
        t, o, s = d['teorico'], d['observado_e1'], d['sessoes']
        print(nome)
        print(f"  Teórico:  E[X] = {fmt(t['esperanca_lucro'])}  RTP = {fmt(t['rtp'] * 100, 1)}%  "
              f"desvio-padrão de X = {fmt(t['desvio_padrao_lucro'])}  P(prêmio) = {fmt(t['prob_premio'] * 100, 1)}%")
        print(f"  E1:       lucro médio = {fmt(o['lucro_medio'])}  desvio-padrão = {fmt(o['desvio_padrao'])}")
        print(f"  Sessões:  ganho {fmt(s['proporcao_ganho'] * 100, 0)}% | empate {fmt(s['proporcao_empate'] * 100, 0)}% | "
              f"perda {fmt(s['proporcao_perda'] * 100, 0)}% (esgotamento {fmt(s['proporcao_esgotamento'] * 100, 0)}%)")
        print(f"            saldo final: média {fmt(s['media_saldo_final'], 1)}, mediana {fmt(s['mediana_saldo_final'], 1)}, "
              f"percentil 90 {fmt(s['percentil_90'], 1)}, maior {fmt(s['maior_saldo_final'], 1)}; "
              f"rodadas em média {fmt(s['media_rodadas'], 1)}")
        print()
    arquivos += exportar_extra_mesma_media_csv(b)
    arquivos.append(grafico_extra_mesma_media(b))
    
    config = salvar_configuracao_execucao('extras', {
        'extra_a_origem': 'Experimento 1 (10.000 rodadas, semente 2026)',
        'extra_a_execucoes_independentes': '200 x 10.000 rodadas, sementes 1 a 200',
        'extra_a_metodo': 'IC 95% = media +- 1,96 s/raiz(n)',
        'extra_b_tabelas': '; '.join(b['tabelas'].keys()),
        'extra_b_sessoes': '100 participantes, saldo 100, ate 500 rodadas, semente 42 (uma vez)',
        'python_version': sys.version.split()[0],
        'gerador': 'random.Random()'
    })
    arquivos.append(config)
    
    print("=" * 80)
    print("✓ EXTRAS CONCLUÍDOS")
    print("=" * 80)
    print("Arquivos gerados:")
    for arq in arquivos:
        print(f"  • {arq}")
    print()


if __name__ == "__main__":
    main()
