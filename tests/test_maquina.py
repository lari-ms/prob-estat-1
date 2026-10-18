"""
Testes do módulo maquina.py
Valida o núcleo do simulador: sorteio, montagem e execução de rodadas.
"""

import pytest
import random
from src.maquina import (
    sortear_parada,
    montar_coluna,
    obter_linha_central,
    calcular_premio,
    calcular_lucro,
    executar_rodada,
    executar_rodadas,
    SIMBOLOS,
    TABELA_BASE
)


class TestSortearParada:
    """Testes da função sortear_parada"""
    
    def test_sortear_parada_intervalo_valido(self):
        """Verifica se a parada está no intervalo [0, 4]"""
        rng = random.Random(42)
        for _ in range(100):
            parada = sortear_parada(rng)
            assert 0 <= parada <= 4, f"Parada {parada} fora do intervalo [0, 4]"
    
    def test_sortear_parada_reprodutibilidade(self):
        """Verifica se a mesma semente produz a mesma sequência"""
        rng1 = random.Random(123)
        rng2 = random.Random(123)
        
        for _ in range(20):
            assert sortear_parada(rng1) == sortear_parada(rng2)
    
    def test_sortear_parada_distribuicao_uniforme(self):
        """Verifica se todos os valores aparecem em uma amostra grande"""
        rng = random.Random(2026)
        contagens = {i: 0 for i in range(5)}
        
        n_sorteios = 10000
        for _ in range(n_sorteios):
            parada = sortear_parada(rng)
            contagens[parada] += 1
        
        # Todos os valores devem aparecer
        for i in range(5):
            assert contagens[i] > 0, f"Valor {i} nunca foi sorteado"
        
        # Cada valor deve aparecer aproximadamente 20% das vezes
        for i in range(5):
            frequencia = contagens[i] / n_sorteios
            # Margem generosa para flutuação aleatória
            assert 0.15 < frequencia < 0.25, \
                f"Frequência de {i} = {frequencia:.3f}, esperado ~0.20"


class TestMontarColuna:
    """Testes da função montar_coluna"""
    
    def test_montar_coluna_casos_conhecidos(self):
        """Verifica casos explícitos do enunciado"""
        # Caso K=4: deve produzir (E, A, B)
        assert montar_coluna(4) == ('E', 'A', 'B')
        
        # Outros casos verificáveis
        assert montar_coluna(0) == ('A', 'B', 'C')
        assert montar_coluna(1) == ('B', 'C', 'D')
        assert montar_coluna(2) == ('C', 'D', 'E')
        assert montar_coluna(3) == ('D', 'E', 'A')
    
    def test_montar_coluna_circularidade(self):
        """Verifica se a sequência é realmente circular"""
        for k in range(5):
            topo, centro, base = montar_coluna(k)
            
            # Os três símbolos devem ser consecutivos na sequência circular
            idx_topo = SIMBOLOS.index(topo)
            idx_centro = SIMBOLOS.index(centro)
            idx_base = SIMBOLOS.index(base)
            
            assert idx_centro == (idx_topo + 1) % 5
            assert idx_base == (idx_topo + 2) % 5
    
    def test_montar_coluna_parada_invalida(self):
        """Verifica se lança exceção para parada inválida"""
        with pytest.raises(ValueError):
            montar_coluna(-1)
        
        with pytest.raises(ValueError):
            montar_coluna(5)
        
        with pytest.raises(ValueError):
            montar_coluna(100)


class TestObterLinhaCentral:
    """Testes da função obter_linha_central"""
    
    def test_obter_linha_central_correto(self):
        """Verifica extração da linha central"""
        colunas = [
            ('A', 'B', 'C'),
            ('B', 'D', 'E'),
            ('C', 'A', 'B')
        ]
        assert obter_linha_central(colunas) == ('B', 'D', 'A')
    
    def test_obter_linha_central_numero_colunas_invalido(self):
        """Verifica se lança exceção com número incorreto de colunas"""
        with pytest.raises(ValueError):
            obter_linha_central([('A', 'B', 'C')])
        
        with pytest.raises(ValueError):
            obter_linha_central([('A', 'B', 'C')] * 4)


class TestCalcularPremio:
    """Testes da função calcular_premio"""
    
    def test_calcular_premio_triplas_premiadas(self):
        """Verifica prêmios das cinco triplas premiadas"""
        assert calcular_premio(('A', 'A', 'A')) == 5
        assert calcular_premio(('B', 'B', 'B')) == 10
        assert calcular_premio(('C', 'C', 'C')) == 15
        assert calcular_premio(('D', 'D', 'D')) == 25
        assert calcular_premio(('E', 'E', 'E')) == 50
    
    def test_calcular_premio_sem_premio(self):
        """Verifica que outras combinações não pagam"""
        assert calcular_premio(('A', 'B', 'C')) == 0
        assert calcular_premio(('A', 'A', 'B')) == 0
        assert calcular_premio(('E', 'D', 'C')) == 0
        assert calcular_premio(('B', 'B', 'A')) == 0


class TestCalcularLucro:
    """Testes da função calcular_lucro"""
    
    def test_calcular_lucro_com_premio(self):
        """Verifica cálculo do lucro para prêmios"""
        assert calcular_lucro(5) == 4
        assert calcular_lucro(10) == 9
        assert calcular_lucro(15) == 14
        assert calcular_lucro(25) == 24
        assert calcular_lucro(50) == 49
    
    def test_calcular_lucro_sem_premio(self):
        """Verifica que sem prêmio o lucro é -1"""
        assert calcular_lucro(0) == -1


