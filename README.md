# Trabalho I - Probabilidade e Estatística

**Repositório:** https://github.com/lari-ms/prob-estat-1  
**Instituição:** IFES Campus Serra — Bacharelado em Sistemas de Informação  
**Disciplina:** Probabilidade e Estatística I  
**Período:** Outubro de 2026

---

## 👥 Integrantes

- Larissa Motta Soares
- Lucas Carvalho Flores

---

## 📋 Objetivo do Projeto

Desenvolver um simulador computacional de máquina de caça-níqueis para fins exclusivamente acadêmicos, demonstrando empiricamente conceitos fundamentais de probabilidade e estatística através de cinco experimentos computacionais.

O projeto valida conceitos como:
- Esperança matemática e Return to Player (RTP)
- Lei dos Grandes Números
- Distribuição de probabilidades discretas
- Probabilidade condicional e independência
- Análise comparativa de tabelas de pagamento

---

## 🎰 Modelo Matemático

### Regras da Máquina

**Estrutura:** 3 rolos × 5 símbolos (A, B, C, D, E)  
**Espaço amostral:** 5 × 5 × 5 = 125 combinações possíveis  
**Custo por rodada:** 1 crédito  
**Linha avaliada:** Linha central única

### Símbolos e Premiações (Tabela Base)

| Combinação | Prêmio | Lucro (Prêmio - Custo) | Probabilidade |
|------------|--------|------------------------|---------------|
| A-A-A | 5 créditos | +4 créditos | 1/125 (0,8%) |
| B-B-B | 10 créditos | +9 créditos | 1/125 (0,8%) |
| C-C-C | 15 créditos | +14 créditos | 1/125 (0,8%) |
| D-D-D | 25 créditos | +24 créditos | 1/125 (0,8%) |
| E-E-E | 50 créditos | +49 créditos | 1/125 (0,8%) |
| Outras 120 | 0 créditos | -1 crédito | 120/125 (96%) |

### Valores Teóricos

**Esperança matemática (E[X]):**
```
E[X] = (1/125) × (4 + 9 + 14 + 24 + 49) + (120/125) × (-1)
E[X] = (1/125) × 100 - (120/125)
E[X] = 0,8 - 0,96 = -0,16 créditos por rodada
```

**Return to Player (RTP):**
```
RTP = (Prêmio médio esperado) / (Custo por rodada)
RTP = 0,84 / 1 = 0,84 = 84%
```

**Probabilidade de prêmio:**
```
P(prêmio) = 5/125 = 0,04 = 4%
```

---

## 📁 Estrutura do Repositório

```
prob-estat-1/
├── src/                              # Código-fonte
│   ├── maquina.py                    # Simulador de rodadas
│   ├── calculos.py                   # Cálculos teóricos
│   ├── experimentos.py               # Experimentos 1-5
│   ├── extras.py                     # Itens extras
│   ├── visualizacao.py               # Geração de gráficos
│   └── exportacao.py                 # Exportação de CSVs
│
├── tests/                            # Testes automatizados (140 testes)
│   ├── test_maquina.py               # 24 testes do simulador
│   ├── test_calculos.py              # 24 testes dos cálculos
│   ├── test_experimento_1.py         # 17 testes
│   ├── test_experimento_2.py         # 23 testes
│   ├── test_experimento_3.py         # 28 testes
│   ├── test_experimento_4.py         # 9 testes
│   ├── test_experimento_5.py         # 9 testes
│   └── test_validacao.py             # 6 testes dos extras
│
├── docs/                             # Documentação
│   ├── RELATORIO_TRABALHO_I.docx     # Relatório final para entrega
│   ├── FASE_1_DOCUMENTACAO.md        # Documentação do modelo matemático
│   ├── FASE_2_DOCUMENTACAO.md        # Documentação do Experimento 1
│   ├── FASE_3_DOCUMENTACAO.md        # Documentação do Experimento 2
│   ├── FASE_4_DOCUMENTACAO.md        # Documentação dos Experimentos 3, 4 e 5
│   ├── APENDICE_A_NOVOS_EXTRAS.md    # Documentação dos itens extras
│   └── EXTRAS_EDUCACAO_CIENTIFICA.html  # Item extra: educação científica
│
├── resultados/                       # Resultados dos experimentos
│   ├── csvs/                         # 12 CSVs (6 experimentos + 6 extras)
│   ├── graficos/                     # 6 gráficos PNG
│   ├── experimento_1_interpretacao.txt
│   ├── experimento_2_interpretacao.txt
│   ├── experimento_3_interpretacao.txt
│   ├── experimento_4_interpretacao.txt
│   └── experimento_5_interpretacao.txt
│
├── executar_experimento_1.py         # Script do Experimento 1
├── executar_experimento_2.py         # Script do Experimento 2
├── executar_experimento_3.py         # Script do Experimento 3
├── executar_experimento_4.py         # Script do Experimento 4
├── executar_experimento_5.py         # Script do Experimento 5
├── executar_todos_extras.py          # Script dos itens extras
├── extra_auditoria.py                # Extra: auditoria de alegações públicas
├── requirements.txt                  # Dependências do projeto
└── README.md                         # Este arquivo
```

---

## 🔧 Requisitos e Instalação

### Pré-requisitos

- **Python:** 3.12 ou superior
- **Sistema Operacional:** Windows, Linux ou macOS
- **pip:** Gerenciador de pacotes Python

### Dependências

```bash
pip install -r requirements.txt
```

**Pacotes necessários:**
- `numpy==1.26.4` - Operações numéricas e geração de números aleatórios
- `pandas==2.1.4` - Manipulação de dados e exportação de CSVs
- `matplotlib==3.8.2` - Geração de gráficos
- `pytest==7.4.3` - Framework de testes automatizados

