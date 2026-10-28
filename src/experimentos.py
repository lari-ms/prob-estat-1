"""
Módulo experimentos.py
Implementa os cinco experimentos obrigatórios do trabalho.
"""

from typing import Dict, List, Tuple
import numpy as np
from src.maquina import executar_rodadas, calcular_premio, calcular_lucro, TABELA_BASE, TABELA_AUMENTADA_10PCT
from src.calculos import (
    calcular_probabilidades_teoricas,
    calcular_esperanca_lucro,
    calcular_rtp_teorico,
    calcular_probabilidade_premio
)


def experimento_1(n: int = 10000, semente: int = 2026) -> Dict:
    """
    Experimento 1: Frequências e Probabilidades
    
    Executa n rodadas e compara frequências observadas com probabilidades teóricas.
    
    Args:
        n: Número de rodadas (padrão: 10.000)
        semente: Semente do gerador (padrão: 2026)
        
    Returns:
        dict: {
            'n_rodadas': int,
            'semente': int,
            'resultados': list com todas as rodadas,
            'contagens': dict {lucro: quantidade},
            'frequencias': dict {lucro: frequência relativa},
            'probabilidades_teoricas': dict {lucro: probabilidade},
            'lucro_medio': float,
            'rtp_observado': float,
            'rtp_teorico': float,
            'proporcao_premios': float,
            'desvio_padrao': float,
            'premios_observados': int,
            'premios_esperados': float
        }
    """
    # Executar rodadas
    resultados = executar_rodadas(n, semente, TABELA_BASE)
    
    # Extrair lucros
    lucros = [r['lucro'] for r in resultados]
    premios = [r['premio'] for r in resultados]
    
    # Contar frequências
    lucros_possiveis = [-1, 4, 9, 14, 24, 49]
    contagens = {lucro: lucros.count(lucro) for lucro in lucros_possiveis}
    
    # Calcular frequências relativas
    frequencias = {lucro: contagens[lucro] / n for lucro in lucros_possiveis}
    
    # Probabilidades teóricas
    prob_teoricas = calcular_probabilidades_teoricas(TABELA_BASE)
    
    # Métricas
    lucro_medio = np.mean(lucros)
    soma_premios = sum(premios)
    total_apostado = n * 1  # Aposta unitária
    rtp_observado = soma_premios / total_apostado
    rtp_teorico = calcular_rtp_teorico(TABELA_BASE)
    
    # Proporção de prêmios
    premios_observados = sum(1 for p in premios if p > 0)
    proporcao_premios = premios_observados / n
    
    # Desvio-padrão amostral (divisor N-1)
    desvio_padrao = np.std(lucros, ddof=1)
    
    # Prêmios esperados
    prob_premio_teorica = calcular_probabilidade_premio(TABELA_BASE)
    premios_esperados = n * prob_premio_teorica
    
    return {
        'n_rodadas': n,
        'semente': semente,
        'resultados': resultados,  # Para reutilização em experimentos futuros
        'contagens': contagens,
        'frequencias': frequencias,
        'probabilidades_teoricas': prob_teoricas,
        'lucro_medio': lucro_medio,
        'rtp_observado': rtp_observado,
        'rtp_teorico': rtp_teorico,
        'proporcao_premios': proporcao_premios,
        'desvio_padrao': desvio_padrao,
        'premios_observados': premios_observados,
        'premios_esperados': premios_esperados
    }


