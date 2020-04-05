n = int(input())

feelings = ' that '.join('I love' if i % 2 == 0 else 'I hate' for i in range(1, n + 1))

print(feelings, 'it')
