limak, bob = map(int, input().split())

years = 1
while True:
    limak *= 3
    bob *= 2
    if limak > bob:
        break
    years += 1

print(years)