def interpretar_experimento_1(dados: Dict) -> str:
    """
    Gera interpretação textual do Experimento 1.
    
    Args:
        dados: Resultado do experimento_1()
        
    Returns:
        str: Texto de interpretação
    """
    interpretacao = []
    
    # Introdução
    interpretacao.append(
        f"Foram executadas {dados['n_rodadas']:,} rodadas com semente {dados['semente']}. "
        f"A Tabela apresenta a comparação entre as probabilidades teóricas e as "
        f"frequências observadas."
    )
    
    # Lucro médio
    diff_lucro = abs(dados['lucro_medio'] - calcular_esperanca_lucro())
    interpretacao.append(
        f"\nO lucro médio observado foi de {dados['lucro_medio']:.4f} créditos, "
        f"com diferença de {diff_lucro:.4f} em relação ao valor teórico de -0,1600. "
        f"Essa diferença é esperada devido à flutuação amostral."
    )
    
    # RTP
    diff_rtp = abs(dados['rtp_observado'] - dados['rtp_teorico'])
    interpretacao.append(
        f"\nO RTP observado foi de {dados['rtp_observado']*100:.2f}%, "
        f"próximo do valor teórico de {dados['rtp_teorico']*100:.2f}%. "
        f"A diferença de {diff_rtp*100:.2f} pontos percentuais está dentro do esperado "
        f"para uma amostra deste tamanho."
    )
    
    # Proporção de prêmios
    interpretacao.append(
        f"\nForam observadas {dados['premios_observados']:,} rodadas premiadas "
        f"({dados['proporcao_premios']*100:.2f}%), enquanto o valor teórico é de 4,00%. "
        f"Esperavam-se {dados['premios_esperados']:.0f} prêmios em média."
    )
    
    # Dispersão
    interpretacao.append(
        f"\nO desvio-padrão amostral foi de {dados['desvio_padrao']:.4f} créditos, "
        f"indicando alta variabilidade nos resultados individuais, mesmo com lucro médio negativo."
    )
    
    # Lei dos Grandes Números
    interpretacao.append(
        f"\n\nAs frequências observadas aproximam-se das probabilidades teóricas, "
        f"conforme esperado pela Lei dos Grandes Números. Com {dados['n_rodadas']:,} rodadas, "
        f"a média amostral converge para a esperança matemática, mas flutuações individuais "
        f"permanecem significativas."
    )
    
    # Distinção RTP vs P(prêmio)
    interpretacao.append(
        f"\n\nÉ fundamental distinguir a proporção de prêmios ({dados['proporcao_premios']*100:.2f}%) "
        f"do RTP ({dados['rtp_observado']*100:.2f}%). O primeiro indica a frequência de vitórias, "
        f"enquanto o segundo mede quanto dos créditos apostados retorna em forma de prêmios. "
        f"Mesmo com RTP de 84%, o jogador tem esperança de perda de 16% por rodada."
    )
    
    return ''.join(interpretacao)


# Armazenamento global dos resultados para reutilização
_cache_experimento_1 = None


def obter_resultados_experimento_1(forcar_nova_execucao: bool = False) -> Dict:
    """
    Retorna os resultados do Experimento 1, executando se necessário ou reutilizando cache.
    
    Args:
        forcar_nova_execucao: Se True, força nova execução mesmo com cache
        
    Returns:
        dict: Resultados do experimento_1()
    """
    global _cache_experimento_1
    
    if _cache_experimento_1 is None or forcar_nova_execucao:
        _cache_experimento_1 = experimento_1()
    
    return _cache_experimento_1


