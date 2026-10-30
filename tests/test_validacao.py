"""
Extra C — Validação automatizada

Bateria de verificações de consistência do simulador, organizada pelas
categorias pedidas no enunciado: pagamentos, lucro, semente, totais e
casos-limite. Complementa os testes de cada módulo/experimento.

Executar:
    python -m pytest tests/test_validacao.py -v
"""

from itertools import product

import pytest
from src.maquina import (
    SIMBOLOS,
    TABELA_BASE,
    TABELA_AUMENTADA_10PCT,
    montar_coluna,
    calcular_premio,
    calcular_lucro,
    executar_rodadas
)
from src.calculos import (
    calcular_probabilidades_teoricas,
    calcular_esperanca_lucro,
    calcular_rtp_teorico,
    calcular_probabilidade_premio
)
from src.experimentos import experimento_1, experimento_4, experimento_5


# Todas as 125 linhas centrais possíveis (espaço amostral)
TODAS_AS_TRIPLAS = list(product(SIMBOLOS, repeat=3))

# Primeiras 10 rodadas da semente 2026: (paradas, linha central, prêmio, lucro).
# Referência fixa: se o sorteio ou a montagem mudarem, este teste acusa.
REFERENCIA_SEMENTE_2026 = [
    ((0, 2, 4), ('B', 'D', 'A'), 0, -1),
    ((4, 0, 1), ('A', 'B', 'C'), 0, -1),
    ((4, 4, 4), ('A', 'A', 'A'), 5, 4),
    ((3, 4, 4), ('E', 'A', 'A'), 0, -1),
    ((3, 4, 3), ('E', 'A', 'E'), 0, -1),
    ((1, 0, 4), ('C', 'B', 'A'), 0, -1),
    ((0, 0, 2), ('B', 'B', 'D'), 0, -1),
    ((0, 3, 0), ('B', 'E', 'B'), 0, -1),
    ((3, 2, 1), ('E', 'D', 'C'), 0, -1),
    ((3, 2, 2), ('E', 'D', 'D'), 0, -1),
]


@pytest.fixture(scope='module')
def dados_e1():
    """10.000 rodadas do Experimento 1 (semente 2026)"""
    return experimento_1(n=10000, semente=2026)


class TestPagamentos:
    """1. As cinco triplas pagam o valor da tabela; as outras 120 pagam zero"""

    @pytest.mark.parametrize('simbolo, valor', [
        ('A', 5), ('B', 10), ('C', 15), ('D', 25), ('E', 50)
    ])
    def test_tripla_premiada_paga_valor_da_tabela(self, simbolo, valor):
        assert calcular_premio((simbolo, simbolo, simbolo)) == valor

    def test_demais_120_triplas_pagam_zero(self):
        nao_premiadas = [t for t in TODAS_AS_TRIPLAS if len(set(t)) > 1]
        assert len(nao_premiadas) == 120
        assert all(calcular_premio(t) == 0 for t in nao_premiadas)

    def test_tabela_aumentada_paga_10_porcento_a_mais(self):
        for tripla in TODAS_AS_TRIPLAS:
            assert calcular_premio(tripla, TABELA_AUMENTADA_10PCT) == pytest.approx(
                1.1 * calcular_premio(tripla, TABELA_BASE))

    def test_premios_da_simulacao_seguem_a_tabela(self, dados_e1):
        for r in dados_e1['resultados']:
            assert r['premio'] == TABELA_BASE.get(r['linha_central'], 0)


class TestLucro:
    """2. O lucro desconta a aposta de 1 crédito: X = P - 1"""

    def test_lucro_desconta_aposta_em_todas_as_triplas(self):
        for tripla in TODAS_AS_TRIPLAS:
            assert calcular_lucro(calcular_premio(tripla)) == calcular_premio(tripla) - 1

    def test_sem_premio_perde_um_credito(self):
        assert calcular_lucro(0) == -1

    def test_lucro_de_cada_rodada_simulada(self, dados_e1):
        for r in dados_e1['resultados']:
            assert r['lucro'] == r['premio'] - 1

    def test_valores_teoricos(self):
        assert calcular_probabilidade_premio() == pytest.approx(0.04)
        assert calcular_esperanca_lucro() == pytest.approx(-0.16)
        assert calcular_rtp_teorico() == pytest.approx(0.84)
        assert calcular_esperanca_lucro(TABELA_AUMENTADA_10PCT) == pytest.approx(-0.076)
        assert calcular_rtp_teorico(TABELA_AUMENTADA_10PCT) == pytest.approx(0.924)


