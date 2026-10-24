# FASE 4: EXPERIMENTO 3 - SALDO LIMITADO

**Status**: ✅ CONCLUÍDA  
**Data**: 24/10/2026  
**Pontuação**: 5 pontos (Experimento 3)

---

## 📋 OBJETIVO

Simular o comportamento de jogadores com **saldo limitado**, demonstrando o impacto da **esperança negativa** em sessões de jogo realistas com:
- Saldo inicial fixo (100 créditos)
- Paradas naturais (zeragem do saldo)
- Limite máximo de rodadas (500)

Este experimento simula de forma realista o comportamento de jogadores que não jogam indefinidamente, mas em sessões limitadas pelo capital disponível.

---

## 🎯 ESPECIFICAÇÃO DO EXPERIMENTO 3

### **Parâmetros**
- **100 participantes virtuais** independentes
- **Saldo inicial**: 100 créditos por participante
- **Máximo de rodadas**: 500 por participante
- **Condição de parada**: saldo zero OU 500 rodadas
- **Sementes**: base 3000, incrementadas para cada participante (3000, 3001, ..., 3099)

### **Dados a Calcular**
1. **Proporções de resultado**:
   - Ganhou (saldo final > saldo inicial)
   - Empatou (saldo final = saldo inicial)
   - Perdeu (saldo final < saldo inicial)
   - Zerou o saldo (saldo final = 0)

2. **Saldos finais**:
   - Média
   - Mediana

3. **Número de rodadas**:
   - Média
   - Mediana

4. **Gráfico**: 5 trajetórias amostrais de saldo ao longo das rodadas

---

## 📊 RESULTADOS OBTIDOS

### **Distribuição de Resultados**
| Resultado | Quantidade | Proporção |
|-----------|-----------|-----------|
| **Ganharam** | 21 | 21.0% |
| **Empataram** | 1 | 1.0% |
| **Perderam** | 78 | 78.0% |
| **Zeraram o saldo** | 62 | 62.0% |

### **Saldos Finais**
| Métrica | Valor |
|---------|-------|
| **Média** | 45.95 créditos |
| **Mediana** | 0.00 créditos |
| **Perda média** | 54.05 créditos (54.05% do capital) |

### **Número de Rodadas**
| Métrica | Valor |
|---------|-------|
| **Média** | 345.9 rodadas |
| **Mediana** | 352 rodadas |
| **Atingiram o máximo (500)** | 38 participantes (38.0%) |

---

## 🔍 INTERPRETAÇÃO DOS RESULTADOS

### **1. Esperança Negativa Confirmada**
- **78% dos participantes perderam**, confirmando que, mesmo em sessões limitadas, a esperança negativa do jogo se manifesta
- **Perda média de 54.05%** do capital inicial demonstra o forte impacto da vantagem matemática do operador

### **2. Zeragem de Saldo**
- **62% zeraram o saldo** antes de completar 500 rodadas
- Esta é a realidade mais severa do jogo: a maioria perde tudo antes de decidir parar voluntariamente
- A **mediana de saldo final sendo 0.00** indica que mais da metade dos jogadores perdeu todo o capital

### **3. Ganhos Ocasionais vs Perda Sistemática**
- Embora **21% tenham ganho**, isto NÃO contradiz a esperança negativa
- Estes são exemplos de **flutuação amostral positiva** (sorte em sessões limitadas)
- Se estes mesmos 21 participantes continuassem jogando, a Lei dos Grandes Números garante convergência para perda (Experimento 2)

### **4. Comparação com Experimento 2**
- **Exp. 2**: Demonstrou convergência teórica para E[X] = -0.1600 com rodadas ilimitadas
- **Exp. 3**: Demonstra o resultado prático em sessões limitadas: perda de 54% do capital
- A diferença existe porque no Exp. 3 há **paradas naturais** (zeragem), impedindo recuperação

### **5. Duração das Sessões**
- **Média de 345.9 rodadas** mostra que a maioria não completa as 500 rodadas permitidas
- **38% atingiram o máximo** (500 rodadas), conseguindo "sobreviver" por mais tempo apesar da esperança negativa
- Estes 38% incluem tanto os que ganharam quanto os que perderam mas mantiveram saldo positivo

---

## 📸 EVIDÊNCIAS VISUAIS

### **Gráfico de Trajetórias**
**Arquivo**: `resultados/graficos/experimento3_trajetorias.png`

**Características**:
- 5 trajetórias amostrais representativas
- Linha de referência: saldo inicial (100 créditos)
- Linha de referência: saldo zero (perda total)
- Mostra diversidade de comportamentos:
  - Participantes que zeraram rapidamente
  - Participantes que zeraram após muitas rodadas
  - Participantes que ganharam (terminaram acima de 100)

**Observações**:
- A maioria das trajetórias converge para zero ou valores baixos
- Flutuações visíveis mesmo em curto prazo
- Saldos que chegam a zero param imediatamente (condição de parada)

---

## 💾 ARQUIVOS GERADOS

### **CSVs**
1. **`experimento3_resumo.csv`**: Tabela de estatísticas agregadas
   - Métricas principais (médias, medianas, proporções)
   - Formato vertical (métrica | valor)

2. **`experimento3_participantes.csv`**: Dados individuais dos 100 participantes
   - Colunas: ID, Semente, Saldo Inicial, Saldo Final, Número de Rodadas, Zerou, Resultado, Variação Saldo, Variação %
   - 100 linhas (uma por participante)

