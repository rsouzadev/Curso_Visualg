TOTN = 0
TOTI = 0
for cont in range(0,6,1):
    v = int(input("Type a number:"))
    if (v >= 0) and (v <= 10):
        TOTN = TOTN+1

    if v % 2 == 1:
        TOTI = TOTI + v
print(f"We have {TOTN} numbers among 0 and 10.")
print(f"The total of the even numbers are {TOTI}.")