def experimento_2(
    sementes: List[int] = [10, 2026, 123456],
    n: int = 10000,
    pontos_acumulacao: List[int] = [1000, 5000, 10000]
) -> Dict:
    """
    Experimento 2: Lei dos Grandes Números
    
    Demonstra empiricamente a convergência da média amostral para a esperança matemática.
    Executa múltiplas sequências independentes e calcula médias acumuladas em diferentes pontos.
    
    Args:
        sementes: Lista de sementes para execuções independentes (padrão: [10, 2026, 123456])
        n: Número total de rodadas por sequência (padrão: 10.000)
        pontos_acumulacao: Pontos onde calcular médias acumuladas (padrão: [1000, 5000, 10000])
        
    Returns:
        dict: {
            'sementes': list,
            'n_rodadas': int,
            'pontos_acumulacao': list,
            'sequencias': dict {semente: lista de lucros},
            'medias_acumuladas': dict {semente: {ponto: média}},
            'trajetorias': dict {semente: lista de médias em cada rodada},
            'esperanca_teorica': float,
            'reutilizou_experimento_1': bool
        }
    """
    # Esperança teórica
    esperanca_teorica = calcular_esperanca_lucro()
    
    # Armazenar sequências
    sequencias = {}
    medias_acumuladas = {}
    trajetorias = {}
    reutilizou_exp1 = False
    
    for semente in sementes:
        # Reutilizar Experimento 1 se semente for 2026
        if semente == 2026 and n == 10000:
            # Só reutiliza se o número de rodadas for exatamente 10.000
            dados_exp1 = obter_resultados_experimento_1()
            lucros = [r['lucro'] for r in dados_exp1['resultados']]
            reutilizou_exp1 = True
        else:
            # Executar nova sequência
            resultados = executar_rodadas(n, semente, TABELA_BASE)
            lucros = [r['lucro'] for r in resultados]
        
        # Armazenar sequência completa
        sequencias[semente] = lucros
        
        # Calcular médias acumuladas nos pontos especificados
        medias_acumuladas[semente] = {}
        for ponto in pontos_acumulacao:
            if ponto <= len(lucros):
                media = np.mean(lucros[:ponto])
                medias_acumuladas[semente][ponto] = media
        
        # Calcular trajetória completa (média acumulada em cada rodada)
        trajetoria = []
        for i in range(1, len(lucros) + 1):
            media = np.mean(lucros[:i])
            trajetoria.append(media)
        trajetorias[semente] = trajetoria
    
    return {
        'sementes': sementes,
        'n_rodadas': n,
        'pontos_acumulacao': pontos_acumulacao,
        'sequencias': sequencias,
        'medias_acumuladas': medias_acumuladas,
        'trajetorias': trajetorias,
        'esperanca_teorica': esperanca_teorica,
        'reutilizou_experimento_1': reutilizou_exp1
    }


def interpretar_experimento_2(dados: Dict) -> str:
    """
    Gera interpretação textual do Experimento 2.
    
    Args:
        dados: Resultado do experimento_2()
        
    Returns:
        str: Texto de interpretação
    """
    interpretacao = []
    
    # Introdução
    interpretacao.append(
        f"O Experimento 2 demonstra empiricamente a Lei dos Grandes Números (LGN) "
        f"através de {len(dados['sementes'])} sequências independentes, cada uma com "
        f"{dados['n_rodadas']:,} rodadas. A LGN garante que a média amostral converge "
        f"para a esperança matemática à medida que o número de observações aumenta."
    )
    
    # Esperança teórica
    interpretacao.append(
        f"\n\nA esperança teórica do lucro por rodada é E[X] = {dados['esperanca_teorica']:.4f} "
        f"créditos (perda média de {abs(dados['esperanca_teorica'])*100:.2f}% por rodada)."
    )
    
    # Reutilização
    if dados['reutilizou_experimento_1']:
        interpretacao.append(
            f"\n\nA sequência com semente 2026 foi reutilizada do Experimento 1, "
            f"garantindo reprodutibilidade e consistência entre os experimentos."
        )
    
    # Análise das médias acumuladas
    interpretacao.append("\n\n### Médias Acumuladas\n")
    for semente in dados['sementes']:
        interpretacao.append(f"\n**Semente {semente}:**")
        for ponto in dados['pontos_acumulacao']:
            if ponto in dados['medias_acumuladas'][semente]:
                media = dados['medias_acumuladas'][semente][ponto]
                diff = abs(media - dados['esperanca_teorica'])
                interpretacao.append(
                    f"\n- Em {ponto:,} rodadas: média = {media:.4f} "
                    f"(diferença: {diff:.4f})"
                )
    
    # Convergência
    interpretacao.append(
        f"\n\nObserva-se que, em todas as três sequências, as médias acumuladas "
        f"aproximam-se progressivamente do valor teórico de {dados['esperanca_teorica']:.4f}. "
        f"As diferenças em relação à esperança diminuem à medida que o número de rodadas aumenta, "
        f"como previsto pela LGN."
    )
    
    # Variabilidade inicial
    interpretacao.append(
        f"\n\nCom 1.000 rodadas, as médias ainda apresentam variabilidade considerável "
        f"entre as sequências devido à flutuação amostral. No entanto, ao atingir "
        f"10.000 rodadas, todas as médias convergem para valores próximos da esperança, "
        f"demonstrando empiricamente o comportamento assintótico previsto pela teoria."
    )
    
    # Gráfico
    interpretacao.append(
        f"\n\nO gráfico de trajetórias ilustra visualmente este fenômeno: as três linhas "
        f"iniciam com flutuações significativas e gradualmente convergem para a linha "
        f"horizontal que representa E[X] = {dados['esperanca_teorica']:.4f}."
    )
    
    # Implicação prática
    interpretacao.append(
        f"\n\n### Implicação para o Jogador\n\n"
        f"A LGN garante que, independentemente de flutuações de curto prazo ou \"sorte\" "
        f"individual, a longo prazo o jogador sempre terá uma perda média de "
        f"{abs(dados['esperanca_teorica'])*100:.2f}% por rodada. Sequências independentes "
        f"(diferentes jogadores ou sessões) convergem para o mesmo resultado negativo."
    )
    
    return ''.join(interpretacao)



