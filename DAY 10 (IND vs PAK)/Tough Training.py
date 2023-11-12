''' You're the coach of the Indian cricket team. You're currently tracking the scores from practice matches played by one of your players. In the first match, the player scored 'A' runs. With ongoing practice, his score is increasing by 'D' runs after each match.
    'X' is your favorite number and you're curious to find out if the player will score exactly 'X' runs in any of the upcoming matches.
    Your task is to Return 1 if the player scores exactly 'X' runs in any of the matches; otherwise, return 0.

    Example:
        Input: 'A' = 2, 'D' = 3, 'X' = 8
        Output: 1
        The sequence of runs scored by the player in the matches is 2, 5, 8, 11, .... 
        Since 8 is present in this sequence. Therefore, we return 1. 
'''

from typing import *

def checkSequence(a: int, d: int, x: int) -> int:
    # Write your code here.
    if d == 0:
        if a == x:
            return 1
        else:
            return 0
    else:
        if (x - a) % d == 0 and (x - a) // d >= 0:
            return 1
        else:
            return 0