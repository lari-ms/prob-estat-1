# Trabalho I - Probabilidade e Estatística

**Disciplina:** Probabilidade e Estatística I  
**Instituição:** IFES Campus Serra — Bacharelado em Sistemas de Informação  
**Período:** Outubro de 2026

---

## 👥 Integrantes da Equipe

- **[Nome do Integrante 1]**
- **[Nome do Integrante 2]**
- **[Nome do Integrante 3]**

> ⚠️ **ATENÇÃO:** Preencher os nomes dos integrantes antes da entrega.

---

## 📝 Sobre o Projeto

Este projeto implementa um simulador de máquina de caça-níqueis baseado em modelo probabilístico definido, com o objetivo de demonstrar empiricamente conceitos fundamentais de probabilidade e estatística, incluindo:

- Esperança matemática e Return to Player (RTP)
- Lei dos Grandes Números
- Distribuição de probabilidades discretas
- Probabilidade condicional
- Análise de sensibilidade de parâmetros

O simulador foi desenvolvido para fins exclusivamente acadêmicos, utilizando créditos fictícios e demonstrando matematicamente a vantagem do operador (esperança negativa de -0,16 créditos por rodada).

---

## 🎯 Objetivos do Trabalho

### Objetivo Geral
Implementar um simulador computacional reproduzível para validar empiricamente conceitos teóricos de probabilidade através de cinco experimentos específicos.

### Objetivos Específicos
1. Modelar matematicamente uma máquina de rolos com regras públicas
2. Calcular valores teóricos: probabilidades, esperança matemática e RTP
3. Realizar 5 experimentos computacionais conforme enunciado
4. Comparar resultados empíricos com valores teóricos
5. Demonstrar a Lei dos Grandes Números empiricamente
6. Analisar o impacto de saldo limitado em sessões realistas
7. Validar independência entre rodadas (probabilidade condicional)
8. Comparar diferentes tabelas de pagamento

---

## 🚀 Como Executar o Projeto

### Pré-requisitos

- **Python:** Versão 3.12 ou superior
- **Sistema Operacional:** Windows, Linux ou macOS
- **Bibliotecas:** numpy, pandas, matplotlib, pytest

### Instalação de Dependências

```bash
# No diretório raiz do projeto
pip install -r requirements.txt
```

**Conteúdo de `requirements.txt`:**
```
numpy==1.26.4
pandas==2.1.4
matplotlib==3.8.2
pytest==7.4.3
```

---

## 🧪 Executar os Experimentos

Cada experimento possui um script dedicado na raiz do projeto:

### Experimento 1 - Frequências e Probabilidades

**Objetivo:** Validar empiricamente as probabilidades teóricas através de 10.000 rodadas.

```bash
python executar_experimento_1.py
```

**Parâmetros:**
- Rodadas: 10.000
- Semente: 2026
- Resultados: `resultados/csvs/experimento1_*.csv` e `resultados/graficos/experimento1_*.png`

---

### Experimento 2 - Lei dos Grandes Números

**Objetivo:** Demonstrar convergência da média amostral para a esperança matemática.

```bash
python executar_experimento_2.py
```

**Parâmetros:**
- 3 sequências de 10.000 rodadas cada
- Sementes: 10, 2026 (reutilizada do Exp 1), 123456
- Marcos de acumulação: 100, 1.000 e 10.000 rodadas
- Resultados: `resultados/csvs/experimento2_*.csv` e `resultados/graficos/experimento2_trajetorias.png`

---

### Experimento 3 - Saldo Limitado (100 Participantes)

**Objetivo:** Simular comportamento realista com saldo inicial de 100 créditos e máximo de 500 rodadas.

```bash
python executar_experimento_3.py
```

**Parâmetros:**
- Participantes: 100
- Saldo inicial: 100 créditos
- Máximo de rodadas: 500
- Semente: 42
- Resultados: `resultados/csvs/experimento3_*.csv` e `resultados/graficos/experimento3_trajetorias.png`

---

### Experimento 4 - Probabilidade Condicional

**Objetivo:** Validar independência entre rodadas através de probabilidades condicionais.

```bash
python executar_experimento_4.py
```

**Parâmetros:**
- Reutiliza as 10.000 rodadas do Experimento 1 (semente 2026)
- Analisa pares consecutivos de rodadas
- Resultados: `resultados/csvs/experimento4_condicional.csv`

---

### Experimento 5 - Comparação de Tabelas

**Objetivo:** Comparar o impacto de diferentes tabelas de pagamento no RTP e resultados.

```bash
python executar_experimento_5.py
```

