# EXTRA — VALIDAÇÃO AUTOMATIZADA (até 3 pontos)

**O que o enunciado pede (pág. 12):** "Acrescentar pelo menos cinco verificações automatizadas relevantes: pagamentos, lucro, semente, totais e um caso-limite. Explicar como executá-las."

**Evidência:** `tests/test_validacao.py` — 28 verificações em 5 grupos, uma para cada categoria pedida. Executa em cerca de 2 segundos.

---

## Como executar

Na pasta do projeto, com as dependências instaladas (`pip install -r requirements.txt`):

```bash
# Somente a validação automatizada (Extra)
python -m pytest tests/test_validacao.py -v

# Todos os testes do projeto
python -m pytest tests/ -v
```

O resultado esperado termina com `28 passed`. Se alguma verificação falhar, o pytest mostra qual teste falhou e os valores obtido e esperado.

---

## O que é verificado

| Categoria | Verificação | Por que importa |
|-----------|-------------|-----------------|
| **1. Pagamentos** | A-A-A, B-B-B, C-C-C, D-D-D e E-E-E pagam 5, 10, 15, 25 e 50 | Regras da Tabela 1 do enunciado |
| | As outras 120 triplas pagam 0 (verificação exaustiva das 125) | Nenhuma combinação paga por engano |
| | A tabela +10% paga exatamente 1,1 × a base em todas as triplas | Base do Experimento 5 |
| | Cada uma das 10.000 rodadas do E1 recebeu o prêmio da tabela | O simulador aplica a tabela corretamente |
| **2. Lucro** | X = P − 1 em todas as 125 triplas e nas 10.000 rodadas do E1 | Aposta de 1 crédito sempre descontada; prêmio bruto ≠ lucro |
| | E[X] = −0,16, RTP = 84%, P(prêmio) = 4%; tabela +10%: E[X] = −0,076, RTP = 92,4% | Valores de referência do enunciado |
| **3. Semente** | As 10 primeiras rodadas da semente 2026 são iguais a uma referência fixa (3ª rodada A-A-A, prêmio 5, lucro 4) | Detecta qualquer mudança no sorteio ou na montagem dos rolos |
| | Mesma semente → mesma sequência; sementes diferentes → sequências diferentes | Reprodução |
| | As 10 primeiras rodadas de uma execução são o início de uma execução mais longa com a mesma semente | O gerador é inicializado uma vez, não antes de cada rodada |
| **4. Totais** | O espaço amostral tem 125 triplas distintas e as probabilidades teóricas somam 1 | Modelo matemático consistente |
| | As contagens do E1 somam 10.000 e as frequências somam 1 | Conferência exigida na pág. 11 |
| | Os grupos do E4 somam 9.999 pares | Conferência exigida na pág. 11 |
| | O E5 tem o mesmo número de prêmios nas duas tabelas | As tabelas são aplicadas às mesmas rodadas |
| | As 5 paradas colocam 5 símbolos diferentes no centro | Cada símbolo tem chance 1/5 na linha central |
| **5. Casos-limite** | K = 4 forma a janela (E, A, B), voltando ao início do rolo | Operação "mod 5" (Figura 3 do enunciado) |
| | Paradas −1 e 5 e execução com 0 rodadas são rejeitadas com erro | Entradas inválidas não passam em silêncio |
| | E4 sem rodadas premiadas: grupo "após prêmio" registrado como não estimável | Não divide por zero (exigido no E4) |
| | Execução de uma única rodada | Menor entrada válida |

---

## Texto sugerido para o relatório (Seção 4.7.1)

> **Validação automatizada.** Além dos testes de cada módulo, foi criada uma bateria de 28 verificações automatizadas (`tests/test_validacao.py`), organizada em cinco grupos: (1) **pagamentos** — as cinco triplas premiadas pagam os valores da tabela e as outras 120 pagam zero, verificado exaustivamente sobre as 125 combinações; (2) **lucro** — o lucro de cada rodada é o prêmio menos a aposta de 1 crédito, e os valores teóricos E[X] = −0,16 e RTP = 84% são conferidos; (3) **semente** — as dez primeiras rodadas da semente 2026 são comparadas com uma referência fixa, e verifica-se que o gerador é inicializado uma única vez; (4) **totais** — as contagens do Experimento 1 somam 10.000 e os pares do Experimento 4 somam 9.999; (5) **casos-limite** — a janela circular para K = 4, entradas inválidas e o grupo sem pares do Experimento 4, registrado como não estimável. As verificações são executadas com `python -m pytest tests/test_validacao.py -v` e todas passaram no ambiente [Python X.Y, sistema operacional].

---

## Trecho sugerido para o README

```markdown
## Validação automatizada (Extra)

As verificações de consistência do simulador estão em `tests/test_validacao.py`
(pagamentos, lucro, semente, totais e casos-limite). Para executar:

    python -m pytest tests/test_validacao.py -v

Para executar todos os testes do projeto:

    python -m pytest tests/ -v
```
