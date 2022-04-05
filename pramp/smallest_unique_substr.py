'''
https://www.pramp.com/challenge/wqNo9joKG6IJm67B6z34
---

unique chars

iterate string, O(s)
    use empty set to keep track of unique chars,
    iterate rest of string, O(s),
        if char in arr, add it to set
        when set has all uniques, then current substring is valid, so:
            update shortest substring,
            if shortest has same length of arr, return shortest
            else break inner loop, because next substrings are also valid but larger
return shortest

total time O(s**2 + a)

this solution is duplicating work by iterating the rest of the string multiple times,
and by emptying the set at every outer iteration.
when a substring is valid, instead of resetting the inner loop, the outer one can advance until meeting the inner,
as if it were following it, because substrings of current substring could be valid too, and they'd be shorter.
in this case the worst case would be traversing the whole string forward, then again but backwards.

in order to check if current substrings are valid without resetting the set,
a hash map can be used to count each unique char in current substring,
while counting how many unique chars have been seen.
a substring would then be valid if this count equals the number of unique chars.

map unique chars to 0
iterate string with 2 pointers, starting at 0, O(s)
    if char at right pointer is in arr,
        and it's the first time seeing it,
            increment count of unique chars,
        then increment its count
    
    while count of unique chars equals total uniques,
        update shortest,
        decrement count of char at left pointer,
        if it's 0, decrement count of unique chars
        advance left pointer
    advance right pointer
return shortest

total time O(s + a)

        l
str = "xyyzyzyx"
              r
u = 3
shor = 4

arr = [A]
       l
str = "A"
       r
u = 1
'''


def get_shortest_unique_substring(arr, string):
    '''
    Time O(s + a)
    
    Space O(a)
    '''
    if len(string) < len(arr):
        return ""

    # save indexes and length of shortest substring
    # instead of actual substring as slicing is by copy
    start = -1
    end = -1
    shortest_len = float('inf')
    # a deque could also be used
    
    # O(a)
    uniques_map = {c: 0 for c in arr}
    uniques = 0

    left = 0
    right = 0
    # O(2s)
    while right < len(string):
        rchar = string[right]
        if rchar in uniques_map:
            if uniques_map[rchar] == 0:
                uniques += 1
            uniques_map[rchar] += 1
        
        # O(s[l:r])
        while uniques == len(arr) and left <= right:
            substr_len = right - left + 1
            
            if substr_len < shortest_len:
                start = left
                end = right
                shortest_len = substr_len

                if shortest_len == uniques:
                    return string[start:end + 1]
        
            lchar = string[left]
            if lchar in uniques_map and uniques_map[lchar] > 0:
                uniques_map[lchar] -= 1

                if uniques_map[lchar] == 0:
                    uniques -= 1

            left += 1
        right += 1
    
    return string[start:end + 1] if shortest_len < float('inf') else ""


def get_shortest_substring_brute(arr, string):
    '''
    Time O(s**2)
    
    Space O(a)
    '''
    start = -1
    end = -1
    shortest_len = float('inf')

    # O(a)
    uniques_set = set(arr)

    # O(s**2)
    for i in range(len(string)):
        curr_uniques = set()
        # O(s)
        for j in range(i, len(string)):
            char = string[j]

            if char in uniques_set:
                curr_uniques.add(char)
            
            substr_len = j - i + 1
            if len(curr_uniques) == len(arr) and substr_len < shortest_len:
                start = i
                end = j
                shortest_len = substr_len

                if shortest_len == len(arr):
                    return string[start:end + 1]
                break
                
    return string[start:end + 1] if shortest_len < float('inf') else ""
