''' As a team selector for the upcoming matches, you are given an array 'A' of 'N' players, where 'A[i]' represents the skill level of the 'i-th' player.
    To maximize your chances of winning, you are tasked with selecting a team of exactly 'K' players, each with a skill level of '9'.
    If it is possible to select such a team, return 1. Otherwise, return 0.

    For Example:
        Let 'N' = 5, 'A' = [1, 9, 2, 3, 9 ], 'K' = 2.
        The team consisting of the '1-st' and level array of [ 9, 9]. '4-th' players has a skill
        Therefore, it is possible to select a team of 'K with a skill level of '9'. = 2' players, each
        Thus, the answer is '1'.
'''

from typing import *


def nines(n: int, a: List[int], k: int) -> int:
    # Write your code here.
    count = 0
    for i in range(n):
        if a[i]==9:
            count=count + 1
    if count >= k:
        return 1
    return 0
    pass