''' A cricket coach is analyzing the performance of his team by studying an array 'X' representing the runs scored in 'N' games. He defines the 'impact' of a subarray of games as the runs scored in the last game of the subarray. Determine the total 'impact' runs from all possible subarrays of games. A subarray is any contiguous part of the array representing consecutive matches.
    
    Example:
        'N' = 2
        'X' = [3, 2].
        There are a total of '3' subarrays in the given array i.e., '[3]', '[2]', and '[3,2]'.
        The total sum of the 'impact' runs of these subarrays will be the sum of the runs scored in the last game of the subarrays which will be equal to '3+2+2=7'
'''


from typing import *


def subarray(n: int, x: List[int]) -> int:
    # write your code here
    impact = 0
    for i in range(n):
        impact += (x[i] * (i + 1))

    return impact