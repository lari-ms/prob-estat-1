# FASE 1 — MODELO MATEMÁTICO E FUNÇÕES BÁSICAS

**Data de conclusão:** [Data atual]  
**Status:** ✅ Concluída e validada  
**Aprovação:** Pendente

---

## 📋 RESUMO EXECUTIVO

A Fase 1 estabeleceu o núcleo matemático do simulador de rolos, implementando todas as regras do modelo definido no enunciado do trabalho. Todos os 47 testes automatizados passaram, e os valores teóricos foram validados com precisão de 10 casas decimais.

**Principais entregas:**
- Simulador funcional de rodadas
- Cálculos matemáticos validados (probabilidades, esperança, RTP)
- 47 testes automatizados (100% de sucesso)
- Reprodutibilidade garantida
- Estrutura de projeto organizada

---

## 🎯 OBJETIVOS DA FASE

### Objetivo principal
Implementar o modelo matemático da máquina de rolos com regras públicas e validar todos os cálculos teóricos de referência.

### Objetivos específicos
1. ✅ Implementar sorteio uniforme de paradas (0-4)
2. ✅ Implementar montagem circular das colunas
3. ✅ Implementar execução de rodadas completas
4. ✅ Implementar cálculo de prêmios e lucros
5. ✅ Validar valores teóricos (E[P], E[X], RTP)
6. ✅ Garantir reprodutibilidade via controle de semente
7. ✅ Criar testes automatizados abrangentes

---

## 🏗️ ARQUITETURA IMPLEMENTADA

### Estrutura de arquivos criada

```
trabProb1/
├── src/
│   ├── __init__.py          # Metadados do pacote
│   ├── maquina.py           # Núcleo: sorteio, rolos, rodadas (237 linhas)
│   └── calculos.py          # Cálculos matemáticos (229 linhas)
├── tests/
│   ├── __init__.py
│   ├── test_maquina.py      # 24 testes do núcleo (330 linhas)
│   └── test_calculos.py     # 23 testes matemáticos (258 linhas)
├── docs/
│   └── FASE_1_DOCUMENTACAO.md  # Este arquivo
├── demo_fase1.py            # Demonstração funcional
├── verificar_reproducao.py  # Verificação de reprodutibilidade
├── requirements.txt         # Dependências
└── .gitignore              # Configuração Git
```

### Módulos implementados

#### **src/maquina.py**
Responsável pelo núcleo do simulador.

**Constantes:**
- `SIMBOLOS = ('A', 'B', 'C', 'D', 'E')`
- `TABELA_BASE` — Tabela de pagamentos original
- `TABELA_AUMENTADA_10PCT` — Tabela com pagamentos +10%

**Funções principais:**
- `sortear_parada(rng)` — Sorteia K uniformemente (0-4)
- `montar_coluna(parada)` — Monta coluna circular a partir de K
- `obter_linha_central(colunas)` — Extrai tripla central
- `calcular_premio(linha_central, tabela)` — Retorna prêmio bruto P
- `calcular_lucro(premio)` — Retorna lucro X = P - 1
- `executar_rodada(rng, tabela)` — Executa uma rodada completa
- `executar_rodadas(n, semente, tabela)` — Executa n rodadas

#### **src/calculos.py**
Responsável pelos cálculos teóricos.

**Funções principais:**
- `calcular_probabilidades_teoricas(tabela)` — Distribuição de P(X=x)
- `calcular_esperanca_premio(tabela)` — E[P]
- `calcular_esperanca_lucro(tabela)` — E[X] = E[P] - 1
- `calcular_rtp_teorico(tabela)` — RTP = E[P] / aposta
- `calcular_probabilidade_premio(tabela)` — P(prêmio > 0)
- `obter_valores_teoricos_referencia(tabela)` — Todos os valores
- `validar_valores_teoricos_tabela_base()` — Validação automática
- `validar_valores_teoricos_tabela_aumentada()` — Validação automática

