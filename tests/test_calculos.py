"""
Testes do módulo calculos.py
Valida os cálculos teóricos de probabilidade, esperança e RTP.
"""

import pytest
from src.calculos import (
    calcular_probabilidades_teoricas,
    calcular_esperanca_premio,
    calcular_esperanca_lucro,
    calcular_rtp_teorico,
    calcular_probabilidade_premio,
    obter_valores_teoricos_referencia,
    validar_valores_teoricos_tabela_base,
    validar_valores_teoricos_tabela_aumentada
)
from src.maquina import TABELA_BASE, TABELA_AUMENTADA_10PCT


class TestProbabilidadesTeoricas:
    """Testes da distribuição de probabilidades"""
    
    def test_probabilidades_somam_um(self):
        """Verifica se as probabilidades somam 1"""
        dist = calcular_probabilidades_teoricas()
        soma = sum(dist.values())
        assert abs(soma - 1.0) < 1e-10, f"Soma das probabilidades: {soma}"
    
    def test_seis_lucros_possiveis(self):
        """Verifica que existem exatamente 6 lucros possíveis"""
        dist = calcular_probabilidades_teoricas()
        assert len(dist) == 6, f"Número de lucros distintos: {len(dist)}"
    
    def test_lucros_corretos(self):
        """Verifica se os lucros estão corretos"""
        dist = calcular_probabilidades_teoricas()
        lucros_esperados = {-1, 4, 9, 14, 24, 49}
        lucros_obtidos = set(dist.keys())
        
        assert lucros_obtidos == lucros_esperados, \
            f"Lucros diferentes do esperado: {lucros_obtidos}"
    
    def test_probabilidade_perda(self):
        """Verifica P(X = -1) = 120/125 = 96%"""
        dist = calcular_probabilidades_teoricas()
        prob_perda = dist[-1]
        
        esperado = 120 / 125
        assert abs(prob_perda - esperado) < 1e-10, \
            f"P(X=-1) = {prob_perda}, esperado {esperado}"
    
    def test_probabilidade_cada_premio(self):
        """Verifica que cada prêmio tem probabilidade 1/125"""
        dist = calcular_probabilidades_teoricas()
        prob_esperada = 1 / 125
        
        for lucro in [4, 9, 14, 24, 49]:
            assert abs(dist[lucro] - prob_esperada) < 1e-10, \
                f"P(X={lucro}) = {dist[lucro]}, esperado {prob_esperada}"


class TestEsperancas:
    """Testes das esperanças matemáticas"""
    
    def test_esperanca_premio_tabela_base(self):
        """Verifica E[P] = 0.84 para tabela base"""
        ep = calcular_esperanca_premio(TABELA_BASE)
        assert abs(ep - 0.84) < 1e-10, f"E[P] = {ep}, esperado 0.84"
    
    def test_esperanca_lucro_tabela_base(self):
        """Verifica E[X] = -0.16 para tabela base"""
        ex = calcular_esperanca_lucro(TABELA_BASE)
        assert abs(ex - (-0.16)) < 1e-10, f"E[X] = {ex}, esperado -0.16"
    
    def test_esperanca_premio_tabela_aumentada(self):
        """Verifica E[P] = 0.924 para tabela aumentada"""
        ep = calcular_esperanca_premio(TABELA_AUMENTADA_10PCT)
        assert abs(ep - 0.924) < 1e-10, f"E[P] = {ep}, esperado 0.924"
    
    def test_esperanca_lucro_tabela_aumentada(self):
        """Verifica E[X] = -0.076 para tabela aumentada"""
        ex = calcular_esperanca_lucro(TABELA_AUMENTADA_10PCT)
        assert abs(ex - (-0.076)) < 1e-10, f"E[X] = {ex}, esperado -0.076"
    
    def test_relacao_esperanca_lucro_e_premio(self):
        """Verifica que E[X] = E[P] - 1"""
        ep = calcular_esperanca_premio()
        ex = calcular_esperanca_lucro()
        
        assert abs(ex - (ep - 1)) < 1e-10, \
            f"E[X] = {ex}, E[P] - 1 = {ep - 1}"


class TestRTP:
    """Testes do Return to Player"""
    
    def test_rtp_tabela_base(self):
        """Verifica RTP = 84% para tabela base"""
        rtp = calcular_rtp_teorico(TABELA_BASE)
        assert abs(rtp - 0.84) < 1e-10, f"RTP = {rtp}, esperado 0.84"
    
    def test_rtp_tabela_aumentada(self):
        """Verifica RTP = 92.4% para tabela aumentada"""
        rtp = calcular_rtp_teorico(TABELA_AUMENTADA_10PCT)
        assert abs(rtp - 0.924) < 1e-10, f"RTP = {rtp}, esperado 0.924"
    
    def test_rtp_igual_esperanca_premio(self):
        """Verifica que RTP = E[P] (aposta unitária)"""
        rtp = calcular_rtp_teorico()
        ep = calcular_esperanca_premio()
        
        assert abs(rtp - ep) < 1e-10, \
            f"RTP = {rtp}, E[P] = {ep}"


