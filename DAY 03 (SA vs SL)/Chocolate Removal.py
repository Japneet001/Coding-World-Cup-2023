''' In the thrilling South Africa vs Sri Lanka match, you find yourself in the stadium selling chocolates to the passionate fans.
    You are given an array 'A' of length 'N'. Each element 'A[i]' represents the number of chocolates in the 'i-th' pile. However, you want to keep some chocolates for yourself, so you decide that you will not sell more than 23 chocolates in a single pile.
    In a single move, you are allowed to perform the following operation: If a pile contains more than 23 chocolates, remove the excess chocolates.
    Your task is to calculate and return the total number of chocolates you will remove from the piles.
    
    Example :
        Input: A = [25, 24, 29, 15]
        Output: 9
        First pile: Contains 25 chocolates, remove 2 to leave 23. Chocolates removed = 2.
        Second pile: Contains 24 chocolates, remove 1 to leave 23. Chocolates removed = 1.
        Third pile: Contains 29 chocolates, remove 6 to leave 23. Choclates removed = 6
        Fourth pile: Contains 15 chocolates, no chocolates removed as the pile already has less than or equal to 23 chocolates.
        Total chocolates removed = 2 + 1 + 6 = 9.
'''


from typing import List

def totalChocolates(n: int, a: List[int]) -> int:
    # Write your code here.
    count = 0
    for i in range(n):
        if a[i]>23:
            count = count + a[i] - 23
    return count 
    pass