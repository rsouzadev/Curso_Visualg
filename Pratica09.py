totn = 0
for c in range(1,6):
    n = int(input("Digite um número por favor:"))
    if n < 0:
        totn = totn + 1
print(f"Foram encontrados {totn} números negativos.")