class TestExecutarRodada:
    """Testes da função executar_rodada"""
    
    def test_executar_rodada_estrutura(self):
        """Verifica se o resultado tem a estrutura esperada"""
        rng = random.Random(42)
        resultado = executar_rodada(rng)
        
        assert 'paradas' in resultado
        assert 'colunas' in resultado
        assert 'linha_central' in resultado
        assert 'premio' in resultado
        assert 'lucro' in resultado
        
        assert len(resultado['paradas']) == 3
        assert len(resultado['colunas']) == 3
        assert len(resultado['linha_central']) == 3
    
    def test_executar_rodada_consistencia(self):
        """Verifica consistência entre paradas, colunas e linha central"""
        rng = random.Random(2026)
        
        for _ in range(50):
            resultado = executar_rodada(rng)
            
            # Reconstruir colunas a partir das paradas
            paradas = resultado['paradas']
            colunas_esperadas = [montar_coluna(k) for k in paradas]
            
            assert resultado['colunas'] == colunas_esperadas
            
            # Verificar linha central
            linha_esperada = obter_linha_central(colunas_esperadas)
            assert resultado['linha_central'] == linha_esperada
            
            # Verificar prêmio e lucro
            premio_esperado = calcular_premio(linha_esperada)
            assert resultado['premio'] == premio_esperado
            assert resultado['lucro'] == premio_esperado - 1
    
    def test_executar_rodada_reprodutibilidade(self):
        """Verifica se mesma semente produz mesmo resultado"""
        rng1 = random.Random(123456)
        rng2 = random.Random(123456)
        
        for _ in range(10):
            r1 = executar_rodada(rng1)
            r2 = executar_rodada(rng2)
            
            assert r1['paradas'] == r2['paradas']
            assert r1['linha_central'] == r2['linha_central']
            assert r1['premio'] == r2['premio']
            assert r1['lucro'] == r2['lucro']


class TestExecutarRodadas:
    """Testes da função executar_rodadas"""
    
    def test_executar_rodadas_quantidade(self):
        """Verifica se executa o número correto de rodadas"""
        resultados = executar_rodadas(100, semente=42)
        assert len(resultados) == 100
        
        resultados = executar_rodadas(1000, semente=2026)
        assert len(resultados) == 1000
    
    def test_executar_rodadas_reprodutibilidade(self):
        """Verifica reprodutibilidade completa"""
        r1 = executar_rodadas(50, semente=999)
        r2 = executar_rodadas(50, semente=999)
        
        for i in range(50):
            assert r1[i]['paradas'] == r2[i]['paradas']
            assert r1[i]['linha_central'] == r2[i]['linha_central']
            assert r1[i]['premio'] == r2[i]['premio']
            assert r1[i]['lucro'] == r2[i]['lucro']
    
    def test_executar_rodadas_numero_invalido(self):
        """Verifica se lança exceção para número inválido de rodadas"""
        with pytest.raises(ValueError):
            executar_rodadas(0, semente=42)
        
        with pytest.raises(ValueError):
            executar_rodadas(-10, semente=42)
    
    def test_executar_rodadas_lucros_possiveis(self):
        """Verifica se aparecem apenas os lucros válidos"""
        resultados = executar_rodadas(1000, semente=2026)
        lucros_validos = {-1, 4, 9, 14, 24, 49}
        
        lucros_observados = {r['lucro'] for r in resultados}
        
        # Todos os lucros observados devem estar no conjunto válido
        assert lucros_observados.issubset(lucros_validos), \
            f"Lucros inválidos encontrados: {lucros_observados - lucros_validos}"


class TestCasosLimite:
    """Testes de casos limite e especiais"""
    
    def test_todas_paradas_produzem_colunas_validas(self):
        """Verifica que todas as 5 paradas produzem colunas válidas"""
        for k in range(5):
            coluna = montar_coluna(k)
            assert len(coluna) == 3
            assert all(s in SIMBOLOS for s in coluna)
    
    def test_todos_simbolos_aparecem_em_posicao_central(self):
        """Verifica que todos os símbolos podem aparecer no centro"""
        simbolos_centrais = set()
        
        for k in range(5):
            _, centro, _ = montar_coluna(k)
            simbolos_centrais.add(centro)
        
        assert simbolos_centrais == set(SIMBOLOS), \
            "Nem todos os símbolos aparecem na posição central"
    
    def test_premio_nunca_negativo(self):
        """Verifica que prêmio nunca é negativo"""
        rng = random.Random(12345)
        
        for _ in range(500):
            resultado = executar_rodada(rng)
            assert resultado['premio'] >= 0, \
                f"Prêmio negativo: {resultado['premio']}"
    
    def test_lucro_minimo_eh_menos_um(self):
        """Verifica que o lucro mínimo é -1 (sem prêmio)"""
        rng = random.Random(777)
        
        lucro_minimo = float('inf')
        for _ in range(1000):
            resultado = executar_rodada(rng)
            lucro_minimo = min(lucro_minimo, resultado['lucro'])
        
        assert lucro_minimo == -1, \
            f"Lucro mínimo observado: {lucro_minimo}, esperado -1"
