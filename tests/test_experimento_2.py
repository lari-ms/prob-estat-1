"""
Testes para o Experimento 2 - Lei dos Grandes Números
"""

import pytest
import numpy as np
from src.experimentos import experimento_2, interpretar_experimento_2
from src.calculos import calcular_esperanca_lucro


class TestExperimento2:
    """Testes básicos do Experimento 2"""
    
    def test_experimento_2_executa_com_parametros_padrao(self):
        """Testa se o experimento executa com parâmetros padrão"""
        dados = experimento_2()
        
        assert 'sementes' in dados
        assert 'n_rodadas' in dados
        assert 'sequencias' in dados
        assert 'medias_acumuladas' in dados
        assert 'trajetorias' in dados
    
    def test_experimento_2_tem_3_sequencias_padrao(self):
        """Testa se retorna 3 sequências por padrão"""
        dados = experimento_2()
        
        assert len(dados['sementes']) == 3
        assert len(dados['sequencias']) == 3
        assert len(dados['medias_acumuladas']) == 3
        assert len(dados['trajetorias']) == 3
    
    def test_experimento_2_sementes_corretas(self):
        """Testa se usa as sementes especificadas"""
        sementes = [10, 2026, 123456]
        dados = experimento_2(sementes=sementes)
        
        assert dados['sementes'] == sementes
        for semente in sementes:
            assert semente in dados['sequencias']
            assert semente in dados['medias_acumuladas']
            assert semente in dados['trajetorias']
    
    def test_experimento_2_numero_rodadas_correto(self):
        """Testa se cada sequência tem o número correto de rodadas"""
        n = 10000
        dados = experimento_2(n=n)
        
        for semente in dados['sementes']:
            assert len(dados['sequencias'][semente]) == n
            assert len(dados['trajetorias'][semente]) == n
    
    def test_experimento_2_pontos_acumulacao_corretos(self):
        """Testa se calcula médias nos pontos especificados"""
        pontos = [100, 1000, 10000]
        dados = experimento_2(pontos_acumulacao=pontos)
        
        for semente in dados['sementes']:
            for ponto in pontos:
                assert ponto in dados['medias_acumuladas'][semente]
    
    def test_experimento_2_reutiliza_experimento_1(self):
        """Testa se reutiliza corretamente a sequência do Experimento 1"""
        dados = experimento_2(sementes=[2026])
        
        assert dados['reutilizou_experimento_1'] == True
    
    def test_experimento_2_nao_reutiliza_outras_sementes(self):
        """Testa que não marca reutilização para outras sementes"""
        dados = experimento_2(sementes=[10, 123456])
        
        # Não deve reutilizar se 2026 não está nas sementes
        assert dados['reutilizou_experimento_1'] == False
    
    def test_experimento_2_esperanca_teorica_correta(self):
        """Testa se armazena a esperança teórica correta"""
        dados = experimento_2()
        esperanca_calculada = calcular_esperanca_lucro()
        
        assert abs(dados['esperanca_teorica'] - esperanca_calculada) < 1e-10
        assert abs(dados['esperanca_teorica'] - (-0.16)) < 1e-10


class TestConvergenciaExperimento2:
    """Testes de convergência para Lei dos Grandes Números"""
    
    def test_medias_acumuladas_convergem(self):
        """Testa se as médias acumuladas se aproximam da esperança"""
        dados = experimento_2(n=10000)
        
        for semente in dados['sementes']:
            # A diferença pode aumentar ou diminuir entre marcos devido à flutuação amostral
            # Testamos que pelo menos em um dos intervalos há redução OU que a diferença
            # final está dentro de um limite razoável
            diff_100 = abs(dados['medias_acumuladas'][semente][100] - dados['esperanca_teorica'])
            diff_1000 = abs(dados['medias_acumuladas'][semente][1000] - dados['esperanca_teorica'])
            diff_10000 = abs(dados['medias_acumuladas'][semente][10000] - dados['esperanca_teorica'])
            
            # Pelo menos uma das transições deve mostrar redução OU a diferença final deve ser razoável
            reducao_1 = diff_1000 < diff_100
            reducao_2 = diff_10000 < diff_1000
            final_razoavel = diff_10000 < 0.1  # Diferença < 0.1 com 10.000 rodadas
            
            assert reducao_1 or reducao_2 or final_razoavel, \
                f"Esperava convergência para semente {semente}: diffs={diff_100:.4f}, {diff_1000:.4f}, {diff_10000:.4f}"
    
    def test_media_final_proxima_da_esperanca(self):
        """Testa se a média final está próxima da esperança teórica"""
        dados = experimento_2(n=10000)
        
        for semente in dados['sementes']:
            media_final = dados['medias_acumuladas'][semente][10000]
            diff = abs(media_final - dados['esperanca_teorica'])
            
            # Com 10.000 rodadas, esperamos diferença < 0.1 (10% de 1.6)
            assert diff < 0.1, f"Média final {media_final} muito distante de {dados['esperanca_teorica']}"
    
    def test_trajetorias_tem_comprimento_correto(self):
        """Testa se as trajetórias têm o tamanho correto"""
        n = 5000
        dados = experimento_2(n=n)
        
        for semente in dados['sementes']:
            assert len(dados['trajetorias'][semente]) == n
    
    def test_trajetoria_valores_dentro_limite(self):
        """Testa se valores das trajetórias estão em range razoável"""
        dados = experimento_2(n=10000)
        
        for semente in dados['sementes']:
            trajetoria = dados['trajetorias'][semente]
            
            # Valores devem estar entre -1 (perda máxima) e 49 (ganho máximo)
            for media in trajetoria:
                assert -1 <= media <= 49