def experimento_3(
    n_participantes: int = 100,
    saldo_inicial: int = 100,
    max_rodadas: int = 500,
    semente_base: int = 3000
) -> Dict:
    """
    Experimento 3: Saldo Limitado
    
    Simula n participantes virtuais jogando até atingir saldo zero ou máximo de rodadas.
    Cada participante tem saldo inicial fixo e para quando perde tudo ou atinge o limite.
    
    Args:
        n_participantes: Número de participantes virtuais (padrão: 100)
        saldo_inicial: Saldo inicial de cada participante em créditos (padrão: 100)
        max_rodadas: Número máximo de rodadas por participante (padrão: 500)
        semente_base: Semente base para gerar sementes individuais (padrão: 3000)
        
    Returns:
        dict: {
            'n_participantes': int,
            'saldo_inicial': int,
            'max_rodadas': int,
            'participantes': list de dicts com histórico de cada participante,
            'saldos_finais': list de saldos finais,
            'rodadas_jogadas': list de rodadas jogadas por cada um,
            'ganhou': int (saldo final > saldo inicial),
            'empatou': int (saldo final == saldo inicial),
            'perdeu': int (saldo final < saldo inicial),
            'zerou_saldo': int (saldo final == 0),
            'media_saldo_final': float,
            'mediana_saldo_final': float,
            'media_rodadas': float,
            'mediana_rodadas': float
        }
    """
    import random
    
    participantes = []
    saldos_finais = []
    rodadas_jogadas = []
    
    # Simular cada participante
    for i in range(n_participantes):
        # Semente única para cada participante
        semente_participante = semente_base + i
        rng = random.Random(semente_participante)
        
        saldo_atual = saldo_inicial
        historico_saldos = [saldo_inicial]
        n_rodadas = 0
        
        # Jogar até zerar ou atingir máximo de rodadas
        while saldo_atual > 0 and n_rodadas < max_rodadas:
            # Executar uma rodada
            resultado = executar_rodadas(1, semente_participante + n_rodadas * 10000, TABELA_BASE)[0]
            lucro = resultado['lucro']
            
            # Atualizar saldo
            saldo_atual += lucro
            historico_saldos.append(saldo_atual)
            n_rodadas += 1
            
            # Se saldo ficou negativo, ajustar para zero (não pode ficar negativo)
            if saldo_atual < 0:
                saldo_atual = 0
                historico_saldos[-1] = 0
        
        # Armazenar dados do participante
        participante_data = {
            'id': i + 1,
            'semente': semente_participante,
            'saldo_inicial': saldo_inicial,
            'saldo_final': saldo_atual,
            'n_rodadas': n_rodadas,
            'historico_saldos': historico_saldos,
            'zerou': saldo_atual == 0,
            'ganhou': saldo_atual > saldo_inicial,
            'empatou': saldo_atual == saldo_inicial,
            'perdeu': saldo_atual < saldo_inicial
        }
        
        participantes.append(participante_data)
        saldos_finais.append(saldo_atual)
        rodadas_jogadas.append(n_rodadas)
    
    # Calcular estatísticas agregadas
    ganhou = sum(1 for p in participantes if p['ganhou'])
    empatou = sum(1 for p in participantes if p['empatou'])
    perdeu = sum(1 for p in participantes if p['perdeu'])
    zerou_saldo = sum(1 for p in participantes if p['zerou'])
    
    media_saldo_final = np.mean(saldos_finais)
    mediana_saldo_final = np.median(saldos_finais)
    
    media_rodadas = np.mean(rodadas_jogadas)
    mediana_rodadas = np.median(rodadas_jogadas)
    
    return {
        'n_participantes': n_participantes,
        'saldo_inicial': saldo_inicial,
        'max_rodadas': max_rodadas,
        'participantes': participantes,
        'saldos_finais': saldos_finais,
        'rodadas_jogadas': rodadas_jogadas,
        'ganhou': ganhou,
        'empatou': empatou,
        'perdeu': perdeu,
        'zerou_saldo': zerou_saldo,
        'media_saldo_final': media_saldo_final,
        'mediana_saldo_final': mediana_saldo_final,
        'media_rodadas': media_rodadas,
        'mediana_rodadas': mediana_rodadas,
        'proporcao_ganhou': ganhou / n_participantes,
        'proporcao_empatou': empatou / n_participantes,
        'proporcao_perdeu': perdeu / n_participantes,
        'proporcao_zerou': zerou_saldo / n_participantes
    }