---

## 🧮 MODELO MATEMÁTICO IMPLEMENTADO

### Regras do modelo

#### Símbolos e rolos
- **5 símbolos:** A, B, C, D, E
- **Sequência circular:** R = (A, B, C, D, E) em posições 0-4
- **3 rolos independentes:** Cada um sorteado separadamente

#### Sorteio e montagem
Para cada rolo:
1. Sortear parada K uniformemente: P(K=k) = 1/5 para k ∈ {0,1,2,3,4}
2. Montar coluna:
   - Topo: R[K]
   - Centro: R[(K+1) mod 5]
   - Base: R[(K+2) mod 5]

**Exemplo:** K=4 → Coluna = (E, A, B)

#### Avaliação e pagamento
- Apenas a **linha central** é avaliada
- Pagamento ocorre quando os **3 símbolos centrais são iguais**
- Aposta fixa: **1 crédito** por rodada
- Lucro: **X = P - 1** (onde P é o prêmio bruto)

### Tabelas de pagamento

#### Tabela Base

| Combinação Central | Prêmio (P) | Lucro (X) | Probabilidade |
|-------------------|-----------|-----------|---------------|
| A-A-A | 5 | 4 | 1/125 |
| B-B-B | 10 | 9 | 1/125 |
| C-C-C | 15 | 14 | 1/125 |
| D-D-D | 25 | 24 | 1/125 |
| E-E-E | 50 | 49 | 1/125 |
| Outras 120 | 0 | -1 | 120/125 |

#### Tabela Aumentada (+10%)

| Combinação | Prêmio (P) | Lucro (X) | Probabilidade |
|-----------|-----------|-----------|---------------|
| A-A-A | 5.5 | 4.5 | 1/125 |
| B-B-B | 11.0 | 10.0 | 1/125 |
| C-C-C | 16.5 | 15.5 | 1/125 |
| D-D-D | 27.5 | 26.5 | 1/125 |
| E-E-E | 55.0 | 54.0 | 1/125 |
| Outras 120 | 0 | -1 | 120/125 |

### Valores teóricos validados

#### Tabela Base

| Métrica | Fórmula | Valor | Status |
|---------|---------|-------|--------|
| Espaço amostral | 5³ | 125 | ✅ |
| P(prêmio) | 5/125 | 0.04 (4%) | ✅ |
| P(sem prêmio) | 120/125 | 0.96 (96%) | ✅ |
| E[P] | Σ(p_i × P_i) | 0.84 | ✅ |
| E[X] | E[P] - 1 | -0.16 | ✅ |
| RTP | E[P] / aposta | 0.84 (84%) | ✅ |
| Vantagem operador | 1 - RTP | 0.16 (16%) | ✅ |

#### Tabela Aumentada

| Métrica | Valor | Status |
|---------|-------|--------|
| P(prêmio) | 0.04 (4%) — inalterada | ✅ |
| E[P] | 0.924 | ✅ |
| E[X] | -0.076 | ✅ |
| RTP | 0.924 (92.4%) | ✅ |

**Cálculo de E[P] para tabela base:**
```
E[P] = (1/125) × 5 + (1/125) × 10 + (1/125) × 15 + (1/125) × 25 + (1/125) × 50
     = (1/125) × (5 + 10 + 15 + 25 + 50)
     = (1/125) × 105
     = 0.84
```

---

## 🧪 TESTES AUTOMATIZADOS

### Resumo dos testes

| Módulo | Testes | Status | Cobertura |
|--------|--------|--------|-----------|
| test_maquina.py | 24 | ✅ 100% | Sorteio, montagem, execução, casos-limite |
| test_calculos.py | 23 | ✅ 100% | Probabilidades, esperanças, RTP, validações |
| **TOTAL** | **47** | **✅ 100%** | — |

**Tempo de execução:** 0.39s

### Detalhamento por categoria

#### test_maquina.py (24 testes)

