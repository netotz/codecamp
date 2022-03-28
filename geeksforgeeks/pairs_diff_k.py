'''
https://practice.geeksforgeeks.org/problems/count-distinct-pairs-with-difference-k1233/1/#
'''


class Solution:
    def TotalPairs(self, nums, k: int) -> int:
        if len(nums) == 0:
            return 0

        hashmap = dict()
        # O(n)
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        
        count = 0
        # O(n)
        for num in hashmap:
            if k == 0:
                if hashmap[num] > 1:
                    count += 1
                continue

            diff = num - k
            if diff in hashmap:
                count += 1

        return count
