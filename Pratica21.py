s = 0
div = 0
nulo = 0
p = 0
totp = 0
for c in range(0, 5):
    n = int(input("Digite um número:"))
    s = s + n
    if n % 5 == 0:
        div = div + 1
    if n == 0:
        nulo = nulo + 1
    if n % 2 == 0:
        p = p + 1
        totp = totp + n
print(f"A soma entre os valores é: {s}")
m = s / 5
print(f"A média entre os valores é {m}")
print(f"Números divisíveis por 5: {div}")
print(f"Valores nulos: {nulo}")
print(f" Números pares: {p}")
print(f"Soma dos números pares: {totp}")
