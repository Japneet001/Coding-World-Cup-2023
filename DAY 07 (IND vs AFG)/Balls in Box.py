''' The newly formed government of Afghanistan thinks that the main reason their cricket team cannot win against the Indian team is the boxes in which cricket balls are kept.
    There are two types of boxes, 'A' and 'B'. Type 'A' boxes have a total capacity of 'X' balls, and type 'B' boxes have a total capacity of 'Y' balls.
    Currently, they have a total of 'N' boxes of type 'A' filled with balls, but their government wants to transfer all balls to type 'B' boxes.
    Find how many boxes of type 'B' they require to transfer all balls if they use the full capacity of type 'B' boxes.
    
    Example:
        'N' = '2'
        'X' = '3'
        'Y' = '2'
        They have '2' boxes of type 'A', and each has '3' balls. So, they have total '6' balls.
        The capacity of one box of type 'B' is '2' balls, so for '6' balls, they need '3' type 'B' boxes.
        So, the answer is '3'.
'''


from typing import *


def boxFilling(n: int, x: int, y: int) -> int:
    # write your code here
    if (((n*x)%y)==0):
        return ((n*x)//y)
    else:
        return ((n*x)//y)+1
    pass