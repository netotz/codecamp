'''
Counting Triangles
Given a list of N triangles with integer side lengths, determine how many different triangles there are. Two triangles are considered to be the same if they can both be placed on the plane such that their vertices occupy exactly the same three points.

Signature
int countDistinctTriangles(ArrayList<Sides> arr)
or 
int countDistinctTrianges(int[][] arr)

Input
In some languages, arr is an Nx3 array where arr[i] is a length-3 array that contains the side lengths of the ith triangle. In other languages, arr is a list of structs/objects that each represent a single triangle with side lengths a, b, and c.
It's guaranteed that all triplets of side lengths represent real triangles.
All side lengths are in the range [1, 1,000,000,000]
1 <= N <= 1,000,000

Output
Return the number of distinct triangles in the list.

Example 1
arr = [[2, 2, 3], [3, 2, 2], [2, 5, 6]]
output = 2
The first two triangles are the same, so there are only 2 distinct triangles.
Example 2
arr = [[8, 4, 6], [100, 101, 102], [84, 93, 173]]
output = 3
All of these triangles are distinct.
Example 3
arr = [[5, 8, 9], [5, 9, 8], [9, 5, 8], [9, 8, 5], [8, 9, 5], [8, 5, 9]]
output = 1
All of these triangles are the same.
---

triangles can be placed anywhere to see if vertices overlap,
no coordinates, so they can be rotated too,
in other words for 2 triangles to be equal, both must have the same side lengths
remove duplicated triangles and return resulting size

iterate array, O(n)
    sort current subarray, O(1)
    iterate rest of array, O(n)
        sort current subarray,
        compare each side,
        if equal, decrement counter
return counter
time O(n**2)

[[2, 2, 3], [3, 2, 2], [2, 5, 6]]
curr1 = [2, 2, 3]
    curr2 = [2, 5, 6]
c = 2
---

iterate array, O(n)
    sort current subarray, O(3 log 3)
    convert it to string, O(3)
    add it to set
return length of set
time O(n)

[[2, 2, 3], [3, 2, 2], [2, 5, 6]]
s = {"2,2,3", "2,5,6"}
'''


def countDistinctTriangles(arr) -> int:
    '''
    Time O(n)
    
    Space O(n)
    '''
    # O(n)
    return len({
        tuple(sorted(triangle))
        for triangle in arr
    })


def countDistinctTriangles_brute(arr) -> int:
    '''
    Time O(n**2)

    Space O(1)
    '''
    count = len(arr)
    # O(n**2)
    for i in range(len(arr)):
        itriangle = sorted(arr[i])

        # O(n)
        for j in range(i + 1, len(arr)):
            jtriangle = sorted(arr[j])

            is_equal = all(
                itriangle[s] == jtriangle[s]
                for s in range(3)
            )
            if is_equal:
                count -= 1

    return count