class TestProbabilidadePremio:
    """Testes da probabilidade de receber algum prêmio"""
    
    def test_probabilidade_premio_tabela_base(self):
        """Verifica P(prêmio) = 5/125 = 4%"""
        prob = calcular_probabilidade_premio(TABELA_BASE)
        esperado = 5 / 125
        
        assert abs(prob - esperado) < 1e-10, \
            f"P(prêmio) = {prob}, esperado {esperado}"
    
    def test_probabilidade_premio_tabela_aumentada_inalterada(self):
        """Verifica que P(prêmio) permanece 4% na tabela aumentada"""
        prob = calcular_probabilidade_premio(TABELA_AUMENTADA_10PCT)
        esperado = 5 / 125
        
        assert abs(prob - esperado) < 1e-10, \
            f"P(prêmio) = {prob}, esperado {esperado} (inalterado)"


class TestValoresReferencia:
    """Testes dos valores de referência completos"""
    
    def test_valores_referencia_estrutura(self):
        """Verifica se retorna todas as chaves esperadas"""
        valores = obter_valores_teoricos_referencia()
        
        chaves_esperadas = {
            'espaco_amostral',
            'n_triplas_premiadas',
            'prob_premio',
            'prob_sem_premio',
            'esperanca_premio',
            'esperanca_lucro',
            'rtp',
            'vantagem_operador',
            'distribuicao_lucro'
        }
        
        assert set(valores.keys()) == chaves_esperadas, \
            f"Chaves faltando ou extras: {set(valores.keys()) ^ chaves_esperadas}"
    
    def test_espaco_amostral(self):
        """Verifica que o espaço amostral tem 125 elementos"""
        valores = obter_valores_teoricos_referencia()
        assert valores['espaco_amostral'] == 125
    
    def test_prob_premio_mais_prob_sem_premio(self):
        """Verifica que P(prêmio) + P(sem prêmio) = 1"""
        valores = obter_valores_teoricos_referencia()
        soma = valores['prob_premio'] + valores['prob_sem_premio']
        
        assert abs(soma - 1.0) < 1e-10, \
            f"P(prêmio) + P(sem prêmio) = {soma}, esperado 1.0"
    
    def test_vantagem_operador(self):
        """Verifica que vantagem = 1 - RTP"""
        valores = obter_valores_teoricos_referencia()
        
        vantagem_calculada = 1 - valores['rtp']
        assert abs(valores['vantagem_operador'] - vantagem_calculada) < 1e-10, \
            f"Vantagem inconsistente: {valores['vantagem_operador']}"


class TestValidacoes:
    """Testes das funções de validação"""
    
    def test_validacao_tabela_base(self):
        """Verifica se a validação da tabela base passa"""
        ok, msg = validar_valores_teoricos_tabela_base()
        assert ok, f"Validação falhou: {msg}"
    
    def test_validacao_tabela_aumentada(self):
        """Verifica se a validação da tabela aumentada passa"""
        ok, msg = validar_valores_teoricos_tabela_aumentada()
        assert ok, f"Validação falhou: {msg}"
    
    def test_valores_diferentes_entre_tabelas(self):
        """Verifica que as duas tabelas têm RTP diferentes"""
        rtp_base = calcular_rtp_teorico(TABELA_BASE)
        rtp_aumentada = calcular_rtp_teorico(TABELA_AUMENTADA_10PCT)
        
        assert rtp_aumentada > rtp_base, \
            f"RTP aumentada ({rtp_aumentada}) deve ser > base ({rtp_base})"
        
        # Verificar que a diferença está próxima de 8.4 pontos percentuais
        diferenca = rtp_aumentada - rtp_base
        esperado = 0.084  # 92.4% - 84% = 8.4%
        
        assert abs(diferenca - esperado) < 1e-10, \
            f"Diferença RTP = {diferenca}, esperado {esperado}"


class TestConsistenciaMatematica:
    """Testes de consistência entre diferentes cálculos"""
    
    def test_esperanca_via_distribuicao(self):
        """Verifica E[X] calculando pela distribuição"""
        dist = calcular_probabilidades_teoricas()
        
        # E[X] = soma de x * P(X = x)
        ex_via_dist = sum(lucro * prob for lucro, prob in dist.items())
        ex_direto = calcular_esperanca_lucro()
        
        assert abs(ex_via_dist - ex_direto) < 1e-10, \
            f"E[X] via distribuição = {ex_via_dist}, direto = {ex_direto}"
    
    def test_prob_premio_via_distribuicao(self):
        """Verifica P(prêmio > 0) calculando pela distribuição"""
        dist = calcular_probabilidades_teoricas()
        
        # Soma das probabilidades de lucros positivos
        prob_via_dist = sum(prob for lucro, prob in dist.items() if lucro > 0)
        prob_direta = calcular_probabilidade_premio()
        
        assert abs(prob_via_dist - prob_direta) < 1e-10, \
            f"P(prêmio) via distribuição = {prob_via_dist}, direta = {prob_direta}"
