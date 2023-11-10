''' You have an array 'X' containing 'N' integer values, where each value in 'X' represents the individual performance of a player in the match. Now, you create another array 'Y' of the same size 'N', following the rules below:
        1. If the performance value 'X[i]' is divisible by '3', 'Y[i]' is set to 'X[i]'. 
        2. If 'X[i]' is not divisible by '3', 'Y[i]' is the square of 'X[i]'.
    Your task is to calculate the sum of the elements in the 'Y' array, which represents the overall impact or contribution of the players in the match based on these rules.
    
    Example:
    N' = 3 'X'= [3, 4, 1]
    Since X[0] is divisible by '3', Y[0]=3. Here X[1] and X[2] are not divisible by 3, So Y[1]=4*4=16 and Y[2]=1*1=1. Y[0]+Y[1]+Y[2]=20.
'''


from typing import *
def divisible3(n: int, x: List[int]) -> int:
    # Write your code here
    y=[]
    for i in range(n):
        if ((x[i]%3)==0):
            y.append(x[i])
        else:
            y.append(pow(x[i],2))
    return sum(y)
    pass