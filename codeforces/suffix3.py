t = int(input())

for sentence in [input() for _ in range(t)]:
    if sentence.endswith('po'):
        print('FILIPINO')
    elif sentence.endswith('mnida'):
        print('KOREAN')
    else:
        print('JAPANESE')
