# DOCUMENTAÇÃO DO TRABALHO I — ÍNDICE GERAL

**Projeto:** Simulador de Máquina de Rolos  
**Disciplina:** Probabilidade e Estatística I  
**Instituição:** IFES Campus Serra — Bacharelado em Sistemas de Informação  
**Professor:** Fidelis Zanetti de Castro  
**Entrega:** 29 de outubro de 2026

---

## 📚 ESTRUTURA DA DOCUMENTAÇÃO

Este projeto está sendo desenvolvido de forma **incremental e verificável**, com documentação detalhada de cada fase. Cada documento de fase contém:

- Objetivos e escopo
- Arquitetura e implementação
- Testes executados e resultados
- Valores teóricos e validações
- Notas para o relatório final
- Checklist de conformidade

---

## 🗂️ FASES DO PROJETO

### ✅ Fase 0 — Diagnóstico e Planejamento
**Status:** Concluída  
**Documento:** Incorporado no resumo da Fase 1  
**Principais entregas:**
- Análise completa do enunciado
- Identificação de todos os requisitos (100 + 20 pontos)
- Plano de implementação incremental
- Arquitetura proposta
- Matriz de conformidade preliminar

---

### ✅ Fase 1 — Modelo Matemático e Funções Básicas
**Status:** Concluída ✅  
**Documento:** [FASE_1_DOCUMENTACAO.md](./FASE_1_DOCUMENTACAO.md)  
**Principais entregas:**
- Núcleo do simulador (sorteio, montagem, execução)
- Cálculos matemáticos validados
- 47 testes automatizados (100% sucesso)
- Reprodutibilidade garantida
- Valores teóricos validados

**Pontuação associada:** 15 pontos (Modelo implementado)

---

### ✅ Fase 2 — Experimento 1: Frequências e Probabilidades
**Status:** Concluída ✅  
**Documento:** [FASE_2_DOCUMENTACAO.md](./FASE_2_DOCUMENTACAO.md)  
**Principais entregas:**
- 10.000 rodadas executadas com semente 2026
- Tabelas de frequências e métricas (CSVs exportados)
- Lucro médio: -0.1315 vs -0.16 teórico
- RTP observado: 86.85% vs 84% teórico
- 2 gráficos de alta qualidade (300 DPI)
- Sistema de cache para reutilização
- 17 testes automatizados (100% passando)

**Pontuação associada:** 5 pontos (Experimento 1)

---

### ✅ Fase 3 — Experimento 2: Lei dos Grandes Números
**Status:** Concluída ✅  
**Documento:** [FASE_3_DOCUMENTACAO.md](./FASE_3_DOCUMENTACAO.md)  
**Principais entregas:**
- 3 sequências (sementes 10, 2026, 123456)
- Reutilização da sequência 2026 do E1 ✓
- Tabela 3×3 de médias acumuladas
- Gráfico de trajetórias convergindo para E[X]
- Demonstração empírica da LGN
- 22 testes automatizados (100% passando)

**Pontuação associada:** 5 pontos (Experimento 2)

---

### ✅ Fase 4 — Experimento 3: Saldo Limitado
**Status:** Concluída ✅  
**Documento:** [FASE_4_DOCUMENTACAO.md](./FASE_4_DOCUMENTACAO.md)  
**Principais entregas:**
- 100 participantes virtuais simulados
- Saldo inicial 100, máx 500 rodadas
- Proporções: 21% ganhou, 78% perdeu, 62% zerou
- Perda média: 54.05% do capital inicial
- Gráfico de 5 trajetórias representativas
- 26 testes automatizados (100% passando)

**Pontuação associada:** 5 pontos (Experimento 3)

---

### ⏳ Fase 5 — Experimento 4: Probabilidade Condicional
**Status:** Não iniciada  
**Documento:** FASE_5_DOCUMENTACAO.md (será criado)  
**Principais entregas previstas:**
- Análise de 9.999 pares consecutivos
- Grupos condicionais (após prêmio / após não-prêmio)
- Tabela com denominadores e proporções
- Tratamento de grupo vazio
- Interpretação sobre independência

**Pontuação associada:** 5 pontos (Experimento 4)

---

