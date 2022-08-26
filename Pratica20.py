#Sequencia de Fibonacci
n1 = 1
print(n1, end=" ")
n2 = 2
print(n2, end=" ")

for c in range(3,15,1):
    n3 = n1 + n2
    print(n3, end=" ")
    n1 = n2
    n2 = n3