---

## 🚀 Execução dos Experimentos

### Experimento 1: Frequências e Probabilidades

**Objetivo:** Validar empiricamente as probabilidades teóricas através de 10.000 rodadas.

```bash
python executar_experimento_1.py
```

**Parâmetros:**
- Rodadas: 10.000
- Semente: 2026
- Resultado esperado: Frequências observadas convergem para probabilidades teóricas

---

### Experimento 2: Lei dos Grandes Números

**Objetivo:** Demonstrar convergência da média amostral para E[X] = -0,16.

```bash
python executar_experimento_2.py
```

**Parâmetros:**
- 3 sequências independentes de 10.000 rodadas cada
- Sementes: 10, 2026 (reutilizada do Exp 1), 123456
- Marcos de avaliação: 100, 1.000, 10.000 rodadas

---

### Experimento 3: Saldo Limitado (100 Participantes)

**Objetivo:** Simular comportamento realista com saldo inicial limitado.

```bash
python executar_experimento_3.py
```

**Parâmetros:**
- Participantes: 100
- Saldo inicial: 100 créditos
- Máximo de rodadas: 500
- Semente: 42

---

### Experimento 4: Probabilidade Condicional

**Objetivo:** Validar independência entre rodadas consecutivas.

```bash
python executar_experimento_4.py
```

**Parâmetros:**
- Reutiliza as 10.000 rodadas do Experimento 1 (semente 2026)
- Analisa pares consecutivos

---

### Experimento 5: Comparação de Tabelas de Pagamento

**Objetivo:** Comparar o impacto de diferentes tabelas no RTP.

```bash
python executar_experimento_5.py
```

**Parâmetros:**
- Tabela Base: RTP 84%
- Tabela Aumentada (+10%): RTP 92,4%

---

## 🧪 Execução dos Testes

### Executar todos os testes

```bash
python -m pytest tests/ -v
```

**Resultado esperado:**
```
================= 140 passed, 3 warnings in XX.XXs ==================
```

### Executar testes específicos

```bash
# Experimento 1
python -m pytest tests/test_experimento_1.py -v

# Todos os testes do núcleo
python -m pytest tests/test_maquina.py tests/test_calculos.py -v
```

---

## 🎯 Itens Extras Implementados

O projeto implementa **4 itens extras**, totalizando **17 pontos**:

### 1. Validação Automatizada (3 pontos) ✅

140 testes automatizados validando todas as funcionalidades.

**Executar:**
```bash
python -m pytest tests/ -v
```

### 2. Intervalos de Confiança (5 pontos) ✅

Cálculo de intervalos de confiança usando métodos Clopper-Pearson, Wilson e Bootstrap.

**Executar:**
```bash
python executar_todos_extras.py
```

### 3. Educação e Conscientização Científica (5 pontos) ✅

Documento HTML educativo sobre jogos de azar e seus riscos.

**Arquivo:** `docs/EXTRAS_EDUCACAO_CIENTIFICA.html`

### 4. Análise de Sensibilidade (4 pontos) ✅

Análise do impacto de variações de ±25% nos parâmetros do modelo.

---

## 🔬 Reprodutibilidade

Todos os experimentos utilizam **sementes fixas**:

| Experimento | Sementes | Observação |
|-------------|----------|------------|
| **Exp 1** | 2026 | 10.000 rodadas |
| **Exp 2** | 10, 2026, 123456 | 3 sequências independentes |
| **Exp 3** | 42 | 100 participantes |
| **Exp 4** | 2026 | Reutiliza resultados do Exp 1 |
| **Exp 5** | 2026 | Reutiliza resultados do Exp 1 |

---

## 📝 Conclusões

### Principais Resultados

1. **Experimento 1:** Frequências convergem para probabilidades teóricas
2. **Experimento 2:** Médias convergem para E[X] = -0,16
3. **Experimento 3:** Saldo limitado demonstra impacto da esperança negativa
4. **Experimento 4:** Confirmada independência entre rodadas
5. **Experimento 5:** RTP impacta diretamente os resultados

### Interpretação Estatística

A esperança matemática negativa (E[X] = -0,16) garante vantagem matemática ao operador no longo prazo.

---

## 🤖 Declaração de Uso de Inteligência Artificial

Este projeto foi desenvolvido com assistência de IA (Claude/Kiro) nas seguintes áreas:

- Implementação do código (maquina.py, calculos.py, experimentos.py, extras.py)
- Desenvolvimento dos 140 testes automatizados
- Documentação técnica
- Análise dos resultados

### Validação Independente

**Todos os valores foram validados através de:**
- 140 testes automatizados
- Verificação analítica manual
- Reprodutibilidade com sementes fixas

A equipe revisou, compreendeu e validou todo o trabalho entregue.

---

## 📚 Referências

[1] WORLD HEALTH ORGANIZATION. *Gambling*. 2 dez. 2024.

[2] WARDLE, H. et al. *The Lancet Public Health Commission on gambling*. The Lancet Public Health, v. 9, p. e950–e994, 2024.

[3] UNIVERSIDADE FEDERAL DE SÃO PAULO; UNIAD. *Caderno Temático LENAD III*. 2025.

[4] BRASIL. Lei nº 14.790, de 29 de dezembro de 2023.

[5] ILLOWSKY, B.; DEAN, S. *Introductory Statistics*. OpenStax, 2018.

---

## ⚠️ Aviso Legal

**Simulador acadêmico com fins exclusivamente educacionais.**

- ✅ Créditos fictícios
- ✅ Demonstra conceitos matemáticos
- ✅ Não representa produtos comerciais

---

**IFES Campus Serra - Sistemas de Informação - Outubro 2026**
