''' In the exciting World Cup cricket match between New Zealand (NZ) and South Africa (SA), the stage is set for a thrilling encounter. SA has won the toss and decided to bowl first, looking to make an early impact on the game.
    Now, the commentators in the stadium are given a special task. They've been instructed to boost the spirits of the batting team (NZ) by displaying an encouraging message on the big screen whenever they spot a "secret pattern" in NZ's performance. A "secret pattern" can be thought of as a good omen for NZ's batting.
    Here's how it works: NZ's performance throughout the match is represented by an array 'A'containing 'N'elements. Each element in 'A' reflects a statistic or a significant moment in the game.
    Your task is to determine whether there exists a "secret pattern" within the array, and if so, return '1'; otherwise, return '0.'
    A "secret pattern" is defined as a set of three consecutive elements in the array, the sum of which is divisible by '10'.
    
    Example:
    Let 'N' = 4, 'A' = [ 10, 11, 21, 8 1.
    There are two sets of three consecutive elements in the given array.
    The first, second, and third elements make the first set, with a sum of 10 + 11 + 21 = 42', which is not divisible by '10'.
    The second, third, and fourth elements make the second set, with a sum of 11 + 21 + 8 = 40' which is divisible by '10'. Therefore, the array does contain the 'secret code'. Thus, the answer is '1'.
    
    Hint:
    Iterate through each array element and check if the last three elements are considered the 'secret code' by finding their sum and checking its divisibility by 10.
'''

from typing import *


def secretCode(n: int, a: List[int]) -> int:
    # Write your code here.
    for i in range(n-2):
        if (((a[i]+a[i+1]+a[i+2])%10)==0):
            return 1
    return 0
    pass