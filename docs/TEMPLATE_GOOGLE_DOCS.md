# GUIA: COMO USAR A DOCUMENTAÇÃO NO GOOGLE DOCS

Este arquivo explica como organizar a documentação no Google Docs para análise e elaboração do relatório final.

---

## 📋 ESTRUTURA SUGERIDA NO GOOGLE DOCS

### Opção 1: Um documento por fase

Crie documentos separados no Google Drive:

```
📁 Trabalho Probabilidade - Documentação/
├── 📄 00_INDICE_GERAL
├── 📄 01_FASE_1_Modelo_Matematico
├── 📄 02_FASE_2_Experimento_1
├── 📄 03_FASE_3_Experimento_2
├── 📄 04_FASE_4_Experimento_3
├── 📄 05_FASE_5_Experimento_4
├── 📄 06_FASE_6_Experimento_5
├── 📄 07_FASE_7_Integracao
└── 📄 99_RELATORIO_RASCUNHO
```

**Vantagens:**
- Fácil de navegar
- Cada fase isolada
- Pode compartilhar fase específica
- Menos pesado para editar

### Opção 2: Um único documento com seções

Crie um único documento com sumário automático:

```
📄 Trabalho I - Documentação Completa
  ├─ Sumário (gerado automaticamente)
  ├─ 1. Índice Geral
  ├─ 2. Fase 1 - Modelo Matemático
  ├─ 3. Fase 2 - Experimento 1
  ├─ ... (demais fases)
  └─ 99. Rascunho do Relatório
```

**Vantagens:**
- Tudo em um lugar
- Busca unificada (Ctrl+F)
- Fácil copiar/colar para relatório
- Histórico de versão único

---

## 🔄 PROCESSO DE TRABALHO RECOMENDADO

### A cada fase concluída:

1. **Copie o arquivo .md da fase** (ex: `FASE_1_DOCUMENTACAO.md`)
2. **Abra no editor de texto** (VS Code, Notepad++, etc.)
3. **Cole no Google Docs** (cria novo ou adiciona seção)
4. **Formate no Google Docs:**
   - Aplique estilos de título (Título 1, 2, 3)
   - Ajuste tabelas se necessário
   - Adicione comentários e anotações
5. **Use para análise:**
   - Marque pontos importantes
   - Adicione observações suas
   - Destaque o que vai para o relatório

### Para o relatório final:

1. **Abra o documento "99_RELATORIO_RASCUNHO"**
2. **Copie seções das fases** conforme estrutura:
   - Contexto e objetivos
   - Modelo e conceitos (da Fase 1)
   - Cinco experimentos (das Fases 2-6)
   - Discussão crítica
3. **Edite e sintetize:**
   - Remova detalhes técnicos excessivos
   - Mantenha interpretações e conceitos
   - Adicione gráficos e tabelas
4. **Mantenha referências** aos documentos originais

---

## 📊 SEÇÕES ESSENCIAIS PARA O GOOGLE DOCS

### Para cada fase, destaque:

#### 1. Resumo Executivo (início)
- O que foi feito
- Principais resultados
- Status de validação

#### 2. Valores Teóricos/Observados (tabelas)
- Copie as tabelas formatadas
- Adicione notas se necessário
- Marque divergências

#### 3. Notas para o Relatório (seção específica)
- Conceitos demonstrados
- Interpretações prontas
- Discussões sugeridas

#### 4. Gráficos e Tabelas
- **No Google Docs:** Insira as imagens dos gráficos
- **Referência:** Mantenha caminho do arquivo original
- **Legenda:** Copie do documento markdown

#### 5. Checklist de Conformidade
- Use checkboxes do Google Docs
- Marque conforme validação
- Anote pendências

---

## 🎨 DICAS DE FORMATAÇÃO NO GOOGLE DOCS

### Hierarquia de títulos sugerida

```
Título (fonte 24pt, negrito)
  ├─ Título 1 (fonte 18pt, negrito)
  │    └─ Título 2 (fonte 14pt, negrito)
  │         └─ Título 3 (fonte 12pt, negrito, itálico)
  └─ Normal (fonte 11pt)
```

### Estilos recomendados

| Elemento | Estilo no Google Docs |
|----------|----------------------|
| Título da fase | Título + cor destaque |
| Seção principal | Título 1 |
| Subseção | Título 2 |
| Item específico | Título 3 |
| Código/fórmula | Fonte monoespaçada (Courier New) |
| Destaque | Negrito ou cor de fundo |
| Nota importante | Cor de texto vermelho/laranja |

### Para tabelas

1. **Copie a tabela** do markdown
2. **Cole no Google Docs** (pode perder formatação)
3. **Ajuste:**
   - Formato da tabela → Bordas
   - Cabeçalho em negrito
   - Linhas alternadas (opcional)
4. **Alinhamento:**
   - Texto: esquerda
   - Números: direita
   - Status: centro

### Para fórmulas matemáticas

