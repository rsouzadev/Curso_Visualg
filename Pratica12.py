c = 1
ContDiv = 0
num = int(input("Digite um número:"))
while c <= num:
    if num % c == 0:
        ContDiv = ContDiv + 1
    c = c + 1
if ContDiv > 2:
    print(f'O número {num} não é primo!')
else:
    print(f'O número {num} é primo!')



