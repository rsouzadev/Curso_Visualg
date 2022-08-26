contador = 1
soma = 0
maior_num = 0
while contador <= 10:
    num = int(input(f"Informe o {contador} número:"))
    if num > maior_num:
        maior_num = num
    contador = contador + 1
    soma = soma + num
print(f"O total deu: {soma}")
print(f'O maior número:{maior_num}')