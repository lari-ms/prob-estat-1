"""
Testes do Experimento 4
"""

import pytest
from src.maquina import executar_rodadas
from src.experimentos import experimento_1, experimento_4, interpretar_experimento_4


def rodadas_com_premios(padrao):
    """Cria rodadas sintéticas: True = premiada (P=5), False = sem prêmio (P=0)"""
    return [{'premio': 5 if p else 0, 'lucro': 4 if p else -1} for p in padrao]


class TestExperimento4:
    """Testes do Experimento 4: Probabilidade Condicional"""
    
    def test_experimento_4_9999_pares(self):
        """10.000 rodadas do Experimento 1 geram 9.999 pares"""
        dados = experimento_4(experimento_1()['resultados'])
        assert dados['n_rodadas'] == 10000
        assert dados['n_pares'] == 9999
    
    def test_experimento_4_grupos_somam_pares(self):
        """Os dois grupos somam todos os pares"""
        dados = experimento_4(executar_rodadas(2000, 5))
        total = sum(g['total_pares'] for g in dados['grupos'].values())
        assert total == dados['n_pares'] == 1999
    
    def test_experimento_4_contagem_manual(self):
        """Confere a contagem em uma sequência conhecida"""
        # Pares: (S,P) (P,P) (P,S) (S,S) (S,P)
        dados = experimento_4(rodadas_com_premios([False, True, True, False, False, True]))
        assert dados['grupos']['apos_premio'] == {
            'total_pares': 2, 'premios_seguinte': 1, 'proporcao': 0.5}
        assert dados['grupos']['apos_nao_premio']['total_pares'] == 3
        assert dados['grupos']['apos_nao_premio']['premios_seguinte'] == 2
        assert dados['grupos']['apos_nao_premio']['proporcao'] == pytest.approx(2 / 3)
    
    def test_experimento_4_grupo_vazio_nao_estimavel(self):
        """Sem pares após prêmio, a proporção é None (sem divisão por zero)"""
        dados = experimento_4(rodadas_com_premios([False] * 10))
        assert dados['grupos']['apos_premio']['total_pares'] == 0
        assert dados['grupos']['apos_premio']['proporcao'] is None
        assert dados['grupos']['apos_nao_premio']['proporcao'] == 0
    
    def test_experimento_4_grupo_apos_premio_igual_premios_menos_ultima(self):
        """Pares após prêmio = rodadas premiadas, exceto a última rodada"""
        resultados = experimento_1()['resultados']
        premiadas_exceto_ultima = sum(1 for r in resultados[:-1] if r['premio'] > 0)
        dados = experimento_4(resultados)
        assert dados['grupos']['apos_premio']['total_pares'] == premiadas_exceto_ultima
    
    def test_experimento_4_reutiliza_experimento_1_por_padrao(self):
        """Sem argumentos, usa as rodadas do Experimento 1"""
        assert experimento_4() == experimento_4(experimento_1()['resultados'])
    
    def test_experimento_4_referencia_4_porcento(self):
        """Referência de independência é 4%"""
        dados = experimento_4(executar_rodadas(10, 1))
        assert dados['probabilidade_teorica'] == pytest.approx(0.04)
    
    def test_experimento_4_menos_de_duas_rodadas(self):
        """Menos de 2 rodadas não formam pares"""
        with pytest.raises(ValueError):
            experimento_4(executar_rodadas(1, 1))
    
    def test_interpretar_experimento_4_menciona_conceitos(self):
        """Rascunho cita pares, referência e falácia do jogador"""
        texto = interpretar_experimento_4(experimento_4())
        for termo in ['9,999', '4%', 'falácia do jogador']:
            assert termo in texto
    
    def test_interpretar_experimento_4_grupo_vazio(self):
        """Rascunho informa grupo não estimável"""
        texto = interpretar_experimento_4(experimento_4(rodadas_com_premios([False] * 5)))
        assert 'não estimável' in texto
