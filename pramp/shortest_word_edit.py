'''
target should be in words

                                      w
["but", "put", "big", "pot", "pog", "dog", "lot"]
t = 'dog'

w = 'pog'
s = {'bit', 'but', 'big', 'put', 'pot', 'pog'}
cq = [lot]
nq = []
l = 5
'''


from collections import deque

import pytest


def shortestWordEditPath(source: str, target: str, words: list[str]) -> int:
    '''
    BFS
    
    time O(wn**2), w = avg len of words

    space O(n)
    '''
    if source == target:
        return 0
      
    if len(source) != len(target):
        return -1

    # discard words with different length
    # O(n)
    wordset = {w for w in words if len(w) == len(source)}
    
    if target not in wordset:
        return -1
    
    curr_lvl = deque([source])
    next_lvl = deque()
    
    level = 0
    
    # O(wn**2)
    while curr_lvl:
        word = curr_lvl.popleft()
        
        # words to reuse in following iterations
        poppeds = set()
        # O(wn)
        while wordset:
            transition = wordset.pop()
            # O(w)
            if are_neighbors(word, transition):
                if transition == target:
                    return level + 1
                next_lvl.append(transition)
            # if transition is not a neighbor of current word
            else:
                # save transition for following iterations,
                # it could be a neighbor of other words
                poppeds.add(transition)
        wordset = poppeds
        
        # swap queues
        if not curr_lvl:
            curr_lvl = next_lvl
            next_lvl = deque()
            level += 1
    
    return -1


def are_neighbors(word1: str, word2: str) -> bool:
    '''
    Two words are neighbors if they differ by exactly 1 character.

    time O(s)

    space O(1)
    '''
    diff = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff += 1
            if diff > 1:
                return False
    
    return True


@pytest.mark.parametrize(
    ('source', 'target', 'words', 'path'), [
        ('bit', 'dog', ["but", "put", "big", "pot", "pog", "dog", "lot"], 5),
        ('no', 'go', ['to'], -1),
        ('abc', 'deg', ['aba', 'abb', 'abc', 'abg', 'aeg', 'deg'], 3),
        ('abc', 'deg', ['aba', 'abb', 'abc', 'abd', 'abe', 'abf', 'abg', 'aac', 'acc', 'adc', 'aec', 'afc', 'agc', 'ahc', 'bbc', 'cbc', 'dbc', 'ebc', 'fbc', 'deg'], -1),
        ('abc', 'deg', ['aba', 'abb', 'abc', 'abd', 'abe', 'abf', 'abg', 'aac', 'acc', 'adc', 'aec', 'afc', 'agc', 'ahc', 'bbc', 'cbc', 'dbc', 'ebc', 'fbc', 'aeg', 'deg'], 3),
        ('abc', 'deg', ['xba', 'xbb', 'xby', 'xbd', 'xbe', 'xbf', 'abg', 'aax', 'acx', 'adx', 'aex', 'afx', 'agx', 'ahx', 'bxc', 'cxc', 'dxc', 'exc', 'fxc', 'aeg', 'deg'], 3),
        ('abc', 'deg', ['xba', 'xbb', 'xby', 'xbd', 'xbe', 'xbf', 'abg', 'aax', 'acx', 'adx', 'aex', 'afx', 'agx', 'ahx', 'bxc', 'cxc', 'dxc', 'exc', 'fxc', 'aji', 'deg'], -1),
        # need more cases
    ]
)
def test(source, target, words, path):
    assert shortestWordEditPath(source, target, words) == path
