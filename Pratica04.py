contador = 1
soma = 0
while contador <= 10:
    num = int(input(f"Informe o {contador} número:"))
    contador = contador + 1
    soma = soma + num
print(f"O total deu: {soma}")