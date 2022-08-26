print("------------------------")
print(" ESCOLA JAVALI CANSADO ")
print("------------------------")
print('''[1] RESULTADO PROVAS
[2] SAIR''')
escolha = str(input("Escolha uma opção:"))
if "1" in escolha:
    nota1 = float(input("Digite a primeira nota:"))
    nota2 = float(input("Digite a segunda nota:"))
    media = (nota1 + nota2) / 2
    print("------------------------")
    if media >=0 and media < 2:
        print("MÉDIA:", media)
        print("APROVEITAMENTO: F")
        print("REPROVADO")
        print("------------------------")
    else:
        if (media > 2) and (media <= 4):
            print("MÉDIA:", media)
            print("APROVEITAMENTO: E")
            print("REPROVADO")
            print("------------------------")
        else:
            if (media > 4) and (media <= 6):
                print("MÉDIA:", media)
                print("APROVEITAMENTO: D")
                print("RECUPERAÇÃO")
                print("------------------------")
            else:
                if (media > 6) and (media <= 7):
                    print("MÉDIA:", media)
                    print("APROVEITAMENTO: C")
                    print("APROVADO")
                    print("------------------------")
                else:
                    if (media > 7) and (media <= 9):
                        print("MÉDIA:", media)
                        print("APROVEITAMENTO: B")
                        print("APROVADO")
                        print("------------------------")
                    else:
                        if (media > 9):
                            print("MÉDIA:", media)
                            print("APROVEITAMENTO: A")
                            print("APROVADO")
                            print("------------------------")
if "2" in escolha:
    print("OBRIGADO POR ESTUDAR NA JAVALI CANSADO")
