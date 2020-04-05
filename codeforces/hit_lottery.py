n = int(input())

bills = 0
for d in (100, 20, 10, 5, 1):
    b = n // d
    n -= d * b
    bills += b
    if not n:
        break

print(bills)
