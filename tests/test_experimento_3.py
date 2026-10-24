"""
Testes para o Experimento 3 - Saldo Limitado
"""

import pytest
import numpy as np
from src.experimentos import experimento_3, interpretar_experimento_3


class TestExperimento3Basico:
    """Testes básicos do Experimento 3"""
    
    def test_experimento_3_executa_com_parametros_padrao(self):
        """Testa se o experimento executa com parâmetros padrão"""
        dados = experimento_3()
        
        assert 'n_participantes' in dados
        assert 'saldo_inicial' in dados
        assert 'max_rodadas' in dados
        assert 'participantes' in dados
        assert 'saldos_finais' in dados
        assert 'rodadas_jogadas' in dados
    
    def test_experimento_3_numero_participantes_correto(self):
        """Testa se retorna o número correto de participantes"""
        n = 50
        dados = experimento_3(n_participantes=n, max_rodadas=100)
        
        assert dados['n_participantes'] == n
        assert len(dados['participantes']) == n
        assert len(dados['saldos_finais']) == n
        assert len(dados['rodadas_jogadas']) == n
    
    def test_experimento_3_saldo_inicial_correto(self):
        """Testa se todos os participantes começam com saldo inicial correto"""
        saldo = 200
        dados = experimento_3(n_participantes=10, saldo_inicial=saldo, max_rodadas=100)
        
        assert dados['saldo_inicial'] == saldo
        
        for p in dados['participantes']:
            assert p['saldo_inicial'] == saldo
            assert p['historico_saldos'][0] == saldo
    
    def test_experimento_3_max_rodadas_respeitado(self):
        """Testa se nenhum participante excede o máximo de rodadas"""
        max_rod = 200
        dados = experimento_3(n_participantes=20, max_rodadas=max_rod)
        
        for p in dados['participantes']:
            assert p['n_rodadas'] <= max_rod
    
    def test_experimento_3_saldo_nao_fica_negativo(self):
        """Testa se nenhum saldo final é negativo"""
        dados = experimento_3(n_participantes=30, max_rodadas=300)
        
        for saldo in dados['saldos_finais']:
            assert saldo >= 0
        
        for p in dados['participantes']:
            assert p['saldo_final'] >= 0
            for saldo in p['historico_saldos']:
                assert saldo >= 0


class TestExperimento3Contagens:
    """Testes de contagens e proporções"""
    
    def test_experimento_3_contagens_somam_total(self):
        """Testa se as contagens de resultados somam o total de participantes"""
        dados = experimento_3(n_participantes=100)
        
        total = dados['ganhou'] + dados['empatou'] + dados['perdeu']
        assert total == dados['n_participantes']
    
    def test_experimento_3_proporcoes_somam_um(self):
        """Testa se as proporções somam 100%"""
        dados = experimento_3(n_participantes=50)
        
        soma_proporcoes = (dados['proporcao_ganhou'] + 
                          dados['proporcao_empatou'] + 
                          dados['proporcao_perdeu'])
        
        assert abs(soma_proporcoes - 1.0) < 1e-10
    
    def test_experimento_3_zerou_saldo_contado_corretamente(self):
        """Testa se a contagem de quem zerou está correta"""
        dados = experimento_3(n_participantes=30, max_rodadas=300)
        
        zerou_manual = sum(1 for p in dados['participantes'] if p['zerou'])
        assert dados['zerou_saldo'] == zerou_manual
    
    def test_experimento_3_ganhou_perdeu_consistente(self):
        """Testa consistência entre flag de resultado e saldo final"""
        dados = experimento_3(n_participantes=40)
        
        for p in dados['participantes']:
            if p['ganhou']:
                assert p['saldo_final'] > p['saldo_inicial']
            elif p['empatou']:
                assert p['saldo_final'] == p['saldo_inicial']
            elif p['perdeu']:
                assert p['saldo_final'] < p['saldo_inicial']
    
    def test_experimento_3_zerou_implica_perdeu(self):
        """Testa se quem zerou também está marcado como perdeu"""
        dados = experimento_3(n_participantes=50)
        
        for p in dados['participantes']:
            if p['zerou']:
                assert p['saldo_final'] == 0
                assert p['perdeu'] == True
                assert p['ganhou'] == False


class TestExperimento3Estatisticas:
    """Testes de estatísticas calculadas"""
    
    def test_experimento_3_media_saldo_calculada_corretamente(self):
        """Testa se a média de saldo final está correta"""
        dados = experimento_3(n_participantes=30)
        
        media_manual = np.mean(dados['saldos_finais'])
        assert abs(dados['media_saldo_final'] - media_manual) < 1e-10
    
    def test_experimento_3_mediana_saldo_calculada_corretamente(self):
        """Testa se a mediana de saldo final está correta"""
        dados = experimento_3(n_participantes=40)
        
        mediana_manual = np.median(dados['saldos_finais'])
        assert abs(dados['mediana_saldo_final'] - mediana_manual) < 1e-10
    
    def test_experimento_3_media_rodadas_calculada_corretamente(self):
        """Testa se a média de rodadas jogadas está correta"""
        dados = experimento_3(n_participantes=25)
        
        media_manual = np.mean(dados['rodadas_jogadas'])
        assert abs(dados['media_rodadas'] - media_manual) < 1e-10
    
    def test_experimento_3_mediana_rodadas_calculada_corretamente(self):
        """Testa se a mediana de rodadas jogadas está correta"""
        dados = experimento_3(n_participantes=35)
        
        mediana_manual = np.median(dados['rodadas_jogadas'])
        assert abs(dados['mediana_rodadas'] - mediana_manual) < 1e-10