class TestSemente:
    """3. A semente reproduz a sequência; sementes diferentes geram sequências diferentes"""

    def test_primeiras_10_rodadas_semente_2026(self):
        obtido = [(r['paradas'], r['linha_central'], r['premio'], r['lucro'])
                  for r in executar_rodadas(10, 2026)]
        assert obtido == REFERENCIA_SEMENTE_2026

    def test_mesma_semente_mesma_sequencia(self):
        assert executar_rodadas(1000, 2026) == executar_rodadas(1000, 2026)

    def test_semente_inicializada_uma_vez(self):
        """10 rodadas seguidas = início de uma sequência mais longa (gerador não reiniciado)"""
        assert executar_rodadas(10, 2026) == executar_rodadas(1000, 2026)[:10]

    def test_sementes_diferentes_sequencias_diferentes(self):
        assert executar_rodadas(100, 10) != executar_rodadas(100, 123456)


class TestTotais:
    """4. Contagens e probabilidades somam o total esperado"""

    def test_espaco_amostral_125_triplas(self):
        assert len(TODAS_AS_TRIPLAS) == len(set(TODAS_AS_TRIPLAS)) == 125

    def test_probabilidades_teoricas_somam_1(self):
        assert sum(calcular_probabilidades_teoricas().values()) == pytest.approx(1.0)

    def test_contagens_e1_somam_10000(self, dados_e1):
        assert sum(dados_e1['contagens'].values()) == 10000
        assert sum(dados_e1['frequencias'].values()) == pytest.approx(1.0)

    def test_pares_e4_somam_9999(self, dados_e1):
        dados = experimento_4(dados_e1['resultados'])
        assert sum(g['total_pares'] for g in dados['grupos'].values()) == 9999

    def test_e5_mesma_quantidade_de_premios_nas_duas_tabelas(self, dados_e1):
        dados = experimento_5(dados_e1['resultados'])
        contagens = [m['premios_observados'] for m in dados['tabelas'].values()]
        assert contagens == [dados_e1['premios_observados']] * 2

    def test_simbolo_central_equiprovavel(self):
        """Cada uma das 5 paradas coloca um símbolo diferente no centro (1/5 cada)"""
        centros = [montar_coluna(k)[1] for k in range(5)]
        assert sorted(centros) == sorted(SIMBOLOS)


class TestCasosLimite:
    """5. Entradas nos limites são tratadas sem erro silencioso"""

    def test_janela_circular_k4(self):
        """K = 4 volta ao início do rolo: (E, A, B) — Figura 3 do enunciado"""
        assert montar_coluna(4) == ('E', 'A', 'B')

    @pytest.mark.parametrize('parada', [-1, 5])
    def test_parada_fora_do_rolo_rejeitada(self, parada):
        with pytest.raises(ValueError):
            montar_coluna(parada)

    def test_zero_rodadas_rejeitado(self):
        with pytest.raises(ValueError):
            executar_rodadas(0, 2026)

    def test_e4_grupo_sem_pares_nao_estimavel(self):
        """Sem rodadas premiadas, a proporção após prêmio é não estimável (sem divisão por zero)"""
        sem_premios = [{'premio': 0, 'lucro': -1}] * 20
        dados = experimento_4(sem_premios)
        assert dados['grupos']['apos_premio']['total_pares'] == 0
        assert dados['grupos']['apos_premio']['proporcao'] is None

    def test_uma_rodada(self):
        resultados = executar_rodadas(1, 2026)
        assert len(resultados) == 1
        assert resultados[0]['lucro'] == resultados[0]['premio'] - 1
