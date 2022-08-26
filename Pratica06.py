quantidade = int(input("Quantas vezes você quer converter seu dinheiro?"))
contador = 1

while contador <= quantidade:
    valor_real = float(input("Informe o valor em R$:"))
    conversao = (valor_real / 5.74)
    print(f'VALOR EM US$:{conversao:.2f}')
    contador = contador + 1