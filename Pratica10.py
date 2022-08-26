f = 1
num = int(input("Digite um número:"))
for c in range(num,0,-1):
    #print(num, "x", c,"=", (num*c))
    f = f * c
print(f"O fatorial de {num} é {f}.")

