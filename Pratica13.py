print("====================")
print("|      MENU        |")
print("====================")
print("| [1] De 1 à 10    |")
print("| [2] De 10 à 1    |")
print("| [3]   SAIR       |")
print("====================")

escolha = ""
while escolha in "Ss":
    o = int(input("Qual é a sua opção?"))
    if o == 1:
        c = 1
        while c <=10:
            print(c)
            c = c+1

    else:
        if o == 2:
            c = 10
            while c>=1:
                print(c)
                c = c-1
        else:
            if o == 3:
                print("VOLTE SEMPRE!")
                break
    escolha = str(input("Quer continuar? [S/N]"))












