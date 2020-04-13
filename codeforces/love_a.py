s = input()
a = s.count('a')

print(a + (a - 1) if a <= len(s) // 2 else len(s))
