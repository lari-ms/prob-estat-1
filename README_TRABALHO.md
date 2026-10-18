# Trabalho I - Probabilidade e Estatística

**Disciplina:** Probabilidade e Estatística I  
**Instituição:** IFES Campus Serra — Bacharelado em Sistemas de Informação  
**Entrega:** 29 de outubro de 2026

---

## 🎯 Status do Projeto

### ✅ FASE 1 CONCLUÍDA: Base Matemática
- Modelo de rolos implementado
- Cálculos teóricos validados
- 47 testes automatizados (100% passando)
- Reprodutibilidade garantida

### ⏳ Próximas Fases: Experimentos 1-5
- Pendentes: implementação dos 5 experimentos obrigatórios

---

## 🚀 Como Testar a Base (Fase 1)

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

### 2. Executar todos os testes

```bash
python -m pytest tests/ -v
```

**Resultado esperado:** 47 testes passando em ~0.4s

### 3. Testar a base (script essencial)

```bash
python testar_base.py
```

**Você verá:**
- Validação matemática automática
- Execução de 10 rodadas com semente 2026
- Verificação da rodada 3 (A-A-A)
- Valores teóricos de referência
- Confirmação: "✓ BASE ESTÁ PRONTA PARA OS EXPERIMENTOS"

---

## 📊 Validações Matemáticas

### Valores teóricos confirmados:

| Métrica | Esperado | Calculado | Status |
|---------|----------|-----------|--------|
| E[P] | 0.84 | 0.84 | ✅ |
| E[X] | -0.16 | -0.16 | ✅ |
| RTP | 84% | 84% | ✅ |
| P(prêmio) | 4% | 4% | ✅ |

---

## 📁 Estrutura Essencial

```
trabProb1/
├── src/                    # Código fonte
│   ├── maquina.py         # Núcleo: sorteio, rolos, execução
│   └── calculos.py        # Cálculos: probabilidades, esperança, RTP
├── tests/                  # Testes automatizados
│   ├── test_maquina.py    # 24 testes do núcleo
│   └── test_calculos.py   # 23 testes matemáticos
├── docs/                   # Documentação completa
├── testar_base.py         # Script ESSENCIAL de teste
└── requirements.txt        # Dependências
```

---

## 🧮 O que a base faz

### Funções principais (src/maquina.py):
- `sortear_parada(rng)` — Sorteia K uniformemente (0-4)
- `montar_coluna(parada)` — Monta coluna circular
- `executar_rodada(rng)` — Executa uma rodada completa
- `executar_rodadas(n, semente)` — Executa n rodadas

### Cálculos teóricos (src/calculos.py):
- `calcular_probabilidades_teoricas()` — Distribuição P(X=x)
- `calcular_esperanca_lucro()` — E[X] = -0.16
- `calcular_rtp_teorico()` — RTP = 84%
- `validar_valores_teoricos_tabela_base()` — Validação automática

### Exemplo de uso:

```python
from src.maquina import executar_rodadas

# Executa 10 rodadas
resultados = executar_rodadas(10, semente=2026)

# Cada resultado tem:
# - paradas: (K1, K2, K3)
# - linha_central: (símbolo1, símbolo2, símbolo3)
# - premio: float
# - lucro: float
```

---

## ✅ Checklist para a Equipe

Antes de aprovar a Fase 1, verifique:

- [ ] `pip install -r requirements.txt` executou sem erros
- [ ] `python -m pytest tests/ -v` mostra 47 passed
- [ ] `python testar_base.py` exibe "✓ TODOS OS TESTES PASSARAM!"
- [ ] Terceira rodada da semente 2026 é: A-A-A, prêmio 5, lucro 4
- [ ] Valores teóricos: E[X]=-0.16, RTP=84%, P(prêmio)=4%

**Todos OK?** ✅ Base aprovada, pode prosseguir para os experimentos!

---

## 📖 Documentação Completa

Consulte a pasta `docs/` para documentação detalhada:
- `docs/INDICE_GERAL.md` — Visão geral do projeto
- `docs/FASE_1_DOCUMENTACAO.md` — Documentação técnica completa da Fase 1

---

## 🔧 Ambiente

- **Python:** 3.12.7
- **SO:** Windows
- **Dependências principais:** numpy, pandas, matplotlib, pytest

---

## 👥 Equipe

[Adicionar nomes dos integrantes aqui]

---

## 🤖 Declaração de uso de IA

Esta base (Fase 1) foi desenvolvida com apoio de IA (Claude/Kiro).  
Todos os valores matemáticos foram validados independentemente.  
Todos os testes foram executados e confirmados pela equipe.

---

## 📅 Próximos Passos

1. ✅ Validar a base (vocês estão aqui!)
2. ⏳ Implementar Experimento 1 (10.000 rodadas)
3. ⏳ Implementar Experimento 2 (Lei dos Grandes Números)
4. ⏳ Implementar Experimento 3 (100 participantes)
5. ⏳ Implementar Experimento 4 (Probabilidade condicional)
6. ⏳ Implementar Experimento 5 (Comparação de tabelas)
7. ⏳ Elaborar relatório final

---

**Simulador acadêmico - somente créditos fictícios**
