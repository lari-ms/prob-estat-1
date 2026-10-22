"""
Testes do Experimento 1
"""

import pytest
from src.experimentos import experimento_1, interpretar_experimento_1


class TestExperimento1:
    """Testes do Experimento 1: Frequências e Probabilidades"""
    
    def test_experimento_1_executa_numero_correto_rodadas(self):
        """Verifica se executa exatamente n rodadas"""
        dados = experimento_1(n=100, semente=42)
        assert dados['n_rodadas'] == 100
        assert len(dados['resultados']) == 100
    
    def test_experimento_1_reprodutibilidade(self):
        """Verifica se mesma semente produz mesmos resultados"""
        dados1 = experimento_1(n=100, semente=123)
        dados2 = experimento_1(n=100, semente=123)
        
        assert dados1['lucro_medio'] == dados2['lucro_medio']
        assert dados1['rtp_observado'] == dados2['rtp_observado']
        assert dados1['contagens'] == dados2['contagens']
    
    def test_experimento_1_contagens_somam_n(self):
        """Verifica se soma das contagens é n"""
        dados = experimento_1(n=500, semente=2026)
        soma_contagens = sum(dados['contagens'].values())
        assert soma_contagens == dados['n_rodadas']
    
    def test_experimento_1_frequencias_somam_um(self):
        """Verifica se frequências somam 1"""
        dados = experimento_1(n=1000, semente=42)
        soma_frequencias = sum(dados['frequencias'].values())
        assert abs(soma_frequencias - 1.0) < 1e-10
    
    def test_experimento_1_apenas_lucros_validos(self):
        """Verifica se apenas lucros válidos aparecem"""
        dados = experimento_1(n=200, semente=999)
        lucros_validos = {-1, 4, 9, 14, 24, 49}
        
        for lucro in dados['contagens'].keys():
            assert lucro in lucros_validos
    
    def test_experimento_1_rtp_entre_0_e_1(self):
        """Verifica se RTP está no intervalo [0, 1]"""
        dados = experimento_1(n=500, semente=2026)
        assert 0 <= dados['rtp_observado'] <= 1
        assert 0 <= dados['rtp_teorico'] <= 1
    
    def test_experimento_1_desvio_padrao_positivo(self):
        """Verifica se desvio-padrão é positivo"""
        dados = experimento_1(n=1000, semente=42)
        assert dados['desvio_padrao'] > 0
    
    def test_experimento_1_premios_dentro_limites(self):
        """Verifica se número de prêmios está em intervalo razoável"""
        dados = experimento_1(n=10000, semente=2026)
        
        # Com p=0.04 e n=10000, esperamos ~400 prêmios
        # Intervalo razoável: 3 desvios-padrão
        # std = sqrt(n*p*(1-p)) = sqrt(10000*0.04*0.96) ≈ 19.6
        esperado = 400
        std = (10000 * 0.04 * 0.96) ** 0.5
        
        assert esperado - 3*std < dados['premios_observados'] < esperado + 3*std
    
    def test_experimento_1_lucro_medio_proximo_teorico(self):
        """Verifica se lucro médio está próximo do teórico com n grande"""
        dados = experimento_1(n=10000, semente=2026)
        
        # Com n=10000, o lucro médio deve estar razoavelmente próximo de -0.16
        # Margem de 0.1 crédito (bem generosa)
        assert abs(dados['lucro_medio'] - (-0.16)) < 0.1
    
    def test_experimento_1_estrutura_completa(self):
        """Verifica se o resultado tem todas as chaves esperadas"""
        dados = experimento_1(n=100, semente=42)
        
        chaves_esperadas = {
            'n_rodadas', 'semente', 'resultados', 'contagens',
            'frequencias', 'probabilidades_teoricas', 'lucro_medio',
            'rtp_observado', 'rtp_teorico', 'proporcao_premios',
            'desvio_padrao', 'premios_observados', 'premios_esperados'
        }
        
        assert set(dados.keys()) == chaves_esperadas
    
    def test_experimento_1_proporcao_premios_entre_0_e_1(self):
        """Verifica se proporção de prêmios está no intervalo [0, 1]"""
        dados = experimento_1(n=500, semente=42)
        assert 0 <= dados['proporcao_premios'] <= 1
    
    def test_interpretar_experimento_1_retorna_string(self):
        """Verifica se interpretação retorna string não vazia"""
        dados = experimento_1(n=100, semente=42)
        interpretacao = interpretar_experimento_1(dados)
        
        assert isinstance(interpretacao, str)
        assert len(interpretacao) > 100
    
    def test_interpretar_experimento_1_menciona_conceitos_chave(self):
        """Verifica se interpretação menciona conceitos importantes"""
        dados = experimento_1(n=1000, semente=2026)
        interpretacao = interpretar_experimento_1(dados)
        
        # Deve mencionar conceitos-chave
        assert 'probabilidades teóricas' in interpretacao.lower() or 'prob' in interpretacao.lower()
        assert 'rtp' in interpretacao.lower()
        assert 'lucro' in interpretacao.lower()


class TestCasosLimiteExperimento1:
    """Testes de casos limite"""
    
    def test_experimento_1_n_minimo(self):
        """Verifica funcionamento com n=1"""
        dados = experimento_1(n=1, semente=42)
        assert dados['n_rodadas'] == 1
        assert len(dados['resultados']) == 1
    
    def test_experimento_1_diferentes_sementes_diferentes_resultados(self):
        """Verifica que sementes diferentes produzem resultados diferentes"""
        dados1 = experimento_1(n=1000, semente=42)
        dados2 = experimento_1(n=1000, semente=123)
        
        # Com alta probabilidade, os lucros médios serão diferentes
        assert dados1['lucro_medio'] != dados2['lucro_medio']
    
    def test_experimento_1_premios_observados_eh_inteiro(self):
        """Verifica que número de prêmios observados é inteiro"""
        dados = experimento_1(n=500, semente=2026)
        assert isinstance(dados['premios_observados'], int)
    
    def test_experimento_1_contagens_sao_inteiras(self):
        """Verifica que todas as contagens são inteiras"""
        dados = experimento_1(n=200, semente=42)
        
        for contagem in dados['contagens'].values():
            assert isinstance(contagem, int)
            assert contagem >= 0
