'''
Minimum Length Substrings

You are given two strings s and t. You can select any substring of string s and rearrange the characters of the selected substring. Determine the minimum length of the substring of s such that string t is a substring of the selected substring.

Signature
int minLengthSubstring(String s, String t)

Input
s and t are non-empty strings that contain less than 1,000,000 characters each

Output
Return the minimum length of the substring of s. If it is not possible, return -1
Example
s = "dcbefebce"
t = "fd"
output = 5
Explanation:
Substring "dcbef" can be rearranged to "cfdeb", "cefdb", and so on. String t is a substring of "cfdeb". Thus, the minimum length required is 5.
---

inputs: strings
output: int

if s < t, not possible
map t to hashmap of occurrences
map of t initialized o 0

l = 0
for r from 0 to len(s), O(s)
    if char at r is in map,
        increment its count
        if count matches map of t,
            increment uniques
    else continue
    
    while uniques is size of map and l <= r,
        save length of curr subs if it's smaller than prev or no prev,
        
        if length of subs equals length of t, return
        
        if char at l is in map,
            decrement its count
            if count no longer matches map of t,
                decrement uniques
        l += 1
return length of subs

     l
s = "dcbefebce"
         r
t = "fd"
tm = {
  f: 1,
  d: 1
}
sm = {
  f: 1,
  d: 0
}
u = 1
x = 5
'''


from collections import Counter


def min_length_substring(s, t):
    if len(s) < len(t):
        return - 1
    
    # O(t)
    tmap = Counter(t)
    # O(t)
    subsmap = {char: 0 for char in tmap}
    
    uniques = 0
    subslen = float('inf')
    
    l = 0
    r = 0
    # O(s)
    while r < len(s):
        rchar = s[r]
        if rchar in tmap:
            subsmap[rchar] += 1
            if subsmap[rchar] == tmap[rchar]:
                uniques += 1
        
        while uniques == len(tmap) and l <= r:
            currlen = r - l + 1
            if currlen < subslen:
                subslen = currlen
                if subslen == len(t):
                    return subslen
            
            lchar = s[l]
            if lchar in tmap:
                subsmap[lchar] -= 1
                if subsmap[lchar] < tmap[lchar]:
                    uniques -= 1
            
            l += 1
        r += 1
    
    return subslen if subslen < float('inf') else -1
