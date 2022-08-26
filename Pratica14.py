toth = 0
totm = 0
r = ""
print("====================")
print(" SELETOR DE PESSOAS ")
print("====================")
while True:
    s = str(input("Informe o sexo: [M/F]")).upper().strip()
    i = int(input("Informe a idade:"))
    print("Qual é a cor do cabelo?")
    print("====================")
    print("[1] Preto")
    print("[2] Castanho")
    print("[3] Loiro")
    print("[4] Ruivo")
    c = int(input("Escolha:"))
    if s == "M" and i > 18 and c == 2:
        toth = toth + 1
    else:
        if s == "F" and i >= 25 and i <= 30 and c == 3:
            totm = totm + 1
    r = str(input("Quer continuar? [S/N]")).strip().upper()
    if r == "N":
        break
print(f"Total de homens com mais de 18 anos e cabelos  castanhos: {toth}")
print(f"Total de mulheres entre 25 e 30 anos e cabelos  loiros: {totm}")