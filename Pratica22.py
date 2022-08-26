import os
N = " "
M = 0
P = 0
PES = " "

print("==================================")
print("D E T E C T O R  D E  P E S A D O ")
print(f"Maior peso até agora: {M} Kg")
print("==================================")
for contador in range(1, 6):
    N = str(input("Digite seu nome:"))
    P = float(input(f"Digite o peso de {N}:"))
    if P > M:
        M = P
        PES = N
    os.system('cls')
    print("==================================")
    print("D E T E C T O R  D E  P E S A D O ")
    print(f"Maior peso até agora: {M} Kg")
    print("==================================")
os.system('cls')
print("==================================")
print("D E T E C T O R  D E  P E S A D O ")
print(f"Maior peso até agora: {M} Kg")
print("==================================")
print(f"A pessoa mais pesada foi {PES} com {M} kilos.")