3. **`experimento_3_configuracao.csv`**: Parâmetros de execução
   - n_participantes, saldo_inicial, max_rodadas, semente_base, python_version, tabela

### **Gráficos**
- **`experimento3_trajetorias.png`**: Gráfico de trajetórias (5 amostras)

### **Interpretação**
- **`experimento_3_interpretacao.txt`**: Interpretação textual completa dos resultados

---

## 🧪 VALIDAÇÃO

### **Testes Automatizados**
**Total**: 26 testes (todos passando ✅)

**Categorias**:
1. **Básicos** (5 testes): Estrutura, parâmetros, limites
2. **Contagens** (5 testes): Proporções, consistência de resultados
3. **Estatísticas** (4 testes): Cálculo de médias e medianas
4. **Comportamento esperado** (5 testes): Esperança negativa, convergência
5. **Reprodutibilidade** (2 testes): Sementes, determinismo
6. **Paradas corretas** (2 testes): Zeragem, máximo de rodadas
7. **Interpretação** (3 testes): Função de interpretação

### **Comando para Executar Testes**
```bash
python -m pytest tests/test_experimento_3.py -v
```

### **Verificações de Consistência**
- ✅ Contagens somam o total de participantes
- ✅ Proporções somam 100%
- ✅ Nenhum saldo final é negativo
- ✅ Nenhum participante excede 500 rodadas
- ✅ Quem zerou está marcado como perdeu
- ✅ Histórico de saldos tem tamanho correto
- ✅ Média de saldo final < saldo inicial (esperança negativa)
- ✅ Maioria perdeu (esperança negativa)
- ✅ Reprodutibilidade com mesma semente

---

## 🎓 CONCEITOS DEMONSTRADOS

### **1. Saldo Limitado e Paradas Naturais**
- Jogadores reais não têm capital ilimitado
- A zeragem do saldo é uma parada forçada e irreversível
- Mesmo com paradas naturais, a esperança negativa se manifesta

### **2. Diferença entre Lucro Esperado e Resultado Prático**
- **E[X] = -0.1600** por rodada (teórico)
- **Perda média de 54.05%** do capital (prático com saldo limitado)
- A diferença existe porque paradas naturais impedem recuperação

### **3. Flutuação Amostral vs Tendência Sistemática**
- **21% ganharam** (flutuação positiva de curto prazo)
- **78% perderam** (tendência sistemática predomina)
- **Saldo médio final sempre < inicial** (esperança negativa garantida)

### **4. Risco de Ruína**
- **62% zeraram o saldo** = Risco de ruína significativo
- A maioria perde tudo antes de decidir parar voluntariamente
- Demonstra o perigo de jogar com capital limitado

### **5. Simulação Realista**
- Experimento 3 simula condições reais de jogo
- Sessões limitadas por capital e/ou tempo
- Resultados agregados sempre negativos para os jogadores

---

## 📝 PARA O RELATÓRIO (SEÇÃO 4.4)

### **Tabela a Incluir**
Use: `resultados/csvs/experimento3_resumo.csv`

### **Gráfico a Incluir**
Use: `resultados/graficos/experimento3_trajetorias.png`

### **Dados Individuais (Opcional)**
Para referência: `resultados/csvs/experimento3_participantes.csv`

### **Interpretação**
Copie de: `resultados/experimento_3_interpretacao.txt`

### **Legendas Sugeridas**
- **Tabela 4**: Resumo estatístico do Experimento 3 (Saldo Limitado)
- **Gráfico 4**: Trajetórias amostrais de saldo com capital limitado (5 participantes de 100)

---

## 🔄 REPRODUTIBILIDADE

### **Executar Novamente**
```bash
python executar_experimento_3.py
```

### **Resultados Garantidos**
- Mesma semente_base → Mesmos resultados
- Sementes: 3000, 3001, ..., 3099
- Reprodutibilidade total garantida

---

## ✅ CHECKLIST DE CONCLUSÃO

- [x] Função `experimento_3()` implementada
- [x] Função `interpretar_experimento_3()` implementada
- [x] Funções de exportação CSV implementadas
- [x] Função de visualização implementada
- [x] Script de execução criado
- [x] 26 testes automatizados (todos passando)
- [x] Experimento executado com sucesso
- [x] CSVs gerados e validados
- [x] Gráfico gerado e validado
- [x] Interpretação gerada
- [x] Documentação completa
- [x] Integração com sistema existente

---

## 🎯 PRÓXIMOS PASSOS

1. **Experimento 4**: Probabilidade Condicional (Fase 5)
2. **Experimento 5**: Comparação de Tabelas de Pagamento (Fase 6)
3. **Discussão Crítica**: 25 pontos
4. **Comunicação do Relatório**: 15 pontos
5. **Pontos Extras** (opcional): até 20 pontos

---

**Progresso do Projeto**: 50/100 pontos obrigatórios (50%)
- ✅ Fase 1: Base Matemática (35 pontos)
- ✅ Fase 2: Experimento 1 (5 pontos)
- ✅ Fase 3: Experimento 2 (5 pontos)
- ✅ Fase 4: Experimento 3 (5 pontos)
- ⏳ Fase 5: Experimento 4 (5 pontos)
- ⏳ Fase 6: Experimento 5 (5 pontos)
- ⏳ Discussão Crítica (25 pontos)
- ⏳ Comunicação (15 pontos)
