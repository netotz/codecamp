'''
Passing Yearbooks
There are n students, numbered from 1 to n, each with their own yearbook. They would like to pass their yearbooks around and get them signed by other students.
You're given a list of n integers arr[1..n], which is guaranteed to be a permutation of 1..n (in other words, it includes the integers from 1 to n exactly once each, in some order). The meaning of this list is described below.
Initially, each student is holding their own yearbook. The students will then repeat the following two steps each minute: Each student i will first sign the yearbook that they're currently holding (which may either belong to themselves or to another student), and then they'll pass it to student arr[i-1]. It's possible that arr[i-1] = i for any given i, in which case student i will pass their yearbook back to themselves. Once a student has received their own yearbook back, they will hold on to it and no longer participate in the passing process.
It's guaranteed that, for any possible valid input, each student will eventually receive their own yearbook back and will never end up holding more than one yearbook at a time.
You must compute a list of n integers output, whose element at i-1 is equal to the number of signatures that will be present in student i's yearbook once they receive it back.

Input
n is in the range [1, 100,000].
Each value arr[i] is in the range [1, n], and all values in arr[i] are distinct.

Output
Return a list of n integers output, as described above.

Example 1
n = 2
arr = [2, 1]
output = [2, 2]
Pass 1:
Student 1 signs their own yearbook. Then they pass the book to the student at arr[0], which is Student 2.
Student 2 signs their own yearbook. Then they pass the book to the student at arr[1], which is Student 1.
Pass 2:
Student 1 signs Student 2's yearbook. Then they pass it to the student at arr[0], which is Student 2.
Student 2 signs Student 1's yearbook. Then they pass it to the student at arr[1], which is Student 1.
Pass 3:
Both students now hold their own yearbook, so the process is complete.
Each student received 2 signatures.

Example 2
n = 2
arr = [1, 2]
output = [1, 1]
Pass 1:
Student 1 signs their own yearbook. Then they pass the book to the student at arr[0], which is themself, Student 1.
Student 2 signs their own yearbook. Then they pass the book to the student at arr[1], which is themself, Student 2.
Pass 2:
Both students now hold their own yearbook, so the process is complete.
Each student received 1 signature.
'''

# when a student start passing her yearbook,
# she starts a cycle in which next students will keep passing it
# until she has it again.
# All the students that conform a cycle will have the same amount of signatures.
# The student who started its cycle is the 'root' of the rest.
# So if we have the amount of signatures of the root of a cycle,
# we have it too for the rest of the students in that cycle,
# therefore we don't have to count it for them if we already know
# their root.
# By doing this each student will be 'visited' only once.


import pytest


def findSignatureCounts(arr: list[int]) -> list[int]:
    '''
    O(n)
    '''
    signatures = [0] * len(arr)
    # root indexes, students who started a cycle
    roots = [0] * len(arr)
    # visited indexes in previous cycles
    # to skip their counting
    visiteds = [False] * len(arr)

    # O(n)
    for i in range(len(arr)):
        # if student at i was already visited
        if visiteds[i]:
            continue

        visiteds[i] = True

        j = -1
        student = arr[i]
        # increment signatures for current student
        # before she receives her own yearbook
        while j != i:
            # sign current yearbook
            signatures[i] += 1
            # student will send current yearbook to student at next index j
            j = student - 1
            # next index is being visited
            visiteds[j] = True
            # root of next index is current index,
            # because current is part of the cycle
            roots[j] = i
            # next student at j
            student = arr[j]
    
    # set signatures of yearbooks that weren't explored
    # because they had a root
    # O(n)
    for i in range(len(signatures)):
        if roots[i] > -1:
            signatures[i] = signatures[roots[i]]
    
    return signatures


@pytest.mark.parametrize(
    ('array', 'signatures'), (
        ([2, 1], [2, 2]),
        ([1, 2], [1, 1]),
        ([2, 4, 3, 1], [3, 3, 1, 3]),
        ([4, 3, 2, 1], [2, 2, 2, 2]),
        ([4, 3, 2, 5, 1], [3, 2, 2, 3, 3]),
        ([5, 2, 4, 3, 1], [2, 1, 2, 2, 2]),
        ([4, 2, 3, 1], [2, 1, 1, 2]),
        ([1, 2, 3, 4], [1, 1, 1, 1]),
        ([1], [1]),
        ([3, 2, 4, 1], [3, 1, 3, 3])
    )
)
def test(array, signatures):
    assert findSignatureCounts(array) == signatures
