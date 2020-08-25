# Given an array of integers, determine whether the array is monotonic or not.
# An array is monotonic if it is either monotone increasing or monotone decreasing.

def is_monotonic(array):
    increasing = False
    for i in range(len(array) - 2):
        dif = array[i + 1] - array[i]
        if dif != 0:
            increasing = dif > 0
            break

    for j in range(i + 1, len(array) - 1):
        dif = array[j + 1] - array[j]
        if increasing:
            if dif < 0:
                return False
        else:
            if dif > 0:
                return False
    return True

def better_solution(array):
    increasing = (array[i] <= array[i + 1] for i in range(len(array) - 1))
    decreasing = (array[i] >= array[i + 1] for i in range(len(array) - 1))
    return all(increasing) or all(decreasing)

test = list(map(int, input().split()))
print(is_monotonic(test))
print(better_solution(test))
