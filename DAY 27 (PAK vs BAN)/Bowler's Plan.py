''' The bowlers of Pakistan have collectively recognized their need for improved consistency in on-field decisions regarding their bowling variations. To address this, they have devised a method in which they randomly generate a string, assigning specific attributes such as bowling length and speed to each character.
    They have also determined that the 'K'th unique letter in this generated string will indicate when they should deliver a bouncer. The wicket keeper is eager to identify which character designates the bouncer so that he can be adequately prepared.
    You are given the string 'S' of length 'N' consisting of lowercase letters and the integer 'K'.
    Return the 'K'th unique letter in 'S'. If the string has less than 'K' unique letters return '?' instead.
    For Example:
        Let 'N' = 7, 'S' = 'aababdc', K = 3.
        The unique letters in 'S' in order are: 'a', 'b', 'd', 'c'. Therefore, the answer is 'd' which means the balls assigned character 'd' will be a bouncer.
'''

from typing import *


def kthUnique(n: int, s: str, k: int) -> str:
    # write your code here
    li=[]
    for i in range(n):
        if (s[i] not in li):
            li.append(s[i])
    if (0<k<=len(li)):
        return li[k-1]
    return '?'