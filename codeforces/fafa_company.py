n = int(input())

ways = 1
for l in range(2, (n // 2) + 1):
    if not n % l:
        ways += 1

print(ways)