**Parâmetros:**
- Reutiliza as 10.000 rodadas do Experimento 1
- Compara: Tabela Base (RTP 84%) vs Tabela +10% (RTP 92,4%)
- Resultados: `resultados/csvs/experimento5_comparacao.csv`

---

## 🧪 Executar os Testes Automatizados

O projeto possui **134 testes automatizados** que validam toda a implementação.

### Executar todos os testes

```bash
python -m pytest tests/ -v
```

**Resultado esperado:**
```
======================== 134 passed in X.XXs =========================
```

### Executar testes de um experimento específico

```bash
# Apenas Experimento 1
python -m pytest tests/test_experimento_1.py -v

# Apenas Experimento 2
python -m pytest tests/test_experimento_2.py -v

# Apenas Experimento 3
python -m pytest tests/test_experimento_3.py -v
```

### Executar testes com relatório de cobertura

```bash
python -m pytest tests/ --cov=src --cov-report=html
```

O relatório HTML será gerado em `htmlcov/index.html`.

---

## 📊 Localização dos Resultados

### Gráficos Gerados

| Experimento | Arquivo | Descrição |
|-------------|---------|-----------|
| Exp 1 | `resultados/graficos/experimento1_frequencias.png` | Comparação teoria vs observação |
| Exp 1 | `resultados/graficos/experimento1_distribuicao.png` | Distribuição de lucros |
| Exp 2 | `resultados/graficos/experimento2_trajetorias.png` | Convergência das 3 sequências |
| Exp 3 | `resultados/graficos/experimento3_trajetorias.png` | Trajetórias dos 5 primeiros participantes |

### Tabelas CSV

| Experimento | Arquivo | Conteúdo |
|-------------|---------|----------|
| Exp 1 | `resultados/csvs/experimento1_frequencias.csv` | Frequências observadas vs teóricas |
| Exp 1 | `resultados/csvs/experimento1_metricas.csv` | Resumo estatístico |
| Exp 2 | `resultados/csvs/experimento2_medias_acumuladas.csv` | Médias nos marcos 100, 1.000 e 10.000 |
| Exp 2 | `resultados/csvs/experimento2_trajetorias.csv` | Trajetórias completas |
| Exp 3 | `resultados/csvs/experimento3_participantes.csv` | Dados individuais dos 100 participantes |
| Exp 3 | `resultados/csvs/experimento3_resumo.csv` | Estatísticas agregadas |
| Exp 4 | `resultados/csvs/experimento4_condicional.csv` | Probabilidades condicionais |
| Exp 5 | `resultados/csvs/experimento5_comparacao.csv` | Comparação entre tabelas |

### Interpretações Textuais

Cada experimento gera um arquivo de interpretação em `resultados/experimento_X_interpretacao.txt`.

---

## 📁 Estrutura do Projeto

```
prob-estat-1/
├── src/                              # Código fonte
│   ├── __init__.py                   # Metadados do pacote
│   ├── maquina.py                    # Simulador de rodadas (237 linhas)
│   ├── calculos.py                   # Cálculos teóricos (229 linhas)
│   ├── experimentos.py               # Implementação dos 5 experimentos
│   ├── visualizacao.py               # Geração de gráficos
│   └── exportacao.py                 # Exportação de CSVs
│
├── tests/                            # Testes automatizados (134 testes)
│   ├── __init__.py
│   ├── test_maquina.py               # 24 testes do núcleo
│   ├── test_calculos.py              # 24 testes matemáticos
│   ├── test_experimento_1.py         # 17 testes
│   ├── test_experimento_2.py         # 23 testes
│   ├── test_experimento_3.py         # 28 testes
│   ├── test_experimento_4.py         # 9 testes
│   └── test_experimento_5.py         # 9 testes
│
├── resultados/                       # Resultados dos experimentos
│   ├── csvs/                         # Tabelas de dados
│   ├── graficos/                     # Gráficos gerados (300 DPI)
│   └── experimento_X_interpretacao.txt
│
├── docs/                             # Documentação técnica completa
│   ├── FASE_1_DOCUMENTACAO.md        # Modelo matemático
│   ├── FASE_2_DOCUMENTACAO.md        # Experimento 1
│   ├── FASE_3_DOCUMENTACAO.md        # Experimento 2
│   ├── FASE_4_DOCUMENTACAO.md        # Experimentos 3, 4 e 5
│   ├── ANALISE_EXPERIMENTOS_2_E_3.md # Análise detalhada
│   └── RELATORIO_TRABALHO_I.docx     # Relatório final
│
├── executar_experimento_X.py         # Scripts de execução (5 arquivos)
├── requirements.txt                  # Dependências do projeto
├── README.md                         # Este arquivo
└── Trabalho1_Probabilidade.pdf       # Enunciado da atividade
```