### ⏳ Fase 6 — Experimento 5: Comparação de Pagamentos
**Status:** Não iniciada  
**Documento:** FASE_6_DOCUMENTACAO.md (será criado)  
**Principais entregas previstas:**
- Reutilização dos 10.000 resultados do E1
- Aplicação de 2 tabelas (base e +10%)
- Comparação completa de métricas
- Interpretação sobre chance vs tamanho de prêmio

**Pontuação associada:** 5 pontos (Experimento 5)

---

### ⏳ Fase 7 — Integração e Testes Obrigatórios
**Status:** Não iniciada  
**Documento:** FASE_7_DOCUMENTACAO.md (será criado)  
**Principais entregas previstas:**
- Execução integrada dos 5 experimentos
- Testes de reutilização de sequências
- Verificação de consistência
- Auditoria de totais e contagens
- Validação completa sem regressões

**Pontuação associada:** Consolidação dos 100 pontos obrigatórios

---

### ⏳ Fases 8-13 — Extras (até 20 pontos)
**Status:** Não iniciadas (opcionais)  
**Documentos:** Serão criados conforme necessário

---

#### ⏳ Fase 8 — Extra A: Intervalos de Confiança (4 pontos)
**Status:** Não iniciada  
**Documento:** FASE_8_EXTRA_A.md (será criado)  
**Principais entregas previstas:**
- Cálculo do erro padrão da média amostral
- Construção de IC 95% para o lucro médio e RTP
- Verificação se valores teóricos pertencem aos intervalos
- Interpretação sobre estimativas e incerteza amostral

**Pontuação associada:** 4 pontos (Extra A)

---

#### ⏳ Fase 9 — Extra B: Mesma Média, Riscos Diferentes (4 pontos)
**Status:** Não iniciada  
**Documento:** FASE_9_EXTRA_B.md (será criado)  
**Principais entregas previstas:**
- Criação de tabela alternativa com E[X] igual
- Comparação de variâncias entre as duas tabelas
- Simulação com ambas as tabelas
- Análise de risco e volatilidade
- Interpretação sobre média vs dispersão

**Pontuação associada:** 4 pontos (Extra B)

---

#### ⏳ Fase 10 — Extra C: Validação Automatizada (3 pontos)
**Status:** Não iniciada  
**Documento:** FASE_10_EXTRA_C.md (será criado)  
**Principais entregas previstas:**
- Bateria de testes automatizados para consistência
- Verificação de invariantes (somas, proporções)
- Testes de regressão para evitar quebras
- Documentação dos critérios de validação
- Suite completa de testes

**Pontuação associada:** 3 pontos (Extra C)

---

#### ⏳ Fase 11 — Extra D: Análise de Sensibilidade (3 pontos)
**Status:** Não iniciada  
**Documento:** FASE_11_EXTRA_D.md (será criado)  
**Principais entregas previstas:**
- Variação de parâmetros (número de faces, prêmios)
- Análise do impacto no RTP e lucro esperado
- Gráficos de sensibilidade
- Interpretação sobre design de jogos
- Recomendações baseadas em análise

**Pontuação associada:** 3 pontos (Extra D)

---

#### ⏳ Fase 12 — Extra E: Auditoria de Afirmação Pública (3 pontos)
**Status:** Não iniciada  
**Documento:** FASE_12_EXTRA_E.md (será criado)  
**Principais entregas previstas:**
- Análise crítica de afirmações de cassinos/loterias
- Verificação matemática de declarações publicitárias
- Identificação de informações enganosas
- Comparação com resultados do simulador
- Relatório de auditoria com evidências

**Pontuação associada:** 3 pontos (Extra E)

---

#### ⏳ Fase 13 — Extra F: Educação Científica (3 pontos)
**Status:** Não iniciada  
**Documento:** FASE_13_EXTRA_F.md (será criado)  
**Principais entregas previstas:**
- Material educativo sobre probabilidade e jogos
- Explicação de conceitos-chave (RTP, esperança, variância)
- Exemplos práticos e simulações interativas
- Desmistificação de falácias comuns
- Guia para interpretação crítica

**Pontuação associada:** 3 pontos (Extra F)

---

### ⏳ Fase 14 — Relatório, README e Pacote Final
**Status:** Não iniciada  
**Documento:** FASE_14_DOCUMENTACAO.md (será criado)  
**Principais entregas previstas:**
- Relatório PDF de 6-10 páginas
- README completo
- Todos os CSVs organizados
- Todos os gráficos gerados
- Instruções de reprodução
- Declaração de uso de IA

