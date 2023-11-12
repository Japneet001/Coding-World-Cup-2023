''' In the South Africa vs. Afghanistan World Cup cricket match, suppose you, as a fan, wants to create a shorter name that combines the names of all the players. You're given a string 'S' of length 'W'that includes the names of all the players combined into a single string.
    To create this name, you can choose any two adjacent characters in the string 's' that are the same, and then remove one of those characters.
    Your task is to determine the maximum number of operations you can perform on the string 'S' to make the combined player names shorter.
    
    Example:
        Let's say, 'S'='bavumaaiden'
        We can select the 6th and 7th characters and delete one of them. 'bavumaaiden'->''bavumaiden''
        We cannot perform any more operations on the string. Hence we return 1.
'''


from typing import *


def stringReduction(s: str) -> int:
    # write your code here

    operations = 0
    n = len(s)

    for i in range(1, n):
        if s[i] == s[i - 1]:
            operations += 1

    return operations
    

    pass
