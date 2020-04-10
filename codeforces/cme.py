q = int(input())
for n in [int(input()) for _ in range(q)]:
    buy = n if n == 2 else n % 2
    print(buy)
