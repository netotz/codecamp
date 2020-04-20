x = int(input())

steps = 0
for move in (5, 4, 3, 2, 1):
    n = x // move
    steps += n
    x -= n * move
    if not x:
        break

print(steps)
