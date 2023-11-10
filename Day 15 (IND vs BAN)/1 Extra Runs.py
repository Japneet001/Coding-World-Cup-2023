''' As India is gearing up for the highly anticipated match against Bangladesh in the Cricket World Cup, the Indian cricket team is focusing on their daily practice sessions.
    Each day, they set a practice target of scoring 'M' runs, aiming to fine-tune their skills for the big game. However, during their training, they manage to score 'N' runs each day.
    If they score more than the daily target during their practice sessions, the additional runs scored beyond their daily practice goal are regarded as extra runs.
    Return the total number of extra runs they made during 'X' days of practice.
    
    Example :
    Input: 'N' = 10, 'M' = 6, 'X' = 3
    Output: 12
    The team sets a daily practice target of scoring 6 runs and they score 10 runs each day.
    So, every day, (106) = 4 extra runs are made. After 3 days, the total number of extra runs will be 3*4 = 12.
'''

from typing import List

def extraRuns(n: int, m: int, x: int) -> int:
    # Write your code here.
    if ((n-m)*x > 0):
        return (n-m)*x
    return 0
    pass