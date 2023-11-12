''' ICC has to give out the Man of the match award but there has been a tie between 2 players. ICC has to find 2 trophies to award them.
    The happiness of each player is directly proportional to the size of the award they receive. However, if one player receives a larger award than the other, they will become upset.
    ICC's goal is to maximize the happiness of both players. If it's possible to find two awards of equal size, return the maximum size of the awards. If it's impossible to find two awards of equal size, return -1.

    For Example:
        Awards: [3, 4, 5, 2, 1, 4, 2]
        ICC can give each player a ball of size 2, and both will be happy. However, if he gives both of them awards of size 4, they will be happier
        ICC can't use the ball of size 5 as the other player will become upset as they will receive a smaller ball..
        Hence the maximum size of ball he can give is 4.
'''


from typing import List

def happyPlayers(balls : List[int]) -> int:
    # Write your code here.
    li=[]
    dup=[]
    for i in range (len(balls)):
        if balls[i] not in li:
            li.append(balls[i])
        else:
            dup.append(balls[i])
    dup.sort()
    if (len(dup)==0):
        return -1
    return dup[len(dup)-1]
    pass