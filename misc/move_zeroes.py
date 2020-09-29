#Given an array nums, write a function to move all zeroes to the end of it while maintaining the relative order of 
#the non-zero elements.

# faster
def move_zeroes(array):
    nonzeroes = [num for num in array if num != 0]
    return nonzeroes + [0] * array.count(0)

# solution by problem publisher
def page_solution(nums):
    for i in nums:
        if 0 in nums:
            nums.remove(0)
            nums.append(0)
    return nums

array = list(map(int, input().split()))
print(move_zeroes(array))
