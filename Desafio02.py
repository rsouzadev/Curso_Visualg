print('=' *30)
print(f'{"   DEPARTAMENTO DE TRÂNSITO"}')
print('=' *30)
ano_atual = int(input("   Ano atual (yyyy):"))
nasc = int(input("   Ano de nascimento (yyyy):"))
idade = ano_atual - nasc
if idade >= 18:
    print("========== STATUS ==========")
    print("   IDADE:",idade)
    print("   APTO A DIRIGIR")
    print("============================")
else:
    print("========== STATUS ==========")
    print("   IDADE:", idade)
    print("   INAPTO A DIRIGIR")
    print("============================")