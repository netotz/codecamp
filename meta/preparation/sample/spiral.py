'''
create a matrix n*n of zeroes
matrix[0][0] = 1
i = 0
j = 0
x = 2
lower = 0
upper = n - 1
direction = 1
# O(n**2)
while True:
    if lower >= upper:
        break

    if direction == 1:
        if j == upper:
            direction = 2
            continue
        j += 1
    elif direction == 2:
        if i == upper:
            direction = 3
            continue
        i += 1
    elif direction == 3:
        if j == low:
            direction = 4
            continue
        j -= 1
    elif direction == 4:
        if i == low + 1:
            direction = 1
            low += 1
            upper -= 1
            continue
        i -= 1
    
    matrix[i][j] = x
    x += 1

return matrix

n = 2
matrix =
    [[0, 0]
     [0, 0]]
matrix =
    [[1, 0]
     [0, 0]]
i = 0
j = 0
x = 2
lower = 0
upper = 1
direction = 1
0 = 1? no
    j = 1
matrix =
    [[1, 2]
     [0, 0]]
x = 3
1 = 1? yes
    direction = 2
0 = 1? no
    i = 1
x = 4
1 = 1? yes
    direction = 3
1 = 0? no
    j = 0
matrix =
    [[1, 2]
     [4, 3]]
x = 5
0 = 0? yes
    direction = 4
1 = 1? yes
    direction = 1
    low = 1
    upper = 0
'''


def spiral(n: int) -> list[list[int]]:
    matrix = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]
    matrix[0][0] = 1
    i = 0
    j = 0
    x = 2
    lower = 0
    upper = n - 1
    direction = 1

    # O(n**2)
    while True:
        if lower > upper:
            break

        if direction == 1:
            if j == upper:
                direction = 2
                continue
            j += 1
        elif direction == 2:
            if i == upper:
                direction = 3
                continue
            i += 1
        elif direction == 3:
            if j == lower:
                direction = 4
                continue
            j -= 1
        elif direction == 4:
            if i == lower + 1:
                direction = 1
                lower += 1
                upper -= 1
                continue
            i -= 1
        
        matrix[i][j] = x
        x += 1

        if x == (n * n) + 1:
            break

    return matrix