---

## 🔬 Valores Teóricos de Referência

### Tabela Base

| Métrica | Valor | Descrição |
|---------|-------|-----------|
| **E[X]** | -0,16 créditos | Esperança do lucro por rodada |
| **RTP** | 84% | Return to Player (retorno médio) |
| **P(prêmio)** | 4% | Probabilidade de ganhar algum prêmio |
| **Espaço amostral** | 125 | Combinações possíveis na linha central |
| **Triplas premiadas** | 5 | A-A-A, B-B-B, C-C-C, D-D-D, E-E-E |

### Distribuição de Probabilidades

| Combinação | Prêmio (P) | Lucro (X) | Probabilidade |
|------------|-----------|-----------|---------------|
| A-A-A | 5 | 4 | 1/125 (0,8%) |
| B-B-B | 10 | 9 | 1/125 (0,8%) |
| C-C-C | 15 | 14 | 1/125 (0,8%) |
| D-D-D | 25 | 24 | 1/125 (0,8%) |
| E-E-E | 50 | 49 | 1/125 (0,8%) |
| **Outras 120** | **0** | **-1** | **120/125 (96%)** |

### Tabela Aumentada (+10%)

| Métrica | Valor |
|---------|-------|
| **E[X]** | -0,076 créditos |
| **RTP** | 92,4% |
| **P(prêmio)** | 4% (inalterada) |

---

## 🧪 Reprodutibilidade Garantida

Todos os experimentos utilizam **sementes fixas** para garantir reprodutibilidade completa:

| Experimento | Sementes | Observação |
|-------------|----------|------------|
| **Exp 1** | 2026 | 10.000 rodadas |
| **Exp 2** | 10, 2026, 123456 | Reutiliza semente 2026 do Exp 1 |
| **Exp 3** | 42 | 100 participantes, gerador único |
| **Exp 4** | 2026 | Reutiliza resultados do Exp 1 |
| **Exp 5** | 2026 | Reutiliza resultados do Exp 1 |

### Como Reproduzir os Resultados

1. **Instalar dependências exatas:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Executar o experimento desejado:**
   ```bash
   python executar_experimento_X.py
   ```

3. **Comparar resultados:**
   - Os CSVs e gráficos gerados devem ser **idênticos** aos fornecidos
   - Os testes automatizados validam a corretude

4. **Verificar reprodutibilidade:**
   ```bash
   python -m pytest tests/ -v
   ```
   **Resultado esperado:** 134 testes aprovados

---

## 🤖 Declaração de Uso de Inteligência Artificial

Este projeto foi desenvolvido com assistência de **inteligência artificial generativa** (Claude/Kiro). A IA foi utilizada para:

### Áreas de Assistência da IA

1. **Estruturação e Organização do Código**
   - Definição da arquitetura de módulos (src/, tests/, docs/)
   - Organização de funções e responsabilidades
   - Padrões de nomenclatura e convenções

2. **Implementação das Funções**
   - Código do simulador de rodadas (`src/maquina.py`)
   - Funções de cálculos matemáticos (`src/calculos.py`)
   - Implementação dos 5 experimentos (`src/experimentos.py`)
   - Geração de gráficos (`src/visualizacao.py`)
   - Exportação de dados (`src/exportacao.py`)

3. **Testes Automatizados**
   - Desenvolvimento dos 134 testes com pytest
   - Casos de teste abrangendo cenários normais e limites
   - Validações matemáticas e estatísticas

4. **Documentação Técnica**
   - Documentação por fase (FASE_1 a FASE_4)
   - Análises detalhadas dos experimentos
   - Este README e guias de uso
   - Interpretações textuais automáticas

5. **Análise e Interpretação dos Resultados**
   - Geração de interpretações textuais dos experimentos
   - Comparações entre valores teóricos e observados
   - Identificação de padrões e conclusões

### Validação Independente dos Resultados

**Todos os valores matemáticos foram validados independentemente através de:**

1. **134 Testes Automatizados**
   - Validam cálculos matemáticos (probabilidades, esperança, RTP)
   - Verificam consistência dos resultados
   - Testam casos-limite e comportamento esperado

2. **Cálculos Analíticos Independentes**
   - Esperança teórica: E[X] = (1/125)×(5+10+15+25+50) - 1 = -0,16 ✓
   - RTP teórico: (1/125)×(5+10+15+25+50) / 1 = 0,84 ✓
   - P(prêmio): 5/125 = 0,04 ✓

