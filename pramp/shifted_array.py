'''
https://www.pramp.com/challenge/N5LYMbYzyOtbpovQoYPX
'''


def find_index_smallest(array: list[int]) -> int:
    '''
    Finds and returns the index of the smallest number in the shifted array
    using binary search.

    Time O(log n)
    '''
    l = 0
    r = len(array) - 1

    while l <= r:
        mid = (l + r) // 2
        if mid == 0 or array[mid] < array[mid - 1]:
            return mid

        if array[mid] > array[0]:
            l = mid + 1
        else:
            r = mid - 1
    return -1


def find_index_of(array: list[int], number: int, l: int, r: int) -> int:
    '''
    Finds and returns the index of `number` using binary search.

    Time O(log n)
    '''
    while l <= r:
        mid = (l + r) // 2
        if array[mid] == number:
            return mid

        if array[mid] < number:
            # search right side
            l = mid + 1
        else:
            # search left side
            r = mid - 1
    return -1


def shifted_arr_search(shiftArr: list[int], num: int) -> int:
    '''
    Time O(log n)
    
    Space O(1)
    '''
    if len(shiftArr) == 0:
        return False

    if shiftArr[0] <= shiftArr[-1]:
        return find_index_of(shiftArr, num, 0, len(shiftArr) - 1)
  
    # O(log n)
    offset = find_index_smallest(shiftArr)
    if offset < 0:
        return False

    if num < shiftArr[0]:
        l = offset
        r = len(shiftArr) - 1
    else:
        l = 0
        r = offset - 1
  
    # O(log n)
    return find_index_of(shiftArr, num, l, r)