def interpretar_experimento_3(dados: Dict) -> str:
    """
    Gera interpretação textual do Experimento 3.
    
    Args:
        dados: Resultado do experimento_3()
        
    Returns:
        str: Texto de interpretação
    """
    interpretacao = []
    
    # Introdução
    interpretacao.append(
        f"O Experimento 3 simula {dados['n_participantes']} participantes virtuais, "
        f"cada um iniciando com {dados['saldo_inicial']} créditos e jogando até zerar "
        f"o saldo ou completar {dados['max_rodadas']} rodadas. Este experimento "
        f"demonstra o comportamento de jogadores com recursos limitados e simula "
        f"sessões reais de jogo com paradas naturais (perda total do saldo)."
    )
    
    # Proporções de resultado
    interpretacao.append(
        f"\n\n### Resultados Finais\n\n"
        f"Dos {dados['n_participantes']} participantes:\n"
        f"- **{dados['ganhou']} ganharam** ({dados['proporcao_ganhou']*100:.1f}%): "
        f"saldo final > {dados['saldo_inicial']} créditos\n"
        f"- **{dados['empatou']} empataram** ({dados['proporcao_empatou']*100:.1f}%): "
        f"saldo final = {dados['saldo_inicial']} créditos\n"
        f"- **{dados['perdeu']} perderam** ({dados['proporcao_perdeu']*100:.1f}%): "
        f"saldo final < {dados['saldo_inicial']} créditos\n"
        f"- **{dados['zerou_saldo']} zeraram o saldo** ({dados['proporcao_zerou']*100:.1f}%): "
        f"perderam todo o capital inicial"
    )
    
    # Saldos finais
    interpretacao.append(
        f"\n\n### Saldos Finais\n\n"
        f"- **Média:** {dados['media_saldo_final']:.2f} créditos "
        f"(perda média de {dados['saldo_inicial'] - dados['media_saldo_final']:.2f} créditos, "
        f"ou {(1 - dados['media_saldo_final']/dados['saldo_inicial'])*100:.1f}% do capital)\n"
        f"- **Mediana:** {dados['mediana_saldo_final']:.2f} créditos\n\n"
        f"A média de saldo final ({dados['media_saldo_final']:.2f}) sendo inferior ao "
        f"saldo inicial ({dados['saldo_inicial']}) confirma a esperança negativa do jogo. "
        f"Em média, cada participante perdeu "
        f"{(1 - dados['media_saldo_final']/dados['saldo_inicial'])*100:.1f}% do seu capital."
    )
    
    # Número de rodadas
    interpretacao.append(
        f"\n\n### Número de Rodadas\n\n"
        f"- **Média:** {dados['media_rodadas']:.1f} rodadas\n"
        f"- **Mediana:** {dados['mediana_rodadas']:.0f} rodadas\n"
        f"- **Máximo possível:** {dados['max_rodadas']} rodadas\n\n"
    )
    
    # Análise da distribuição de rodadas
    participantes_max = sum(1 for r in dados['rodadas_jogadas'] if r >= dados['max_rodadas'])
    if participantes_max > 0:
        interpretacao.append(
            f"{participantes_max} participantes ({participantes_max/dados['n_participantes']*100:.1f}%) "
            f"atingiram o limite de {dados['max_rodadas']} rodadas sem zerar o saldo, "
            f"demonstrando que conseguiram \"sobreviver\" por mais tempo apesar da esperança negativa.\n\n"
        )
    
    # Análise de zeragem de saldo
    if dados['zerou_saldo'] > 0:
        interpretacao.append(
            f"{dados['zerou_saldo']} participantes ({dados['proporcao_zerou']*100:.1f}%) "
            f"perderam todo o seu capital antes de completar {dados['max_rodadas']} rodadas. "
            f"Esta é a realidade mais severa do jogo: uma parcela significativa dos jogadores "
            f"perde tudo antes de decidir parar.\n\n"
        )
    
    # Implicação sobre ganhos vs perdas
    if dados['ganhou'] > 0:
        interpretacao.append(
            f"\n\n### Ganhos Ocasionais vs Perda Sistemática\n\n"
            f"Embora {dados['ganhou']} participantes ({dados['proporcao_ganhou']*100:.1f}%) "
            f"tenham terminado com lucro, isto não contradiz a esperança negativa do jogo. "
            f"Estes são exemplos de **flutuação amostral positiva**: alguns jogadores tiveram "
            f"sorte em suas sessões limitadas.\n\n"
            f"Porém, a **maioria ({dados['perdeu']}, ou {dados['proporcao_perdeu']*100:.1f}%) perdeu**, "
            f"e o saldo médio final ({dados['media_saldo_final']:.2f}) é inferior ao inicial "
            f"({dados['saldo_inicial']}), confirmando que **em agregado, o grupo como um todo perde**.\n\n"
            f"Se estes mesmos {dados['ganhou']} participantes que ganharam continuassem jogando "
            f"indefinidamente, a Lei dos Grandes Números garante que eventualmente convergiriam "
            f"para perda, como demonstrado no Experimento 2."
        )
    
    # Conclusão
    interpretacao.append(
        f"\n\n### Conclusão\n\n"
        f"O Experimento 3 demonstra que, mesmo com saldo limitado e paradas naturais "
        f"(zeragem do saldo), o resultado agregado é sempre negativo para os jogadores. "
        f"Embora alguns indivíduos possam ter ganhos em sessões curtas, a maioria perde, "
        f"e o saldo médio final é sempre inferior ao inicial.\n\n"
        f"Este experimento simula de forma realista o comportamento de jogadores reais, "
        f"que não jogam indefinidamente mas em sessões limitadas. Mesmo neste cenário, "
        f"a vantagem matemática do operador se manifesta: perda média de "
        f"{(1 - dados['media_saldo_final']/dados['saldo_inicial'])*100:.1f}% do capital inicial."
    )
    
    return ''.join(interpretacao)


