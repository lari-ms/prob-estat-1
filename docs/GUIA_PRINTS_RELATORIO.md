# 📸 GUIA DE CAPTURA DE PRINTS PARA O RELATÓRIO

**Para:** Seções 4.2 (Experimento 1) e 4.3 (Experimento 2) do relatório Word  
**Objetivo:** Documentar visualmente os resultados obtidos

---

## 🎯 PRINTS NECESSÁRIOS

### EXPERIMENTO 1

#### Print 1.1: Execução do Experimento 1
**Comando:**
```bash
python executar_experimento_1.py
```

**O que capturar:**
- Cabeçalho "EXPERIMENTO 1: FREQUÊNCIAS E PROBABILIDADES"
- Tabela de frequências observadas vs teóricas
- Métricas principais (lucro médio, RTP, prêmios)
- Lista de arquivos gerados

**Nome do arquivo:** `prints/experimento1_execucao.png`

**Para o relatório:**
> **Figura X:** Saída da execução do Experimento 1, mostrando as métricas observadas em 10.000 rodadas (semente 2026) e a comparação com os valores teóricos.

---

#### Print 1.2: Gráfico de Distribuição
**Arquivo:** `resultados/graficos/experimento1_distribuicao.png`

**Já salvo!** Inserir diretamente no relatório.

**Para o relatório:**
> **Figura Y:** Distribuição dos lucros observados em 10.000 rodadas. A perda de -1 crédito representa 95,88% das rodadas (9.588 ocorrências), enquanto os prêmios representam 4,12% (412 ocorrências).

---

#### Print 1.3: Gráfico de Comparação
**Arquivo:** `resultados/graficos/experimento1_frequencias.png`

**Já salvo!** Inserir diretamente no relatório.

**Para o relatório:**
> **Figura Z:** Comparação entre probabilidades teóricas e frequências observadas. O painel superior mostra a perda (-1 crédito) e o painel inferior mostra os cinco resultados premiados, cada um com probabilidade teórica de 0,80%.

---

#### Print 1.4: Testes do Experimento 1
**Comando:**
```bash
python -m pytest tests/test_experimento_1.py -v
```

**O que capturar:**
- Lista dos 17 testes
- Status PASSED em verde
- Tempo de execução
- Resumo "17 passed"

**Nome do arquivo:** `prints/experimento1_testes.png`

**Para o relatório (Anexo ou Seção de Validação):**
> **Figura W:** Bateria de testes automatizados do Experimento 1, com 17 testes unitários validando a correção da implementação.

---

### EXPERIMENTO 2

#### Print 2.1: Execução do Experimento 2
**Comando:**
```bash
python executar_experimento_2.py
```

**O que capturar:**
- Cabeçalho "EXPERIMENTO 2: LEI DOS GRANDES NÚMEROS"
- Confirmação da reutilização da semente 2026
- Tabela de médias acumuladas (3×3)
- Tabela de diferenças
- Lista de arquivos gerados
- Mensagem final sobre convergência

**Nome do arquivo:** `prints/experimento2_execucao.png`

**Para o relatório:**
> **Figura A:** Saída da execução do Experimento 2, demonstrando a convergência das médias acumuladas de três sequências independentes para a esperança teórica E[X] = -0,1600.

---

#### Print 2.2: Gráfico de Trajetórias
**Arquivo:** `resultados/graficos/experimento2_trajetorias.png`

**Já salvo!** Inserir diretamente no relatório.

**Para o relatório:**
> **Figura B:** Trajetórias das médias acumuladas demonstrando a Lei dos Grandes Números. As três linhas coloridas representam sequências independentes (sementes 10, 2026 e 123456) convergindo para E[X] = -0,1600 (linha tracejada horizontal).

---

#### Print 2.3: Tabela CSV Formatada
**Arquivo:** `resultados/csvs/experimento2_medias_acumuladas.csv`

**Como fazer:**
1. Abrir o CSV no Excel ou LibreOffice Calc
2. Formatar:
   - Adicionar bordas nas células
   - Centralizar cabeçalho
   - Formatar números com 6 casas decimais
   - Negrito na linha "E[X] teórico"
3. Tirar print da tabela formatada

**Nome do arquivo:** `prints/experimento2_tabela_formatada.png`

**Para o relatório:**
> **Tabela X:** Médias acumuladas das três sequências em 1.000, 5.000 e 10.000 rodadas, comparadas com E[X] = -0,1600. Observa-se que as médias aproximam-se progressivamente do valor teórico.

---

#### Print 2.4: Testes do Experimento 2
**Comando:**
```bash
python -m pytest tests/test_experimento_2.py -v
```

**O que capturar:**
- Lista dos 22 testes
- Status PASSED em verde
- Tempo de execução
- Resumo "22 passed"

**Nome do arquivo:** `prints/experimento2_testes.png`

**Para o relatório (Anexo ou Seção de Validação):**
> **Figura C:** Validação automatizada do Experimento 2, com 22 testes unitários incluindo verificações de convergência, reprodutibilidade e reutilização da sequência 2026.

---

#### Print 2.5: Todos os Testes Passando
**Comando:**
```bash
python -m pytest tests/ -v --tb=short
```

**O que capturar:**
- Resumo final mostrando "86 passed"
- Tempo total de execução

