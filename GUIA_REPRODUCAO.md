# Guia de Reprodução dos Experimentos

Este guia contém instruções detalhadas para reproduzir todos os experimentos do Trabalho I de Probabilidade e Estatística.

## Pré-requisitos

- Python 3.8 ou superior
- Ambiente virtual (recomendado)
- Dependências instaladas via `requirements.txt`

## Instalação

```bash
# 1. Clone o repositório (se aplicável)
git clone [URL_DO_REPOSITORIO]
cd prob-estat-1

# 2. Crie e ative o ambiente virtual
python -m venv venv

# Windows (bash):
source venv/Scripts/activate

# Linux/Mac:
source venv/bin/activate

# 3. Instale as dependências
pip install -r requirements.txt
```

## Estrutura de Diretórios

Antes de executar os experimentos, verifique que a estrutura de diretórios está completa:

```
prob-estat-1/
├── src/                          # Código-fonte dos módulos
├── resultados/                   # Resultados dos experimentos
│   ├── csvs/                     # Arquivos CSV gerados
│   └── graficos/                 # Gráficos gerados
├── docs/                         # Documentação técnica
├── tests/                        # Testes automatizados
├── executar_experimento_X.py     # Scripts de execução
└── gerar_relatorio.py            # Gerador de relatório
```

Os diretórios `resultados/csvs/` e `resultados/graficos/` são criados automaticamente pelos scripts.

---

## Experimento 1: Comportamento de Longo Prazo

**Objetivo:** Executar 10.000 rodadas e observar a convergência da frequência relativa para a probabilidade teórica.

**Parâmetros:**
- Número de rodadas: `10000`
- Semente aleatória: `2026`
- Aposta: `R$ 1,00`

**Comando:**
```bash
python executar_experimento_1.py
```

**Saídas esperadas:**
- Console: Tabela completa com lucros, probabilidades teóricas, contagens, frequências relativas
- Console: Métricas (lucro médio, RTP observado, proporção de prêmios, desvio-padrão)
- Console: Gráfico comparativo (teoria vs. observação)
- **Arquivo CSV:** `resultados/csvs/experimento1_resultados.csv`
- **Gráfico:** `resultados/graficos/experimento1_comparacao.png`

**Nota:** A documentação completa dos resultados está em `docs/FASE_2_DOCUMENTACAO.md`. A execução é opcional para entrega, pois os valores teóricos e interpretação já estão documentados.

**Validação:**
```bash
# Executar testes específicos do Experimento 1
pytest tests/test_experimento_1.py -v
```

---

## Experimento 2: Valor Esperado do Lucro (VPL)

**Objetivo:** Calcular o lucro esperado teórico de cada símbolo e verificar experimentalmente com 5.000 rodadas.

**Parâmetros:**
- Número de rodadas: `5000`
- Semente aleatória: `2025`
- Aposta: `R$ 1,00`

**Comando:**
```bash
python executar_experimento_2.py
```

**Saídas esperadas:**
- Console: Lucros teóricos e observados por símbolo
- Console: RTP teórico e observado
- **Arquivo CSV:** `resultados/csvs/experimento2_resultados.csv`
- **Gráfico:** `resultados/graficos/experimento2_comparacao.png` (barras lado a lado)

**Interpretação:** Disponível em `resultados/experimento_2_resumo_relatorio.txt`

**Validação:**
```bash
pytest tests/test_experimento_2.py -v
```

---

## Experimento 3: Repetição da Simulação (Reprodutibilidade)

**Objetivo:** Executar 10 simulações independentes de 1.000 rodadas e analisar a variabilidade do lucro médio e do RTP observado.

**Parâmetros:**
- Número de simulações: `10`
- Rodadas por simulação: `1000`
- Sementes: `101, 102, 103, ..., 110`
- Aposta: `R$ 1,00`

**Comando:**
```bash
python executar_experimento_3.py
```

**Saídas esperadas:**
- Console: Tabela com lucro médio e RTP observado de cada simulação
- Console: Estatísticas agregadas (média, DP, mín, máx)
- **Arquivo CSV:** `resultados/csvs/experimento3_resultados.csv`
- **Gráfico boxplot:** `resultados/graficos/experimento3_boxplot.png`
- **Gráfico linhas:** `resultados/graficos/experimento3_linhas.png`

**Interpretação:** Disponível em `resultados/experimento_3_interpretacao.txt`

**Validação:**
```bash
pytest tests/test_experimento_3.py -v
```

---

## Experimento 4: Comparação com o Esperado

