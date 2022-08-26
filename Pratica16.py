TOTP = 0
num = int(input("Digite um valor:"))

for c in range(1,num+1,1):
    print(c)
    if c % 2 == 0:
        TOTP = TOTP + 1
print(f"Ao todo temos {TOTP} números pares.")