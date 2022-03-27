from collections import deque


def coin_change_dp(coins: list[int], amount: int) -> int:
    '''
    Use dynamic programming to memoize recursion.

    Time O(ac)
    
    Space O(a)
    '''
    if amount == 0:
        return 0

    INF = float('inf')
    # memory array to store the minimum coins needed
    # for each number from 0 to amount,
    # default to infinity meaning that there's no exact change for them (yet)
    # except 0 whose minimum is 0, because it's the base case
    memory = [0] + [INF] * amount

    # O(ac)
    for i in range(1, len(memory)):
        # O(c)
        for coin in coins:
            # subtract current coin from amount i
            diff = i - coin
            # if subtraction >= 0 then it's a valid path that has exact change
            if diff >= 0:
                # update number of coins needed for amount i and for current coin
                # by choosing the minimum between the current number of coins and
                # the minimum coins needed for the subtraction
                memory[i] = min(memory[i], memory[diff] + 1)
                # after the for loop this is the minimum between
                # the minimums of every subtraction of amount i
    
    return -1 if memory[amount] == INF else memory[amount]


def coin_change_bfs(coins: list[int], amount: int) -> int:
    '''
    Use BFS to traverse tree of subtractions of amount and coins.
    
    Time O(ac)
    
    Space O(a)
    '''
    if amount == 0:
        return 0
    
    current_level = deque([amount])
    next_level = deque()
    
    # keep track of visited amounts
    visiteds = [True] + [False] * amount
    
    level = 0
    # O(ac)
    while len(current_level) > 0:
        current_amount = current_level.popleft()
        
        # O(c)
        for coin in coins:
            difference = current_amount - coin
            
            # the first exact change that is found is the minimum coins,
            # it's shortest path to it
            if difference == 0:
                return level + 1

            if difference >= 0 and not visiteds[difference]:
                # add "child" amount
                next_level.append(difference)
                # mark it as visited so its subtree is not recalculated
                visiteds[difference] = True
        
        # swap levels
        if len(current_level) == 0:
            current_level = next_level
            next_level = deque()
            # go to next level
            level += 1
    
    return -1
