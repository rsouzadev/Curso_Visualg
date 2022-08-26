totp = 0
for c in range(1, 6, 1):
    n = int(input("Digite um número:"))
    if n % 2 == 0:
        totp = totp+1

print(f" Total dos números pares: {totp}")
