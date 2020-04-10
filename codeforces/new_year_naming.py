n, m = map(int, input().split())
sstr = input().split()
tstr = input().split()
q = int(input())

for y in [int(input()) for _ in range(q)]:
    s = (y % n) - 1
    t = (y % m) - 1
    print(sstr[s] + tstr[t])
