n = int(input())
cities = input()

print(('NO', 'YES')[cities[0] == 'S' and cities[-1] == 'F'])