**TestSortearParada (3 testes)**
- ✅ `test_sortear_parada_intervalo_valido` — Verifica K ∈ [0,4]
- ✅ `test_sortear_parada_reprodutibilidade` — Mesma semente = mesmos resultados
- ✅ `test_sortear_parada_distribuicao_uniforme` — Todos valores aparecem ~20%

**TestMontarColuna (3 testes)**
- ✅ `test_montar_coluna_casos_conhecidos` — K=4 → (E,A,B), K=0 → (A,B,C)
- ✅ `test_montar_coluna_circularidade` — Verifica mod 5 correto
- ✅ `test_montar_coluna_parada_invalida` — Lança exceção para K inválido

**TestObterLinhaCentral (2 testes)**
- ✅ `test_obter_linha_central_correto` — Extrai tripla central
- ✅ `test_obter_linha_central_numero_colunas_invalido` — Valida 3 colunas

**TestCalcularPremio (2 testes)**
- ✅ `test_calcular_premio_triplas_premiadas` — 5 triplas retornam prêmio correto
- ✅ `test_calcular_premio_sem_premio` — Outras retornam 0

**TestCalcularLucro (2 testes)**
- ✅ `test_calcular_lucro_com_premio` — X = P - 1
- ✅ `test_calcular_lucro_sem_premio` — P=0 → X=-1

**TestExecutarRodada (3 testes)**
- ✅ `test_executar_rodada_estrutura` — Dict tem todas as chaves
- ✅ `test_executar_rodada_consistencia` — Paradas → colunas → linha → prêmio
- ✅ `test_executar_rodada_reprodutibilidade` — Mesma semente = mesmo resultado

**TestExecutarRodadas (4 testes)**
- ✅ `test_executar_rodadas_quantidade` — Retorna n resultados
- ✅ `test_executar_rodadas_reprodutibilidade` — Sequências idênticas
- ✅ `test_executar_rodadas_numero_invalido` — Rejeita n ≤ 0
- ✅ `test_executar_rodadas_lucros_possiveis` — Apenas {-1, 4, 9, 14, 24, 49}

**TestCasosLimite (5 testes)**
- ✅ `test_todas_paradas_produzem_colunas_validas` — 5 paradas OK
- ✅ `test_todos_simbolos_aparecem_em_posicao_central` — A, B, C, D, E no centro
- ✅ `test_premio_nunca_negativo` — P ≥ 0 sempre
- ✅ `test_lucro_minimo_eh_menos_um` — min(X) = -1

#### test_calculos.py (23 testes)

**TestProbabilidadesTeoricas (5 testes)**
- ✅ `test_probabilidades_somam_um` — ΣP(X=x) = 1
- ✅ `test_seis_lucros_possiveis` — |{lucros}| = 6
- ✅ `test_lucros_corretos` — {-1, 4, 9, 14, 24, 49}
- ✅ `test_probabilidade_perda` — P(X=-1) = 120/125
- ✅ `test_probabilidade_cada_premio` — P(X>0) = 1/125 cada

**TestEsperancas (5 testes)**
- ✅ `test_esperanca_premio_tabela_base` — E[P] = 0.84
- ✅ `test_esperanca_lucro_tabela_base` — E[X] = -0.16
- ✅ `test_esperanca_premio_tabela_aumentada` — E[P] = 0.924
- ✅ `test_esperanca_lucro_tabela_aumentada` — E[X] = -0.076
- ✅ `test_relacao_esperanca_lucro_e_premio` — E[X] = E[P] - 1

**TestRTP (3 testes)**
- ✅ `test_rtp_tabela_base` — RTP = 0.84
- ✅ `test_rtp_tabela_aumentada` — RTP = 0.924
- ✅ `test_rtp_igual_esperanca_premio` — RTP = E[P]

**TestProbabilidadePremio (2 testes)**
- ✅ `test_probabilidade_premio_tabela_base` — P(prêmio) = 5/125
- ✅ `test_probabilidade_premio_tabela_aumentada_inalterada` — P(prêmio) = 5/125

