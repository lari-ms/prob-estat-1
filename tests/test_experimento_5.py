"""
Testes do Experimento 5
"""

import pytest
from src.maquina import executar_rodadas, TABELA_BASE
from src.experimentos import experimento_1, experimento_5, interpretar_experimento_5


class TestExperimento5:
    """Testes do Experimento 5: Comparação de Tabelas de Pagamento"""
    
    @pytest.fixture(scope='class')
    def dados(self):
        return experimento_5(experimento_1()['resultados'])
    
    def test_experimento_5_duas_tabelas(self, dados):
        """Compara base e +10% sobre 10.000 rodadas"""
        assert list(dados['tabelas'].keys()) == ['Base', 'Prêmios +10%']
        assert dados['n_rodadas'] == 10000
    
    def test_experimento_5_base_igual_experimento_1(self, dados):
        """Tabela base reproduz as métricas do Experimento 1"""
        e1 = experimento_1()
        base = dados['tabelas']['Base']
        assert base['lucro_medio'] == pytest.approx(e1['lucro_medio'])
        assert base['rtp_observado'] == pytest.approx(e1['rtp_observado'])
        assert base['premios_observados'] == e1['premios_observados']
    
    def test_experimento_5_mesma_frequencia_de_premio(self, dados):
        """Mesmas rodadas → mesma frequência de prêmio nas duas tabelas"""
        base, aumentada = dados['tabelas']['Base'], dados['tabelas']['Prêmios +10%']
        assert base['premios_observados'] == aumentada['premios_observados']
        assert base['prob_premio_teorica'] == aumentada['prob_premio_teorica'] == pytest.approx(0.04)
    
    def test_experimento_5_premio_medio_10_porcento_maior(self, dados):
        """Mesmas rodadas → prêmio médio e RTP observado exatamente 1,1 vez maiores"""
        base, aumentada = dados['tabelas']['Base'], dados['tabelas']['Prêmios +10%']
        assert aumentada['premio_medio'] == pytest.approx(1.1 * base['premio_medio'])
        assert aumentada['rtp_observado'] == pytest.approx(1.1 * base['rtp_observado'])
    
    def test_experimento_5_valores_teoricos(self, dados):
        """RTP = 84% e 92,4%; E[X] = -0,16 e -0,076"""
        base, aumentada = dados['tabelas']['Base'], dados['tabelas']['Prêmios +10%']
        assert base['rtp_teorico'] == pytest.approx(0.84)
        assert base['lucro_esperado_teorico'] == pytest.approx(-0.16)
        assert aumentada['rtp_teorico'] == pytest.approx(0.924)
        assert aumentada['lucro_esperado_teorico'] == pytest.approx(-0.076)
    
    def test_experimento_5_lucro_igual_premio_menos_aposta(self, dados):
        """Lucro médio = prêmio médio - 1 em cada tabela"""
        for m in dados['tabelas'].values():
            assert m['lucro_medio'] == pytest.approx(m['premio_medio'] - 1)
    
    def test_experimento_5_nao_sorteia_novamente(self):
        """Usa as linhas centrais recebidas, sem novo sorteio"""
        resultados = executar_rodadas(500, 99)
        dados = experimento_5(resultados, {'Base': TABELA_BASE})
        assert dados['tabelas']['Base']['premio_medio'] == pytest.approx(
            sum(r['premio'] for r in resultados) / 500)
    
    def test_experimento_5_reutiliza_experimento_1_por_padrao(self, dados):
        """Sem argumentos, usa as rodadas do Experimento 1"""
        assert experimento_5() == dados
    
    def test_interpretar_experimento_5_menciona_conceitos(self, dados):
        """Rascunho cita as tabelas, RTPs e a conclusão"""
        texto = interpretar_experimento_5(dados)
        for termo in ['Base', 'Prêmios +10%', '84.0%', '92.4%', 'continua negativa']:
            assert termo in texto
