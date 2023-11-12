''' In the context of the India vs. Netherlands World Cup cricket match, the Indian cricket player is positioned facing North. A sequence of 'N'instructions in a binary string 'S'determines the player's turns. If 'S[i]' is 0, the player will turn clockwise by '90' degrees; otherwise, they will turn counterclockwise by '90' degrees.
    Due to fatigue, the player prefers not to execute all 'N' instructions. The player wants to determine the final direction. Find the ultimate facing direction, which can be 'NORTH', 'SOUTH', 'EAST', or 'WEST'.
    
    Example:
        N = '3' S = '101'
        Player's direction will change in the following order: North West North → West
        So, the answer is 'WEST'.
'''

from typing import List

def directionGame(n: int, s: str) -> str:
    # Write your code here.
    dir=['NORTH','WEST','SOUTH','EAST']
    present_dir=0
    for i in range(n):
        if s[i]=='1':
            present_dir+=1
        else:
            present_dir-=1
    if present_dir>3 or present_dir<0:
        present_dir=present_dir%4
    return dir[present_dir]
    pass