**Nome do arquivo:** `prints/todos_testes_passando.png`

**Para o relatório (Anexo ou Introdução da Seção de Resultados):**
> **Figura D:** Bateria completa de testes do projeto, com 86 testes unitários validando a implementação completa da Fase 1 (base matemática), Experimento 1 e Experimento 2.

---

## 🖼️ COMO CAPTURAR OS PRINTS

### No Windows:

#### Método 1: Ferramenta de Captura (Recomendado)
1. Pressione `Win + Shift + S`
2. Selecione a área desejada
3. A captura vai para a área de transferência
4. Abra Paint ou Word e cole (`Ctrl + V`)
5. Salve como PNG

#### Método 2: Print Screen
1. Pressione `Print Screen` (tela completa) ou `Alt + Print Screen` (janela ativa)
2. Abra Paint
3. Cole (`Ctrl + V`)
4. Recorte a área relevante
5. Salve como PNG

#### Método 3: Snipping Tool (Ferramenta de Recorte)
1. Busque "Snipping Tool" no menu Iniciar
2. Novo → Selecione a área
3. Salve como PNG

---

## 📁 ORGANIZAÇÃO DOS ARQUIVOS

### Opção 1: Criar pasta de prints
```
docs/
  prints/
    experimento1_execucao.png
    experimento1_testes.png
    experimento2_execucao.png
    experimento2_tabela_formatada.png
    experimento2_testes.png
    todos_testes_passando.png
```

### Opção 2: Inserir diretamente no Word
- Não salvar os prints separadamente
- Capturar e colar diretamente no relatório
- Usar `Ctrl + V` após captura

---

## 📝 CHECKLIST COMPLETO

### Experimento 1:
- [ ] Print da execução (terminal)
- [ ] Gráfico de distribuição (já salvo)
- [ ] Gráfico de comparação (já salvo)
- [ ] Print dos testes (opcional)

### Experimento 2:
- [ ] Print da execução (terminal)
- [ ] Gráfico de trajetórias (já salvo)
- [ ] Tabela CSV formatada (Excel)
- [ ] Print dos testes (opcional)

### Geral:
- [ ] Print de todos os testes passando (86/86)

---

## 💡 DICAS IMPORTANTES

### Para melhor qualidade:

1. **Resolução:** Use resolução mínima de 1920×1080
2. **Zoom:** Ajuste o zoom do terminal para texto legível
3. **Recorte:** Remova partes desnecessárias (barra de título, etc.)
4. **Formato:** Sempre salve em PNG (não JPG)
5. **Contraste:** Use fundo claro no terminal para melhor impressão

### Para o relatório Word:

1. **Inserir imagem:**
   - Inserir → Imagens → Selecione o arquivo
   - Ou copie e cole diretamente

2. **Redimensionar:**
   - Clique na imagem
   - Arraste os cantos mantendo proporção
   - Largura ideal: 15-16 cm

3. **Adicionar legenda:**
   - Clique com botão direito na imagem
   - Inserir Legenda
   - Tipo: "Figura" ou "Tabela"
   - Digite a descrição

4. **Formatar:**
   - Alinhamento: Centralizado
   - Quebra de texto: "Em linha com o texto"
   - Adicionar "Fonte: Elaborado pelos autores" abaixo

---

## 🎨 EXEMPLO DE FORMATAÇÃO NO WORD

```
[IMAGEM CENTRALIZADA]

Figura 1 - Saída da execução do Experimento 1, mostrando as métricas 
observadas em 10.000 rodadas (semente 2026) e a comparação com os 
valores teóricos.

Fonte: Elaborado pelos autores.
```

---

## ⚡ ATALHOS RÁPIDOS

### Para captura no Windows:
- `Win + Shift + S` → Captura de área seletiva
- `Print Screen` → Captura de tela completa
- `Alt + Print Screen` → Captura da janela ativa

### Para o Word:
- `Ctrl + V` → Colar imagem
- `Ctrl + Enter` → Quebra de página
- `Alt + Shift + C` → Inserir legenda (em alguns Word)

---

## 🚀 WORKFLOW RECOMENDADO

### Para cada experimento:

1. **Execute o script**
   ```bash
   python executar_experimento_X.py
   ```

2. **Capture a tela** (`Win + Shift + S`)

3. **Cole no Paint** ou diretamente no Word

4. **Recorte** se necessário

5. **Salve** ou insira no relatório

6. **Adicione legenda** seguindo o padrão

7. **Repita** para próximo print

---

## ✅ RESULTADO ESPERADO

Ao final, o relatório deve ter:

- **Seção 4.2 (Experimento 1):**
  - 1-2 prints de execução/tabelas
  - 2 gráficos (distribuição e comparação)
  - Legendas descritivas

- **Seção 4.3 (Experimento 2):**
  - 1 print de execução
  - 1 gráfico de trajetórias
  - 1 tabela formatada
  - Legendas descritivas

- **Anexo (opcional):**
  - Prints de testes passando
  - Evidências de validação

**Total estimado:** 6-8 figuras bem documentadas

---

**Lembre-se:** Os gráficos PNG já estão salvos em alta resolução (300 DPI) e prontos para inserir diretamente no relatório. Você só precisa capturar os prints das execuções no terminal! 🎯
