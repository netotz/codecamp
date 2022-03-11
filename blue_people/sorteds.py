def join_sorteds(array1, array2):
    i = 0
    j = 0
    merged = list()
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            merged.append(array1[i])
            i += 1
        else:
            merged.append(array2[j])
            j += 1
    merged += array1[i:] if i < len(array1) else array2[j:]
    return merged


def test():
    assert join_sorteds([3, 4, 9, 9, 17, 20], [8, 9, 40, 41]) == [3, 4, 8, 9, 9, 9, 17, 20, 40, 41]
    assert join_sorteds([5, 6, 20], [2, 3, 4, 5]) == [2, 3, 4, 5, 5, 6, 20]
    assert join_sorteds([1, 3, 5, 7, 9], [2, 4, 6, 8]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert join_sorteds([14, 17, 18, 21, 22, 26], [3, 15, 30, 31]) == [3, 14, 15, 17, 18, 21, 22, 26, 30, 31]
    assert join_sorteds([3, 4, 6, 9, 11, 16, 17], [8, 9, 9, 40]) == [3, 4, 6, 8, 9, 9, 9, 11, 16, 17, 40]
