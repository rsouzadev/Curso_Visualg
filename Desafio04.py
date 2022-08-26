print("SÃO PAULO X PALMEIRAS")
print("======================")
sampa = int(input("Quantos gols do SAMPA?"))
parma = int(input("Quantos gols do PARMA?"))
print("======================")
diferenca: int = (sampa - parma) * (-1)
print("DIFERENÇA: ", diferenca)
if diferenca == 0:
    print("STATUS: EMPATE")
else:
    if diferenca == 1:
        print("STATUS: NORMAL")
    else:
        if diferenca == 2:
            print("STATUS: NORMAL")
        else:
            if diferenca == 3:
                print("STATUS: GOLEADA")
            else:
                if diferenca > 3:
                    print("STATUS: CHOCOLATE!")