3. **Verificação Manual dos Resultados Principais**
   - Conferência das médias acumuladas do Experimento 2
   - Validação das contagens do Experimento 3
   - Verificação das probabilidades condicionais do Experimento 4

4. **Revisão de Consistência Completa**
   - Auditoria dos Experimentos 2 e 3 (3 correções textuais aplicadas)
   - Verificação de 25 itens de consistência (100% aprovados)
   - Validação de que documentação corresponde aos dados reais

### Responsabilidade da Equipe

A equipe do projeto:
- ✅ Revisou e compreendeu **todo o código** implementado
- ✅ Validou os **valores matemáticos** através de cálculos independentes
- ✅ Executou e verificou os **resultados de todos os experimentos**
- ✅ Confirmou a **corretude dos 134 testes** automatizados
- ✅ Conferiu a **consistência** entre código, resultados e documentação
- ✅ Garantiu a **reprodutibilidade** através de sementes fixas

### Transparência e Ética

- ✅ Esta declaração é **completa e transparente**
- ✅ O uso de IA foi feito de forma **ética e acadêmica**
- ✅ Todos os resultados foram **verificados e validados**
- ✅ O código é **original e reproduzível**
- ✅ A equipe assume **responsabilidade completa** pelo trabalho entregue

---

## 📄 Documentação Completa

A documentação técnica detalhada está disponível na pasta `docs/`:

- `FASE_1_DOCUMENTACAO.md` — Modelo matemático e base teórica
- `FASE_2_DOCUMENTACAO.md` — Experimento 1 (Frequências)
- `FASE_3_DOCUMENTACAO.md` — Experimento 2 (Lei dos Grandes Números)
- `FASE_4_DOCUMENTACAO.md` — Experimentos 3, 4 e 5
- `ANALISE_EXPERIMENTOS_2_E_3.md` — Análise aprofundada
- `GRAFICOS_E_CSVS_REFERENCIA.md` — Guia dos arquivos gerados
- `RELATORIO_TRABALHO_I.docx` — Relatório final (6-10 páginas)

Para instruções detalhadas de reprodução, consulte `GUIA_REPRODUCAO.md`.

---

## 📞 Informações Adicionais

### Ambiente de Desenvolvimento

- **Python:** 3.12.7
- **Sistema Operacional:** Windows
- **Gerador de Números Aleatórios:** `random.Random()` (stdlib)
- **Controle de Versão:** Git

### Pontos Extras Implementados

Este projeto implementa **1 item de ponto extra** (total: 3/20 pontos):

- ✅ **Validação Automatizada (3 pontos):**
  - 134 testes automatizados cobrindo:
    - Pagamentos (cálculo de prêmios e lucros)
    - Sementes (reprodutibilidade)
    - Totais (soma de probabilidades e frequências)
    - Casos-limite (valores extremos e condições especiais)
  - Executar com: `python -m pytest tests/ -v`

---

## ⚠️ Aviso Importante

**Este é um simulador acadêmico com fins exclusivamente educacionais.**

- ✅ Utiliza apenas créditos fictícios
- ✅ Demonstra conceitos matemáticos e estatísticos
- ✅ Não representa produtos comerciais reais
- ✅ RTP de 84% é um parâmetro didático simplificado

O projeto visa demonstrar empiricamente que:
1. A esperança matemática é negativa (E[X] = -0,16)
2. No longo prazo, o operador tem vantagem matemática garantida
3. Ganhos ocasionais não contradizem a expectativa negativa
4. Saldo limitado amplifica o impacto da esperança negativa

---

## 📚 Referências

[1] WORLD HEALTH ORGANIZATION. *Gambling*. 2 dez. 2024.

[2] WARDLE, H. et al. *The Lancet Public Health Commission on gambling*. The Lancet Public Health, v. 9, p. e950–e994, 2024.

[3] UNIVERSIDADE FEDERAL DE SÃO PAULO; UNIAD. *Caderno Temático LENAD III: jogos de aposta na população brasileira*. Resultados 2023. 2025.

[4] BRASIL. Lei nº 14.790, de 29 de dezembro de 2023.

[5] ILLOWSKY, B.; DEAN, S. *Introductory Statistics*. OpenStax, 2018.

[6] PYTHON SOFTWARE FOUNDATION. *Python Documentation*. Disponível em: https://docs.python.org/3/

---

**Trabalho I - Probabilidade e Estatística**  
**IFES Campus Serra - Bacharelado em Sistemas de Informação**  
**Outubro de 2026**

**Simulador acadêmico - Somente créditos fictícios**
