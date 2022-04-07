'''
1 Billion Users
We have N different apps with different user growth rates. At a given time t, measured in days, the number of users using an app is g^t (for simplicity we'll allow fractional users), where g is the growth rate for that app. These apps will all be launched at the same time and no user ever uses more than one of the apps. We want to know how many total users there are when you add together the number of users from each app.
After how many full days will we have 1 billion total users across the N apps?

Signature
int getBillionUsersDay(float[] growthRates)

Input
1.0 < growthRate < 2.0 for all growth rates
1 <= N <= 1,000

Output
Return the number of full days it will take before we have a total of 1 billion users across all N apps.

Example 1
growthRates = [1.5]
output = 52
Example 2
growthRates = [1.1, 1.2, 1.3]
output = 79
Example 3
growthRates = [1.01, 1.02]
output = 1047
---

at least 1 app
are growth rates sorted?

u = g**t
t = log_g(u)

days = 1
while true: O(t)
    users = 0
    iterate apps, O(n)
        users += app[i] ** days
        if users >= 10**9:
            break
    if users >= 10**9:
        return days
    days += 1
total time O(nt)

[1.1, 1.2, 1.3]
d = 79
u = 1862.18 + 1800190.38 + 1003517226 >= 10**9

the while loop is essentially going from 1 to t, in increasing order,
searching for the first value that >= 1 billion.
this can be interpreted as iterating a sorted array,
which would allow us to use binary search to look for the days,
in O(n log t).

---
get max possible days, m = ceil log_max(apps)(10**9), O(n)
do binary search to find t, from 1 to m, O(log m)
total time O(n log m), where t <= m

https://leetcode.com/discuss/interview-question/746520/Facebook-or-Recruiting-Portal-or-1-Billion-Users/1340628
'''


import math


BILLION = 10 ** 9


def getBillionUsersDay(growthRates):
    '''
    Time O(n log m)
    
    Space O(1)
    '''
    # O(n)
    max_rate = max(growthRates)
    # upper bound
    max_days = math.ceil(math.log(BILLION, max_rate))

    l = 1
    r = max_days
    # O(n log m)
    while l <= r:
        mid = (r + l) // 2

        users = 0
        # O(n)
        for g in growthRates:
            users += g ** mid
            if users >= BILLION:
                break

        if users < BILLION:
            l = mid + 1
        else:
            r = mid - 1

    return mid


def getBillionUsersDay_brute(growthRates):
    '''
    Time O(nt)
    
    Space O(1)
    '''
    days = 0
    users = 0
    # O(nt)
    while users < BILLION:
        days += 1
        users = 0
        # O(n)
        for app in growthRates:
            users += app ** days
            if users >= BILLION:
                break
    
    return days
