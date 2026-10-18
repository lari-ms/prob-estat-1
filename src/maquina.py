"""
Módulo maquina.py
Implementa o núcleo do simulador de rolos: sorteio, montagem e execução de rodadas.
"""

from typing import Tuple, Dict, List
import random


# Constantes do modelo
SIMBOLOS = ('A', 'B', 'C', 'D', 'E')
POSICOES_ROLO = 5  # 0, 1, 2, 3, 4

# Tabelas de pagamento
TABELA_BASE = {
    ('A', 'A', 'A'): 5,
    ('B', 'B', 'B'): 10,
    ('C', 'C', 'C'): 15,
    ('D', 'D', 'D'): 25,
    ('E', 'E', 'E'): 50,
}

TABELA_AUMENTADA_10PCT = {
    ('A', 'A', 'A'): 5.5,
    ('B', 'B', 'B'): 11.0,
    ('C', 'C', 'C'): 16.5,
    ('D', 'D', 'D'): 27.5,
    ('E', 'E', 'E'): 55.0,
}


def sortear_parada(rng: random.Random) -> int:
    """
    Sorteia uniformemente uma posição de parada do rolo.
    
    Args:
        rng: Gerador pseudoaleatório Random
        
    Returns:
        int: Posição de parada K (0, 1, 2, 3 ou 4)
    """
    return rng.randint(0, 4)


def montar_coluna(parada: int) -> Tuple[str, str, str]:
    """
    Monta uma coluna do tabuleiro a partir da posição de parada.
    
    A sequência circular dos rolos é R = (A, B, C, D, E).
    Para uma parada K, a coluna mostra:
    - Topo: R[K]
    - Centro: R[(K+1) mod 5]
    - Base: R[(K+2) mod 5]
    
    Exemplo: K=4 → (E, A, B)
    
    Args:
        parada: Posição de parada K (0-4)
        
    Returns:
        tuple: (topo, centro, base) com os três símbolos
    """
    if not 0 <= parada < POSICOES_ROLO:
        raise ValueError(f"Parada deve estar entre 0 e 4, recebido: {parada}")
    
    topo = SIMBOLOS[parada]
    centro = SIMBOLOS[(parada + 1) % POSICOES_ROLO]
    base = SIMBOLOS[(parada + 2) % POSICOES_ROLO]
    
    return (topo, centro, base)


def obter_linha_central(colunas: List[Tuple[str, str, str]]) -> Tuple[str, str, str]:
    """
    Extrai a linha central do tabuleiro (única linha avaliada para pagamento).
    
    Args:
        colunas: Lista de 3 colunas, cada uma com (topo, centro, base)
        
    Returns:
        tuple: Tripla com os três símbolos centrais
    """
    if len(colunas) != 3:
        raise ValueError(f"Esperadas 3 colunas, recebido: {len(colunas)}")
    
    return (colunas[0][1], colunas[1][1], colunas[2][1])


def calcular_premio(linha_central: Tuple[str, str, str], tabela: Dict = None) -> float:
    """
    Calcula o prêmio bruto P para a linha central.
    
    Args:
        linha_central: Tripla de símbolos da linha central
        tabela: Dicionário de pagamentos. Se None, usa TABELA_BASE
        
    Returns:
        float: Prêmio bruto (0 se não houver combinação premiada)
    """
    if tabela is None:
        tabela = TABELA_BASE
    
    return tabela.get(linha_central, 0)


def calcular_lucro(premio: float) -> float:
    """
    Calcula o lucro líquido do jogador: X = P - 1
    
    A aposta fixa é de 1 crédito.
    
    Args:
        premio: Prêmio bruto P
        
    Returns:
        float: Lucro líquido X
    """
    return premio - 1


def executar_rodada(rng: random.Random, tabela: Dict = None) -> Dict:
    """
    Executa uma rodada completa da máquina de rolos.
    
    Processo:
    1. Sorteia três paradas independentes (uma por rolo)
    2. Monta as três colunas
    3. Extrai a linha central
    4. Calcula prêmio e lucro
    
    Args:
        rng: Gerador pseudoaleatório Random
        tabela: Tabela de pagamentos. Se None, usa TABELA_BASE
        
    Returns:
        dict: {
            'paradas': (K1, K2, K3),
            'colunas': [(topo1, centro1, base1), ...],
            'linha_central': (símbolo1, símbolo2, símbolo3),
            'premio': float,
            'lucro': float
        }
    """
    # Sorteia três paradas independentes
    paradas = tuple(sortear_parada(rng) for _ in range(3))
    
    # Monta as três colunas
    colunas = [montar_coluna(k) for k in paradas]
    
    # Extrai linha central
    linha_central = obter_linha_central(colunas)
    
    # Calcula prêmio e lucro
    premio = calcular_premio(linha_central, tabela)
    lucro = calcular_lucro(premio)
    
    return {
        'paradas': paradas,
        'colunas': colunas,
        'linha_central': linha_central,
        'premio': premio,
        'lucro': lucro
    }


def executar_rodadas(n: int, semente: int, tabela: Dict = None) -> List[Dict]:
    """
    Executa n rodadas com semente especificada.
    
    Args:
        n: Número de rodadas
        semente: Semente para inicializar o gerador
        tabela: Tabela de pagamentos. Se None, usa TABELA_BASE
        
    Returns:
        list: Lista com os resultados de cada rodada
    """
    if n <= 0:
        raise ValueError(f"Número de rodadas deve ser positivo, recebido: {n}")
    
    rng = random.Random(semente)
    resultados = []
    
    for _ in range(n):
        resultado = executar_rodada(rng, tabela)
        resultados.append(resultado)
    
    return resultados