**Opção A:** Use o editor de equações do Google Docs
- Inserir → Equação
- Digite usando LaTeX ou interface

**Opção B:** Mantenha como texto simples
- E[P] = 0.84
- E[X] = -0.16
- RTP = 84%

**Opção C:** Insira como imagem
- Gere a fórmula em LaTeX
- Exporte como PNG
- Insira no documento

---

## 📝 TEMPLATE PARA ANOTAÇÕES

Para cada seção no Google Docs, adicione uma caixa de comentário:

### 🔍 ANÁLISE (use comentários do Google Docs)

```
💡 Para o relatório:
- [ ] Incluir este conceito
- [ ] Simplificar explicação
- [ ] Adicionar exemplo

⚠️ Pendências:
- [ ] Verificar valor X
- [ ] Conferir interpretação Y

📌 Observações:
- Ponto importante para discussão
- Relacionar com experimento Z
```

---

## 🗂️ ORGANIZAÇÃO DE ARQUIVOS EXTERNOS

### Crie pastas no Google Drive paralelas:

```
📁 Trabalho Probabilidade/
├─ 📁 01_Documentacao/       ← Docs com texto
├─ 📁 02_Graficos/            ← Imagens dos gráficos
├─ 📁 03_Tabelas_CSV/         ← CSVs dos experimentos
├─ 📁 04_Codigo_Fonte/        ← Backup do código (opcional)
└─ 📁 05_Relatorio_Final/     ← Versões do relatório PDF
```

**No Google Docs, referencie:**
- "Gráfico disponível em: 02_Graficos/experimento1.png"
- "Dados completos em: 03_Tabelas_CSV/experimento1.csv"

---

## 🔖 SISTEMA DE TAGS/MARCADORES

Use cores de destaque no Google Docs:

| Cor | Significado |
|-----|------------|
| 🟡 Amarelo | Para revisar/confirmar |
| 🟢 Verde | Validado e pronto |
| 🔴 Vermelho | Pendente/bloqueado |
| 🔵 Azul | Para incluir no relatório |
| 🟣 Roxo | Discussão crítica |

---

## 📤 EXEMPLO DE FLUXO COMPLETO

### Dia 1 - Fase 1 concluída:

1. ✅ Abra `FASE_1_DOCUMENTACAO.md`
2. ✅ Copie todo o conteúdo
3. ✅ Cole no Google Docs "01_FASE_1_Modelo_Matematico"
4. ✅ Formate títulos e tabelas
5. ✅ Adicione comentário: "Valores teóricos validados!"
6. ✅ Marque seção "Notas para Relatório" em azul
7. ✅ Atualize o índice geral

### Dia 2 - Análise:

1. 📖 Leia a documentação no Google Docs
2. 📝 Adicione comentários com dúvidas
3. 🎯 Destaque pontos para o relatório
4. ✏️ Rascunhe interpretações no doc "99_RASCUNHO"
5. ✅ Marque itens do checklist conforme valida

### Semana final - Relatório:

1. 📄 Abra o rascunho do relatório
2. 📋 Copie seções dos docs de cada fase
3. ✂️ Edite e sintetize (6-10 páginas)
4. 🖼️ Insira gráficos da pasta 02_Graficos
5. 📊 Referência os CSVs da pasta 03_Tabelas
6. 🔍 Revise com os checklists das fases
7. 📤 Exporte para PDF

---

## 🎯 ATALHOS DO GOOGLE DOCS ÚTEIS

| Ação | Atalho |
|------|--------|
| Adicionar comentário | Ctrl + Alt + M |
| Buscar | Ctrl + F |
| Substituir | Ctrl + H |
| Inserir link | Ctrl + K |
| Aplicar Título 1 | Ctrl + Alt + 1 |
| Aplicar Título 2 | Ctrl + Alt + 2 |
| Sumário automático | Inserir → Índice |
| Contar palavras | Ferramentas → Contar palavras |

---

## ✅ CHECKLIST GERAL

### Após cada fase:
- [ ] Copiei documentação para Google Docs
- [ ] Formatei títulos e tabelas
- [ ] Adicionei comentários relevantes
- [ ] Destaquei pontos para o relatório
- [ ] Atualizei o índice geral
- [ ] Salvei gráficos na pasta correta

### Ao final do projeto:
- [ ] Todas as fases documentadas
- [ ] Todos os gráficos inseridos
- [ ] Relatório rascunhado
- [ ] Checklists completados
- [ ] README pronto
- [ ] Todos os arquivos organizados

---

## 💡 DICA FINAL

**Mantenha dois ambientes:**

1. **Documentação técnica completa** (Google Docs)
   - Todos os detalhes
   - Todos os testes
   - Todos os valores
   - Para consulta e validação

2. **Relatório final** (Google Docs separado)
   - Síntese de 6-10 páginas
   - Apenas o essencial
   - Formatação para PDF
   - Para entrega

**O primeiro alimenta o segundo!**

---

**Bom trabalho! 🚀**