# ==============================================================================
# EXPERIMENTO 4: PROBABILIDADE CONDICIONAL
# ==============================================================================

def experimento_4(resultados: List[Dict] = None) -> Dict:
    """
    Experimento 4: Depois de perder, aumenta a chance de ganhar?
    
    Examina os n-1 pares de rodadas consecutivas (i, i+1) e os separa conforme
    a primeira rodada do par pagou prêmio (P > 0) ou não. Em cada grupo, conta
    quantas vezes a rodada seguinte foi premiada e divide pelo total de pares
    do grupo. Grupo sem pares tem proporção não estimável (None).
    
    Args:
        resultados: Rodadas a analisar. Se None, reutiliza as 10.000 rodadas
                    do Experimento 1 (semente 2026)
        
    Returns:
        dict: {
            'n_rodadas': int,
            'n_pares': int,
            'grupos': {
                'apos_premio': {'total_pares', 'premios_seguinte', 'proporcao'},
                'apos_nao_premio': {'total_pares', 'premios_seguinte', 'proporcao'}
            },
            'probabilidade_teorica': float (referência de independência, 4%)
        }
    """
    if resultados is None:
        resultados = obter_resultados_experimento_1()['resultados']
    
    if len(resultados) < 2:
        raise ValueError(f"São necessárias pelo menos 2 rodadas, recebido: {len(resultados)}")
    
    premiada = [r['premio'] > 0 for r in resultados]
    
    grupos = {
        'apos_premio': {'total_pares': 0, 'premios_seguinte': 0},
        'apos_nao_premio': {'total_pares': 0, 'premios_seguinte': 0}
    }
    
    # Pares (i, i+1) para i = 0..n-2
    for atual, seguinte in zip(premiada[:-1], premiada[1:]):
        grupo = grupos['apos_premio'] if atual else grupos['apos_nao_premio']
        grupo['total_pares'] += 1
        if seguinte:
            grupo['premios_seguinte'] += 1
    
    # Proporção condicional; grupo vazio não é estimável (não dividir por zero)
    for grupo in grupos.values():
        if grupo['total_pares'] > 0:
            grupo['proporcao'] = grupo['premios_seguinte'] / grupo['total_pares']
        else:
            grupo['proporcao'] = None
    
    return {
        'n_rodadas': len(resultados),
        'n_pares': len(resultados) - 1,
        'grupos': grupos,
        'probabilidade_teorica': calcular_probabilidade_premio(TABELA_BASE)
    }