**Pontuação associada:** 15 pontos (Comunicação)

---

### ⏳ Fase 15 — Auditoria Final de Conformidade
**Status:** Não iniciada  
**Documento:** FASE_15_DOCUMENTACAO.md (será criado)  
**Principais entregas previstas:**
- Matriz de conformidade completa
- Verificação de todos os 120 pontos
- Lista de evidências por critério
- Identificação de pendências
- Recomendações finais

**Pontuação associada:** Validação final

---

## 📊 PROGRESSO GERAL

### Pontuação alcançada

| Categoria | Pontos max. | Concluído | Status |
|-----------|-------------|-----------|--------|
| Modelo implementado | 15 | 15 | ✅ |
| Conceitos e cálculos | 20 | 20 | ✅ |
| Experimento 1 | 5 | 5 | ✅ |
| Experimento 2 | 5 | 5 | ✅ |
| Experimento 3 | 5 | 5 | ✅ |
| Experimento 4 | 5 | 0 | ⏳ |
| Experimento 5 | 5 | 0 | ⏳ |
| Discussão crítica | 25 | 0 | ⏳ |
| Comunicação | 15 | 0 | ⏳ |
| **Subtotal obrigatório** | **100** | **50** | **50%** |
| Extras | 20 | 0 | ⏳ |
| **TOTAL** | **120** | **50** | **42%** |

### Timeline

```
Fase 0 ✅━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
Fase 1 ✅━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
Fase 2 ✅━━━━━━━━━━━━━━━━━━━━━━━━━━━┫ Concluído
Fase 3 ✅━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
Fase 4 ✅━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
Fase 5 ⏳─────────────────────────────┤ Próxima
Fase 6 ⏳─────────────────────────────┤ A fazer
Fase 7 ⏳─────────────────────────────┤
Fase 14 ⏳────────────────────────────┤
Fase 15 ⏳────────────────────────────┘
```

---

## 🎯 COMO USAR ESTA DOCUMENTAÇÃO

### Para acompanhamento do desenvolvimento
1. Consulte este índice para ver o progresso geral
2. Acesse o documento específico de cada fase para detalhes
3. Verifique a pontuação alcançada em cada categoria

### Para elaboração do relatório final
1. Use as seções "Notas para o Relatório" de cada fase
2. Reúna os valores teóricos validados
3. Colete os gráficos e tabelas gerados
4. Compile as interpretações dos experimentos
5. Use os conceitos demonstrados para a discussão

### Para apresentação/defesa
1. Os documentos contêm explicações detalhadas
2. Todos os testes estão documentados
3. Decisões técnicas estão justificadas
4. Valores de referência estão claramente indicados

---

## 📝 CONVENÇÕES DA DOCUMENTAÇÃO

### Status
- ✅ **Concluída e validada** — Testes passaram, aprovada
- 🔄 **Em desenvolvimento** — Implementação em andamento
- ⏳ **Aguardando** — Dependência de fase anterior
- ❌ **Bloqueada** — Impedimento identificado

### Símbolos
- 🎯 Objetivo
- 🏗️ Arquitetura
- 🧮 Matemática
- 🧪 Testes
- 🔄 Reprodutibilidade
- 📦 Dependências
- 📝 Notas
- 🏁 Conclusão

### Checklist
- [x] Item concluído
- [ ] Item pendente
- [~] Item parcial

---

## 🔗 LINKS ÚTEIS

### Documentos do projeto
- [Enunciado completo](../Trabalho1_Probabilidade.md)
- [Código fonte](../src/)
- [Testes automatizados](../tests/)
- [Scripts de demonstração](../demo_fase1.py)

### Referências externas
- Python 3.12 Documentation: https://docs.python.org/3.12/
- NumPy Documentation: https://numpy.org/doc/
- Matplotlib Gallery: https://matplotlib.org/stable/gallery/
- Pytest Documentation: https://docs.pytest.org/

---

## 📧 METADADOS

**Última atualização:** Fase 4 concluída  
**Próxima revisão:** Após conclusão da Fase 5  
**Versão:** 1.2

---

**Este índice é atualizado automaticamente a cada fase concluída.**
