table = input()
hand = input().split()

if any(table[0] == c[0] or table[1] == c[1] for c in hand):
    print('YES')
else:
    print('NO')