class TestReprodutibilidadeExperimento2:
    """Testes de reprodutibilidade"""
    
    def test_mesma_semente_mesmos_resultados(self):
        """Testa se a mesma semente produz os mesmos resultados"""
        dados1 = experimento_2(sementes=[42], n=1000)
        dados2 = experimento_2(sementes=[42], n=1000)
        
        seq1 = dados1['sequencias'][42]
        seq2 = dados2['sequencias'][42]
        
        assert seq1 == seq2
    
    def test_sementes_diferentes_resultados_diferentes(self):
        """Testa se sementes diferentes produzem resultados diferentes"""
        dados = experimento_2(sementes=[10, 20], n=1000)
        
        seq1 = dados['sequencias'][10]
        seq2 = dados['sequencias'][20]
        
        assert seq1 != seq2
    
    def test_reutilizacao_semente_2026_consistente(self):
        """Testa se reutilização da semente 2026 é consistente"""
        dados1 = experimento_2(sementes=[2026], n=10000)
        dados2 = experimento_2(sementes=[2026], n=10000)
        
        # Deve reutilizar do cache
        assert dados1['sequencias'][2026] == dados2['sequencias'][2026]
    
    def test_semente_2026_reproduz_experimento_1(self):
        """Testa se os primeiros 10 resultados da semente 2026 são idênticos no Exp1 e Exp2"""
        from src.experimentos import obter_resultados_experimento_1
        
        # Obter resultados do Experimento 1
        dados_exp1 = obter_resultados_experimento_1()
        primeiros_10_exp1 = [r['lucro'] for r in dados_exp1['resultados'][:10]]
        
        # Obter resultados do Experimento 2 com semente 2026
        dados_exp2 = experimento_2(sementes=[2026], n=10000)
        primeiros_10_exp2 = dados_exp2['sequencias'][2026][:10]
        
        # Devem ser idênticos
        assert primeiros_10_exp1 == primeiros_10_exp2, \
            f"Os 10 primeiros resultados diferem:\nExp1: {primeiros_10_exp1}\nExp2: {primeiros_10_exp2}"


class TestInterpretacaoExperimento2:
    """Testes de interpretação"""
    
    def test_interpretar_retorna_string(self):
        """Testa se a interpretação retorna uma string"""
        dados = experimento_2(n=1000)
        interpretacao = interpretar_experimento_2(dados)
        
        assert isinstance(interpretacao, str)
        assert len(interpretacao) > 0
    
    def test_interpretacao_menciona_lgn(self):
        """Testa se a interpretação menciona Lei dos Grandes Números"""
        dados = experimento_2(n=1000)
        interpretacao = interpretar_experimento_2(dados)
        
        assert 'Lei dos Grandes Números' in interpretacao or 'LGN' in interpretacao
    
    def test_interpretacao_menciona_convergencia(self):
        """Testa se a interpretação menciona convergência"""
        dados = experimento_2(n=1000)
        interpretacao = interpretar_experimento_2(dados)
        
        assert 'converg' in interpretacao.lower()
    
    def test_interpretacao_menciona_esperanca(self):
        """Testa se a interpretação menciona a esperança teórica"""
        dados = experimento_2(n=1000)
        interpretacao = interpretar_experimento_2(dados)
        
        assert 'esperança' in interpretacao.lower() or 'E[X]' in interpretacao


class TestCasosLimiteExperimento2:
    """Testes de casos limite"""
    
    def test_experimento_2_n_minimo(self):
        """Testa com número mínimo de rodadas"""
        dados = experimento_2(sementes=[10], n=10, pontos_acumulacao=[10])
        
        assert len(dados['sequencias'][10]) == 10
        assert 10 in dados['medias_acumuladas'][10]
    
    def test_experimento_2_ponto_acumulacao_maior_que_n(self):
        """Testa quando ponto de acumulação é maior que n"""
        dados = experimento_2(sementes=[10], n=100, pontos_acumulacao=[1000])
        
        # Não deve calcular média para ponto inexistente
        assert 1000 not in dados['medias_acumuladas'][10]
    
    def test_experimento_2_uma_sequencia(self):
        """Testa com apenas uma sequência"""
        dados = experimento_2(sementes=[999], n=1000)
        
        assert len(dados['sementes']) == 1
        assert 999 in dados['sequencias']
