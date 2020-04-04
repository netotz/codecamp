n = int(input())
opinions = map(int, input().split())

is_easy = True
for o in opinions:
    if o == 1:
        print('HARD')
        is_easy = False
        break

if is_easy:
    print('EASY')
