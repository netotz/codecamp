def join_sorteds(array1, array2):
    if array1[0] < array2[0]:
        lesser = array1
        greater = array2
    else:
        lesser = array2
        greater = array1
    while True:
        loop_again = False
        for i in range(len(lesser) - 1):
            for j in range(len(greater)):
                print(lesser[i] , greater[j] , lesser[i + 1])
                if lesser[i] <= greater[j] <= lesser[i + 1]:
                    lesser.insert(i + 1, greater[j])
                    greater.pop(j)
                    print(lesser, greater)
                    loop_again = True
                    break
                else:
                    break
            if loop_again:
                break
        if not loop_again:
            break
    if greater:
        lesser.extend(greater)
    return lesser


def test():
    assert join_sorteds([3, 4, 9, 9, 17, 20], [8, 9, 40, 41]) == [3, 4, 8, 9, 9, 9, 17, 20, 40, 41]
    assert join_sorteds([5, 6, 20], [2, 3, 4, 5]) == [2, 3, 4, 5, 5, 6, 20]
    assert join_sorteds([1, 3, 5, 7, 9], [2, 4, 6, 8]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert join_sorteds([14, 17, 18, 21, 22, 26], [3, 15, 30, 31]) == [3, 14, 15, 17, 18, 21, 22, 26, 30, 31]
    assert join_sorteds([3, 4, 6, 9, 11, 16, 17], [8, 9, 9, 40]) == [3, 4, 6, 8, 9, 9, 9, 11, 16, 17, 40]
