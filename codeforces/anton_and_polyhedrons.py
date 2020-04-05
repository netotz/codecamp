n = int(input())

faces = {
    'T': 4,
    'C': 6,
    'O': 8,
    'D': 12,
    'I': 20
}

print(sum(faces[input()[0]] for _ in range(n)))