**Objetivo:** Executar 5.000 rodadas e comparar o RTP observado com o RTP teórico, calculando o erro percentual.

**Parâmetros:**
- Número de rodadas: `5000`
- Semente aleatória: `2024`
- Aposta: `R$ 1,00`

**Comando:**
```bash
python executar_experimento_4.py
```

**Saídas esperadas:**
- Console: RTP teórico, RTP observado, erro percentual
- Console: Interpretação do resultado
- **Arquivo CSV:** `resultados/csvs/experimento4_resultados.csv`

**Interpretação:** Disponível em `resultados/experimento_4_interpretacao.txt`

**Validação:**
```bash
pytest tests/test_experimento_4.py -v
```

---

## Experimento 5: Análise de Cenários

**Objetivo:** Comparar dois cenários de apostas diferentes: 1.000 rodadas de R$ 10 vs. 10.000 rodadas de R$ 1.

**Parâmetros:**

**Cenário A:**
- Número de rodadas: `1000`
- Aposta: `R$ 10,00`
- Semente: `3001`

**Cenário B:**
- Número de rodadas: `10000`
- Aposta: `R$ 1,00`
- Semente: `3002`

**Comando:**
```bash
python executar_experimento_5.py
```

**Saídas esperadas:**
- Console: Comparação entre cenários (lucro total, lucro médio, RTP, desvio-padrão)
- Console: Análise interpretativa
- **Arquivo CSV:** `resultados/csvs/experimento5_comparacao.csv`

**Interpretação:** Disponível em `resultados/experimento_5_interpretacao.txt`

**Validação:**
```bash
pytest tests/test_experimento_5.py -v
```

**⚠️ IMPORTANTE:** Não execute novamente este experimento se o arquivo `resultados/csvs/experimento5_comparacao.csv` já existir e estiver validado. Os resultados foram verificados nos testes automatizados.

---

## Execução de Todos os Testes

Para validar todos os experimentos e módulos de uma vez:

```bash
# Executar todos os testes com relatório detalhado
pytest tests/ -v

# Executar com cobertura (se pytest-cov estiver instalado)
pytest tests/ --cov=src --cov-report=term-missing
```

**Resultado esperado:** 134 testes passando (100% de sucesso)

---

## Geração do Relatório Consolidado

(Funcionalidade planejada, não implementada na Fase 1)

```bash
python gerar_relatorio.py
```

---

## Verificações de Reprodutibilidade

Os experimentos foram projetados para serem **100% reprodutíveis** através de:

1. **Sementes fixas:** Cada experimento usa sementes documentadas
2. **Parâmetros fixos:** Número de rodadas, apostas e multiplicadores são constantes
3. **Testes automatizados:** 134 testes cobrem:
   - Cálculos de pagamento (test_calculos.py)
   - Cálculos de lucro (test_calculos.py)
   - Reprodutibilidade com sementes (test_maquina.py)
   - Soma de probabilidades = 1 (test_calculos.py)
   - Casos-limite (n_minimo em test_experimento_1.py)

4. **Validação contínua:** Execute `pytest tests/` antes e depois de cada experimento para confirmar integridade

---

## Solução de Problemas

### Erro: "No module named 'src'"
**Solução:** Execute os scripts a partir do diretório raiz do projeto (`prob-estat-1/`)

### Erro: "FileNotFoundError: resultados/csvs/"
**Solução:** Os diretórios são criados automaticamente. Se persistir, crie manualmente:
```bash
mkdir -p resultados/csvs resultados/graficos
```

### Testes falhando
**Solução:**
1. Verifique se todas as dependências estão instaladas: `pip install -r requirements.txt`
2. Confirme que está no ambiente virtual
3. Execute `pytest tests/ -v` para ver detalhes dos erros

### Gráficos não aparecem
**Solução:** Os gráficos são salvos automaticamente na pasta `resultados/graficos/`. Se usar ambiente sem interface gráfica (SSH, Docker), desabilite `plt.show()` editando os scripts de execução.

---

## Contato e Suporte

Para dúvidas sobre a reprodução dos experimentos, consulte:

- **Documentação técnica:** `docs/FASE_*_DOCUMENTACAO.md`
- **Relatório final:** `docs/RELATORIO_TRABALHO_I.docx`
- **Código-fonte:** Arquivos em `src/` com docstrings detalhadas

---

**Última atualização:** 2026-10-29  
**Versão do Python testada:** 3.8+  
**Tempo estimado de execução completa:** ~5 minutos (todos os experimentos + testes)
