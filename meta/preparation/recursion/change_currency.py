'''
Change in a Foreign Currency
You likely know that different currencies have coins and bills of different denominations. In some currencies, it's actually impossible to receive change for a given amount of money. For example, Canada has given up the 1-cent penny. If you're owed 94 cents in Canada, a shopkeeper will graciously supply you with 95 cents instead since there exists a 5-cent coin.
Given a list of the available denominations, determine if it's possible to receive exact change for an amount of money targetMoney. Both the denominations and target amount will be given in generic units of that currency.
Signature
boolean canGetExactChange(int targetMoney, int[] denominations)
Input
1 ≤ |denominations| ≤ 100
1 ≤ denominations[i] ≤ 10,000
1 ≤ targetMoney ≤ 1,000,000
Output
Return true if it's possible to receive exactly targetMoney given the available denominations, and false if not.
Example 1
denominations = [5, 10, 25, 100, 200]
targetMoney = 94
output = false
Every denomination is a multiple of 5, so you can't receive exactly 94 units of money in this currency.
Example 2
denominations = [4, 17, 29]
targetMoney = 75
output = true
You can make 75 units with the denominations [17, 29, 29].
---
use memoization, for each amount store if it has exact change, O(td)

use BFS, return true when first 0 is reached, O(td)
'''


from collections import deque


def canGetExactChange(targetMoney, denominations) -> bool:
    '''
    Use BFS.
    
    Time O(td)
    
    Space O(t)
    '''
    # set index 0 to true, rest to false
    is_visited = [True] + [False] * targetMoney

    queue = deque([targetMoney])
    
    # O(t)
    while len(queue) > 0:
        curr_amount = queue.popleft()
        
        # O(d)
        for value in denominations:
            subtraction = curr_amount - value
            # when first valid path is found
            if subtraction == 0:
                return True
            
            if subtraction >= 0 and not is_visited[subtraction]:
                queue.append(subtraction)
                is_visited[subtraction] = True

    return False
