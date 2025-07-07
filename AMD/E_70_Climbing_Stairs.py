'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''

n = 2
def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    step1 = 1
    step2 = 2

    for i in range(3, n + 1):
        count = step1 + step2
        step1 = step2
        step2 = count

    return count

print(climbStairs(n))

