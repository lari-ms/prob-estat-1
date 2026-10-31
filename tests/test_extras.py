"""
Testes dos itens extras (intervalos de confiança; mesma média, riscos diferentes)
"""

import math
import numpy as np
import pytest
from src.maquina import executar_rodadas, TABELA_BASE
from src.extras import (
    intervalo_confianca_media,
    extra_intervalos_confianca,
    momentos_teoricos,
    gerar_linhas_participantes,
    simular_sessao,
    extra_mesma_media,
    TABELA_BAIXO_RISCO,
    TABELA_ALTO_RISCO
)


@pytest.fixture(scope='module')
def rodadas_e1():
    return executar_rodadas(10000, 2026)


class TestIntervaloConfianca:
    """Extra A: intervalos de confiança"""
    
    def test_ic_valores_conhecidos(self):
        ic = intervalo_confianca_media([1, 2, 3, 4, 5], z=2)
        # média 3, s = √2,5, erro-padrão = √2,5/√5 = √0,5
        assert ic['media'] == pytest.approx(3)
        assert ic['erro_padrao'] == pytest.approx(math.sqrt(0.5))
        assert ic['inferior'] == pytest.approx(3 - 2 * math.sqrt(0.5))
        assert ic['superior'] == pytest.approx(3 + 2 * math.sqrt(0.5))
    
    def test_ic_simetrico_em_torno_da_media(self):
        ic = intervalo_confianca_media([r['lucro'] for r in executar_rodadas(500, 3)])
        assert ic['media'] - ic['inferior'] == pytest.approx(ic['superior'] - ic['media'])
    
    def test_ic_precisa_de_duas_observacoes(self):
        with pytest.raises(ValueError):
            intervalo_confianca_media([1.0])
    
    def test_ic_e1_contem_valores_teoricos(self, rodadas_e1):
        dados = extra_intervalos_confianca(rodadas_e1, n_execucoes=0)
        assert dados['ic_lucro']['media'] == pytest.approx(-0.1315)
        assert dados['ic_lucro']['contem_teorico']
        assert dados['ic_rtp']['contem_teorico']
    
    def test_ic_rtp_e_lucro_tem_mesma_largura(self, rodadas_e1):
        """P = X + 1: mesmo desvio-padrão, intervalo deslocado em 1"""
        dados = extra_intervalos_confianca(rodadas_e1, n_execucoes=0)
        assert dados['ic_rtp']['inferior'] == pytest.approx(dados['ic_lucro']['inferior'] + 1)
        assert dados['ic_rtp']['margem'] == pytest.approx(dados['ic_lucro']['margem'])
    
    def test_ic_estreita_com_n(self, rodadas_e1):
        dados = extra_intervalos_confianca(rodadas_e1, n_execucoes=0)
        margens = [dados['ic_por_n'][m]['margem'] for m in (100, 1000, 10000)]
        assert margens[0] > margens[1] > margens[2]
    
    def test_cobertura_proxima_de_95(self, rodadas_e1):
        """Execuções independentes: cerca de 95% dos intervalos contêm -0,16"""
        dados = extra_intervalos_confianca(rodadas_e1, n_execucoes=40, n_rodadas=2000)
        assert len(dados['execucoes']) == 40
        assert 0.8 <= dados['cobertura'] <= 1.0
        assert [ic['semente'] for ic in dados['execucoes']] == list(range(1, 41))


class TestMesmaMedia:
    """Extra B: mesma média, riscos diferentes"""
    
    @pytest.mark.parametrize('tabela', [TABELA_BASE, TABELA_BAIXO_RISCO, TABELA_ALTO_RISCO])
    def test_mesma_esperanca_e_rtp(self, tabela):
        m = momentos_teoricos(tabela)
        assert m['esperanca_lucro'] == pytest.approx(-0.16)
        assert m['rtp'] == pytest.approx(0.84)
    
    def test_variancias_diferentes(self):
        base = momentos_teoricos(TABELA_BASE)['variancia_lucro']
        baixo = momentos_teoricos(TABELA_BAIXO_RISCO)['variancia_lucro']
        alto = momentos_teoricos(TABELA_ALTO_RISCO)['variancia_lucro']
        assert base == pytest.approx(27.0944)
        assert baixo < base < alto
    
    def test_variancia_teorica_confere_com_distribuicao(self):
        """Var(X) calculada pela distribuição completa das 125 triplas"""
        lucros = np.array([TABELA_BASE.get(t, 0) - 1 for t in
                           [(a, b, c) for a in 'ABCDE' for b in 'ABCDE' for c in 'ABCDE']])
        assert np.var(lucros) == pytest.approx(momentos_teoricos(TABELA_BASE)['variancia_lucro'])
    
    def test_sessao_para_quando_saldo_acaba(self):
        linhas = [('A', 'B', 'C')] * 10
        sessao = simular_sessao(linhas, TABELA_BASE, saldo_inicial=3)
        assert sessao['saldo_final'] == 0
        assert sessao['rodadas'] == 3
        assert sessao['esgotou']
        assert sessao['trajetoria'] == [3, 2, 1, 0]
    
    def test_sessao_para_no_limite_de_rodadas(self):
        linhas = [('A', 'A', 'A')] * 5
        sessao = simular_sessao(linhas, TABELA_BASE, saldo_inicial=1)
        assert sessao['rodadas'] == 5
        assert sessao['saldo_final'] == 1 + 5 * 4
        assert not sessao['esgotou']
    
    def test_linhas_participantes_semente_uma_vez(self):
        """Participantes recebem trechos consecutivos de UMA sequência"""
        linhas = gerar_linhas_participantes(3, 10, 42)
        sequencia = [r['linha_central'] for r in executar_rodadas(30, 42)]
        assert linhas[0] + linhas[1] + linhas[2] == sequencia
    
    def test_mesmos_sorteios_em_todas_as_tabelas(self, rodadas_e1):
        dados = extra_mesma_media(rodadas_e1, n_participantes=20, max_rodadas=100)
        base = dados['tabelas']['Base']
        baixo = dados['tabelas']['Baixo risco (todas pagam 21)']
        alto = dados['tabelas']['Alto risco (só E-E-E paga 105)']
        assert base['observado_e1']['freq_premio'] == baixo['observado_e1']['freq_premio']
        assert alto['observado_e1']['freq_premio'] < base['observado_e1']['freq_premio']
        assert base['observado_e1']['lucro_medio'] == pytest.approx(-0.1315)
    
    def test_proporcoes_somam_100(self, rodadas_e1):
        dados = extra_mesma_media(rodadas_e1, n_participantes=20, max_rodadas=100)
        for d in dados['tabelas'].values():
            s = d['sessoes']
            assert s['proporcao_ganho'] + s['proporcao_empate'] + s['proporcao_perda'] == pytest.approx(1)
            assert s['proporcao_esgotamento'] <= s['proporcao_perda']
            assert len(d['saldos_finais']) == 20
