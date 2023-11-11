''' In the context of the India vs Sri Lanka World Cup match, let's focus on the top batsmen for India, Virat Kohli and Rohit Sharma. Both players have been leading run-scorers in the tournament, but there's a specific difference 'Y' in the total runs scored by each of them.
    The aim is to find the runs that both Virat and Rohit need to score in this match to reduce the difference 'Y' between their run totals. This will help both players become the leading run-scorers for the Indian team. Additionally, the combined runs scored by Virat and Rohit should contribute 'Y'runs to the team's total.
    Return a vector of size 2 containing the runs of the two players mentioned above in any order if it's possible to achieve those runs; otherwise, return [-1, -1].
    
    For example:
        Let 'X' = 8, 'Y' = 4. So, the runs can be 6 and 2 as their sum is 8 and their difference is 4.
'''

def findPair(x: int, y: int) -> list:
    # Write your solution here.
    if ((x+y)%2==0 and (x-y)%2==0):
        a=(x+y)//2
        b=(x-y)//2
        li=[a,b]
    else:
        li=[-1,-1]
    return li
