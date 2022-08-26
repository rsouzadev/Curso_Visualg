import os
resp =" "
while resp != "N":
    num = int(input("Digite um valor:"))
    cont = num
    fat = 1
    while cont > 0:
        fat = fat * cont
        cont = cont - 1
    print(f"O fatorial de {num} é {fat}.")
    resp = str(input("Quer continuar[S/N]")).strip().upper()
    os.system('cls')


