''' A cricket player has matches scheduled over a 30-day period, and he follows certain fitness rules to decide whether to play a match or not. The rules are:
        • If he plays a match on a particular day, he must rest the next day to recover.
        • He always plays the first scheduled match.
    You are given a binary string of 30 characters. '1' represents a scheduled match, while '0' represents a rest day.
    Your task is to calculate the total number of matches he will play during those 30 days.
    
    Example:
        Schedule = '010110000000000000000000000000'.
        The player has matches on the 2nd, 4th, and 5th day.
        The player will play his first match on the second day. Then, he will play another match on the fourth day, which means he will rest on the fifth day due to the fitness rule. In total, he will play two matches.
        Hence, the answer for this test case is 2.
'''


from typing import List
def calculateNumberOfDays(s: str) -> int:

    # write your code here
    matches_played = 0
    rest_day = False

    for day in s:
        if day == '1' and not rest_day:
            matches_played += 1
            rest_day = True
        else:
            rest_day = False

    return matches_played