**TestValoresReferencia (4 testes)**
- ✅ `test_valores_referencia_estrutura` — 9 chaves presentes
- ✅ `test_espaco_amostral` — 125 combinações
- ✅ `test_prob_premio_mais_prob_sem_premio` — Soma = 1
- ✅ `test_vantagem_operador` — 1 - RTP

**TestValidacoes (3 testes)**
- ✅ `test_validacao_tabela_base` — Todos valores corretos
- ✅ `test_validacao_tabela_aumentada` — Todos valores corretos
- ✅ `test_valores_diferentes_entre_tabelas` — RTP aumentada > base

**TestConsistenciaMatematica (2 testes)**
- ✅ `test_esperanca_via_distribuicao` — E[X] = Σx·P(X=x)
- ✅ `test_prob_premio_via_distribuicao` — P(prêmio) = Σ P(X>0)

---

## 🔄 REPRODUTIBILIDADE

### Configuração do ambiente

| Item | Valor |
|------|-------|
| Sistema operacional | Windows |
| Python | 3.12.7 |
| Gerador | `random.Random()` (stdlib) |
| Biblioteca | Módulo `random` padrão |

### Primeiros 10 resultados da semente 2026

Estes resultados devem ser **idênticos** em qualquer execução com a mesma configuração:

| Rodada | Paradas | Linha Central | Prêmio | Lucro |
|--------|---------|---------------|--------|-------|
| 1 | (0,2,4) | B-D-A | 0.0 | -1.0 |
| 2 | (4,0,1) | A-B-C | 0.0 | -1.0 |
| 3 | (4,4,4) | **A-A-A** | **5.0** | **4.0** |
| 4 | (3,4,4) | E-A-A | 0.0 | -1.0 |
| 5 | (3,4,3) | E-A-E | 0.0 | -1.0 |
| 6 | (1,0,4) | C-B-A | 0.0 | -1.0 |
| 7 | (0,0,2) | B-B-D | 0.0 | -1.0 |
| 8 | (0,3,0) | B-E-B | 0.0 | -1.0 |
| 9 | (3,2,1) | E-D-C | 0.0 | -1.0 |
| 10 | (3,2,2) | E-D-D | 0.0 | -1.0 |

**Média dos 10 primeiros:** -0.500 créditos  
**Prêmios:** 1 em 10 (10% — flutuação natural em amostra pequena)

### Como verificar

```bash
python verificar_reproducao.py
```

Execute múltiplas vezes e compare os resultados — devem ser idênticos.

---

## 📦 DEPENDÊNCIAS

### Bibliotecas instaladas

```
numpy==1.26.4         # Computação científica
pandas==2.1.4         # Manipulação de dados (para próximas fases)
matplotlib==3.8.2     # Visualização (para próximas fases)
pytest==7.4.3         # Framework de testes
```

### Instalação

```bash
pip install -r requirements.txt
```

---

## ✅ VALIDAÇÃO DA FASE

### Checklist de conformidade

- [x] Sorteio uniforme implementado e testado
- [x] Montagem circular validada (K=4 → E,A,B)
- [x] 3 rolos independentes confirmados
- [x] Linha central única avaliada
- [x] Tabelas de pagamento corretas
- [x] Cálculo de prêmio validado
- [x] Cálculo de lucro validado (X = P - 1)
- [x] Valores teóricos exatos (8/8)
- [x] 47 testes automatizados passando
- [x] Reprodutibilidade garantida
- [x] Semente controlada explicitamente
- [x] Documentação clara e organizada

### Comandos de validação

```bash
# Executar todos os testes
python -m pytest tests/ -v

# Demonstração funcional
python demo_fase1.py

# Verificar reprodutibilidade
python verificar_reproducao.py
```

---

## 📝 NOTAS PARA O RELATÓRIO

