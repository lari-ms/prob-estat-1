"""
Script ESSENCIAL para testar a base implementada na Fase 1
Execute este arquivo para validar que tudo está funcionando
"""

from src.maquina import executar_rodadas, TABELA_BASE
from src.calculos import validar_valores_teoricos_tabela_base, obter_valores_teoricos_referencia

print("=" * 70)
print("TESTE DA BASE - FASE 1")
print("=" * 70)
print()

# Teste 1: Validação matemática
print("1. Validando valores teóricos...")
ok, msg = validar_valores_teoricos_tabela_base()
if ok:
    print("   ✓ Valores matemáticos corretos!")
else:
    print(f"   ✗ ERRO: {msg}")
    exit(1)

# Teste 2: Executar 10 rodadas
print("\n2. Executando 10 rodadas (semente 2026)...")
resultados = executar_rodadas(10, semente=2026)
print(f"   ✓ {len(resultados)} rodadas executadas")

# Teste 3: Verificar rodada específica
print("\n3. Verificando rodada 3 (deve ser A-A-A)...")
r3 = resultados[2]  # índice 2 = rodada 3
if r3['linha_central'] == ('A', 'A', 'A') and r3['premio'] == 5 and r3['lucro'] == 4:
    print(f"   ✓ Rodada 3: {r3['linha_central']}, prêmio={r3['premio']}, lucro={r3['lucro']}")
else:
    print(f"   ✗ ERRO: Rodada 3 incorreta!")
    print(f"   Esperado: ('A', 'A', 'A'), premio=5, lucro=4")
    print(f"   Obtido: {r3['linha_central']}, premio={r3['premio']}, lucro={r3['lucro']}")
    exit(1)

# Teste 4: Mostrar resumo
print("\n4. Resumo das 10 rodadas:")
lucros = [r['lucro'] for r in resultados]
media = sum(lucros) / len(lucros)
premios = sum(1 for r in resultados if r['premio'] > 0)
print(f"   Lucro médio: {media:.2f} créditos")
print(f"   Rodadas premiadas: {premios}/10")

# Teste 5: Valores teóricos
print("\n5. Valores teóricos de referência:")
valores = obter_valores_teoricos_referencia()
print(f"   E[P] = {valores['esperanca_premio']:.2f} créditos")
print(f"   E[X] = {valores['esperanca_lucro']:.2f} créditos")
print(f"   RTP = {valores['rtp']*100:.1f}%")
print(f"   P(prêmio) = {valores['prob_premio']*100:.1f}%")

print()
print("=" * 70)
print("✓ TODOS OS TESTES PASSARAM!")
print("✓ BASE ESTÁ PRONTA PARA OS EXPERIMENTOS")
print("=" * 70)