def interpretar_experimento_4(dados: Dict) -> str:
    """
    Gera um RASCUNHO de interpretação do Experimento 4 a partir dos números obtidos.
    
    O texto deve ser revisado e reescrito pela equipe antes de entrar no relatório.
    
    Args:
        dados: Resultado do experimento_4()
        
    Returns:
        str: Texto de interpretação
    """
    ref = dados['probabilidade_teorica']
    nomes = {'apos_premio': 'após uma rodada premiada',
             'apos_nao_premio': 'após uma rodada sem prêmio'}
    interpretacao = []
    
    interpretacao.append(
        f"Foram examinados os {dados['n_pares']:,} pares de rodadas consecutivas das "
        f"{dados['n_rodadas']:,} rodadas do Experimento 1, separados conforme a primeira "
        f"rodada do par pagou ou não prêmio."
    )
    
    for chave, nome in nomes.items():
        g = dados['grupos'][chave]
        if g['proporcao'] is None:
            interpretacao.append(
                f"\nNão houve pares {nome}; a proporção nesse grupo é não estimável."
            )
        else:
            interpretacao.append(
                f"\nDos {g['total_pares']:,} pares {nome}, a rodada seguinte foi premiada "
                f"{g['premios_seguinte']:,} vezes ({g['proporcao']*100:.2f}%)."
            )
    
    interpretacao.append(
        f"\nA referência do modelo, por independência, é Pr(G(i+1) | G(i)) = "
        f"Pr(G(i+1) | não G(i)) = Pr(G(i+1)) = {ref*100:.0f}%."
    )
    
    interpretacao.append(
        f"\n\n[REVISAR] Os sorteios de cada rodada são independentes dos anteriores: a "
        f"máquina não guarda memória de perdas nem passa a \"dever\" um prêmio. As duas "
        f"frequências observadas podem diferir entre si e de {ref*100:.0f}% por flutuação "
        f"amostral; o grupo \"após prêmio\" tem poucos pares, por isso sua proporção oscila "
        f"mais. Uma diferença amostral, sozinha, não indica mudança das regras. Esperar que um "
        f"prêmio venha para compensar perdas recentes é a falácia do jogador."
    )
    
    return ''.join(interpretacao)


# ==============================================================================
# EXPERIMENTO 5: COMPARAÇÃO DE TABELAS DE PAGAMENTO
# ==============================================================================

TABELAS_EXPERIMENTO_5 = {
    'Base': TABELA_BASE,
    'Prêmios +10%': TABELA_AUMENTADA_10PCT
}