### Conceitos demonstrados nesta fase

1. **Espaço amostral:** 5³ = 125 combinações centrais equiprováveis
2. **Eventos:** 5 triplas premiadas, 120 sem prêmio
3. **Distribuição uniforme:** P(K=k) = 1/5 para cada parada
4. **Independência:** Os 3 rolos são sorteados independentemente
5. **Variável aleatória discreta:** X (lucro) com 6 valores possíveis
6. **Esperança matemática:** E[X] = -0.16 crédito por rodada
7. **Linearidade da esperança:** E[X] = E[P] - 1
8. **RTP (Return to Player):** 84% para tabela base

### Pontos importantes para discussão

**1. Diferença entre probabilidade de prêmio e RTP**
- P(prêmio) = 4% — chance de receber algo
- RTP = 84% — quanto dos créditos apostados retorna em média
- São conceitos diferentes! 4% não significa 4% de retorno

**2. Esperança negativa não impede ganhos ocasionais**
- Rodada 3 com semente 2026: lucro de +4
- Mas a esperança é -0.16 por rodada
- Ganhos individuais coexistem com perda esperada

**3. Aumentar pagamentos melhora RTP, mas não a chance**
- Tabela +10%: RTP sobe de 84% para 92.4%
- Mas P(prêmio) permanece 4%
- Pagar mais ≠ premiar com mais frequência

---

## 🔜 PRÓXIMOS PASSOS

### Preparação para Fase 2

A **Fase 2** implementará o **Experimento 1**:

**O que será feito:**
- Executar 10.000 rodadas com semente 2026
- Contar frequências dos 6 lucros possíveis
- Calcular estatísticas: média, RTP observado, desvio-padrão
- Gerar tabela CSV comparando teoria vs observação
- Criar gráfico de barras

**Arquivos a criar:**
- `src/experimentos.py`
- `src/visualizacao.py`
- `src/exportacao.py`
- `resultados/csvs/experimento1_frequencias.csv`
- `resultados/graficos/experimento1_frequencias.png`

**Reutilização:**
- Os resultados do E1 serão salvos para reutilização no E2, E4 e E5

---

## 📊 MÉTRICAS DA FASE

| Métrica | Valor |
|---------|-------|
| Arquivos Python criados | 8 |
| Linhas de código (src/) | 466 |
| Linhas de teste | 588 |
| Testes automatizados | 47 |
| Taxa de sucesso | 100% |
| Tempo de testes | 0.39s |
| Cobertura de funcionalidades | 100% |
| Valores teóricos validados | 8/8 |

---

## 🎓 APRENDIZADOS E OBSERVAÇÕES

### Decisões técnicas importantes

1. **Uso de `random.Random(seed)` em vez de `random.seed()`**
   - Permite múltiplos geradores independentes
   - Mais seguro para testes paralelos
   - Recomendação da documentação oficial

2. **Validação com tolerância de 1e-10**
   - Evita erros de arredondamento de ponto flutuante
   - Mantém precisão matemática rigorosa

3. **Testes abrangentes com casos-limite**
   - Não apenas "happy path"
   - Valida entradas inválidas, distribuições, consistência

### Lições para próximas fases

- ✅ Manter testes automatizados a cada implementação
- ✅ Documentar valores de referência antes de simular
- ✅ Separar claramente teoria (cálculos) de experimento (simulação)
- ✅ Usar nomes de função descritivos e consistentes

---

## 🏁 CONCLUSÃO DA FASE 1

A Fase 1 foi **concluída com sucesso**. O núcleo matemático do simulador está:
- ✅ Implementado corretamente
- ✅ Matematicamente validado
- ✅ Completamente testado
- ✅ Reproduzível
- ✅ Documentado

**Status:** Pronto para aprovação e início da Fase 2.

---

**Documento gerado automaticamente durante a implementação da Fase 1**  
**Trabalho I de Probabilidade e Estatística — IFES Campus Serra**
