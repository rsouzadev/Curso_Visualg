print("CONTAGEM INTELIGENTE")
print("====================")
inicio = int(input("Início:"))
final = int(input("Final:"))
print("====================")
print("      CONTANDO      ")
print("====================")
contador = inicio
if inicio < final:
    while contador <= final:
        print(contador,end="...")
        contador = contador + 1

else:
    if inicio > final:
        while contador >= final:
            print(contador,end="...")
            contador = contador - 1



