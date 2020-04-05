n = int(input())

s = ' that I '.join(('hate', 'love')[i%2] for i in range(n))

print(f'I {s} it')