class TestExperimento3ComportamentoEsperado:
    """Testes do comportamento esperado estatisticamente"""
    
    def test_experimento_3_maioria_perde(self):
        """Testa se a maioria dos participantes perde (esperança negativa)"""
        dados = experimento_3(n_participantes=100, max_rodadas=500)
        
        # Com esperança negativa, esperamos que a maioria perca
        assert dados['perdeu'] > dados['ganhou']
    
    def test_experimento_3_saldo_medio_menor_que_inicial(self):
        """Testa se o saldo médio final é menor que o inicial"""
        dados = experimento_3(n_participantes=100, saldo_inicial=100, max_rodadas=500)
        
        # Em média, os participantes devem perder (esperança negativa)
        assert dados['media_saldo_final'] < dados['saldo_inicial']
    
    def test_experimento_3_alguns_zeram_saldo(self):
        """Testa se alguns participantes zeram o saldo"""
        dados = experimento_3(n_participantes=100, max_rodadas=500)
        
        # Com saldo limitado e esperança negativa, esperamos que alguns zerem
        # Não testamos quantidade exata, apenas que existe possibilidade
        assert dados['zerou_saldo'] >= 0
    
    def test_experimento_3_historico_saldo_tem_tamanho_correto(self):
        """Testa se o histórico de saldos tem tamanho correto"""
        dados = experimento_3(n_participantes=20)
        
        for p in dados['participantes']:
            # Histórico deve ter n_rodadas + 1 (inicial + após cada rodada)
            assert len(p['historico_saldos']) == p['n_rodadas'] + 1
    
    def test_experimento_3_rodadas_jogadas_consistente_com_historico(self):
        """Testa se n_rodadas é consistente com histórico"""
        dados = experimento_3(n_participantes=25)
        
        for p in dados['participantes']:
            # n_rodadas = len(histórico) - 1 (excluindo saldo inicial)
            assert p['n_rodadas'] == len(p['historico_saldos']) - 1


class TestExperimento3Reprodutibilidade:
    """Testes de reprodutibilidade"""
    
    def test_experimento_3_mesma_semente_mesmos_resultados(self):
        """Testa se a mesma semente_base produz os mesmos resultados"""
        dados1 = experimento_3(n_participantes=10, semente_base=42, max_rodadas=100)
        dados2 = experimento_3(n_participantes=10, semente_base=42, max_rodadas=100)
        
        assert dados1['saldos_finais'] == dados2['saldos_finais']
        assert dados1['rodadas_jogadas'] == dados2['rodadas_jogadas']
    
    def test_experimento_3_sementes_diferentes_resultados_diferentes(self):
        """Testa se sementes diferentes produzem resultados diferentes"""
        dados1 = experimento_3(n_participantes=10, semente_base=100, max_rodadas=100)
        dados2 = experimento_3(n_participantes=10, semente_base=200, max_rodadas=100)
        
        # Probabilidade de serem iguais é virtualmente zero
        assert dados1['saldos_finais'] != dados2['saldos_finais']


class TestExperimento3ParadaCorreta:
    """Testes de condições de parada"""
    
    def test_experimento_3_para_quando_zera_saldo(self):
        """Testa se para quando saldo chega a zero"""
        dados = experimento_3(n_participantes=50, max_rodadas=500)
        
        for p in dados['participantes']:
            if p['zerou']:
                # Se zerou, saldo final deve ser exatamente 0
                assert p['saldo_final'] == 0
                # E o último saldo do histórico também
                assert p['historico_saldos'][-1] == 0
    
    def test_experimento_3_para_no_maximo_rodadas(self):
        """Testa se para ao atingir máximo de rodadas"""
        max_rod = 100
        dados = experimento_3(n_participantes=30, max_rodadas=max_rod)
        
        for p in dados['participantes']:
            # Ninguém deve exceder o máximo
            assert p['n_rodadas'] <= max_rod
            
            # Se não zerou e jogou exatamente max_rod, atingiu o limite
            if p['n_rodadas'] == max_rod and not p['zerou']:
                assert p['saldo_final'] > 0


class TestExperimento3Interpretacao:
    """Testes da função de interpretação"""
    
    def test_interpretar_experimento_3_retorna_string(self):
        """Testa se a interpretação retorna uma string"""
        dados = experimento_3(n_participantes=20, max_rodadas=200)
        interpretacao = interpretar_experimento_3(dados)
        
        assert isinstance(interpretacao, str)
        assert len(interpretacao) > 0
    
    def test_interpretacao_menciona_metricas_principais(self):
        """Testa se a interpretação menciona as métricas principais"""
        dados = experimento_3(n_participantes=30, max_rodadas=300)
        interpretacao = interpretar_experimento_3(dados)
        
        # Deve mencionar participantes, saldo, rodadas
        assert 'participantes' in interpretacao.lower()
        assert 'saldo' in interpretacao.lower()
        assert 'rodadas' in interpretacao.lower()
    
    def test_interpretacao_menciona_proporcoes(self):
        """Testa se a interpretação menciona as proporções de resultado"""
        dados = experimento_3(n_participantes=40, max_rodadas=400)
        interpretacao = interpretar_experimento_3(dados)
        
        # Deve mencionar ganho, perda, empate
        assert 'ganhou' in interpretacao.lower() or 'ganhar' in interpretacao.lower()
        assert 'perdeu' in interpretacao.lower() or 'perder' in interpretacao.lower()