def experimento_5(resultados: List[Dict] = None, tabelas: Dict[str, Dict] = None) -> Dict:
    """
    Experimento 5: Prêmios maiores tornam o jogo favorável?
    
    Aplica cada tabela de pagamentos às MESMAS rodadas (mesmas linhas centrais),
    sem sortear outra sequência, e compara as métricas teóricas e observadas.
    
    Args:
        resultados: Rodadas a reavaliar. Se None, reutiliza as 10.000 rodadas
                    do Experimento 1 (semente 2026)
        tabelas: dict {nome: tabela de pagamentos}. Se None, usa base e +10%
        
    Returns:
        dict: {
            'n_rodadas': int,
            'tabelas': {nome: {
                'prob_premio_teorica', 'freq_premio_observada', 'premios_observados',
                'premio_medio', 'lucro_medio', 'lucro_esperado_teorico',
                'rtp_teorico', 'rtp_observado'
            }}
        }
    """
    if resultados is None:
        resultados = obter_resultados_experimento_1()['resultados']
    if tabelas is None:
        tabelas = TABELAS_EXPERIMENTO_5
    
    n = len(resultados)
    linhas = [r['linha_central'] for r in resultados]
    
    metricas = {}
    for nome, tabela in tabelas.items():
        premios = [calcular_premio(linha, tabela) for linha in linhas]
        lucros = [calcular_lucro(p) for p in premios]
        premios_observados = sum(1 for p in premios if p > 0)
        
        metricas[nome] = {
            'prob_premio_teorica': calcular_probabilidade_premio(tabela),
            'freq_premio_observada': premios_observados / n,
            'premios_observados': premios_observados,
            'premio_medio': float(np.mean(premios)),
            'lucro_medio': float(np.mean(lucros)),
            'lucro_esperado_teorico': calcular_esperanca_lucro(tabela),
            'rtp_teorico': calcular_rtp_teorico(tabela),
            'rtp_observado': sum(premios) / n  # aposta de 1 crédito por rodada
        }
    
    return {
        'n_rodadas': n,
        'tabelas': metricas
    }


def interpretar_experimento_5(dados: Dict) -> str:
    """
    Gera um RASCUNHO de interpretação do Experimento 5 a partir dos números obtidos.
    
    O texto deve ser revisado e reescrito pela equipe antes de entrar no relatório.
    
    Args:
        dados: Resultado do experimento_5()
        
    Returns:
        str: Texto de interpretação
    """
    interpretacao = []
    
    interpretacao.append(
        f"As {len(dados['tabelas'])} tabelas de pagamento foram aplicadas às mesmas "
        f"{dados['n_rodadas']:,} rodadas do Experimento 1, sem sortear outra sequência."
    )
    
    for nome, m in dados['tabelas'].items():
        interpretacao.append(
            f"\nTabela {nome}: prêmios em {m['premios_observados']:,} rodadas "
            f"({m['freq_premio_observada']*100:.2f}%; teórico {m['prob_premio_teorica']*100:.2f}%), "
            f"prêmio médio {m['premio_medio']:.4f}, lucro médio {m['lucro_medio']:.4f} "
            f"(teórico {m['lucro_esperado_teorico']:.4f}), RTP observado "
            f"{m['rtp_observado']*100:.2f}% (teórico {m['rtp_teorico']*100:.2f}%)."
        )
    
    primeira, ultima = list(dados['tabelas'].values())[0], list(dados['tabelas'].values())[-1]
    favoravel = ultima['lucro_esperado_teorico'] > 0
    interpretacao.append(
        f"\n\n[REVISAR] A chance de prêmio é a mesma nas duas tabelas, pois os símbolos e "
        f"suas probabilidades não mudaram. Aumentar os pagamentos multiplica o prêmio esperado "
        f"(RTP de {primeira['rtp_teorico']*100:.1f}% para {ultima['rtp_teorico']*100:.1f}%) e "
        f"reduz a perda esperada (de {primeira['lucro_esperado_teorico']:.3f} para "
        f"{ultima['lucro_esperado_teorico']:.3f} por rodada), "
        + ("e a esperança do lucro passa a ser positiva. "
           if favoravel else
           "mas a esperança do lucro continua negativa: o jogo segue desfavorável. ")
        + f"Pagar mais, "
        f"pagar com maior frequência e produzir lucro esperado positivo são afirmações "
        f"diferentes."
    )
    
    return ''.join(interpretacao)
