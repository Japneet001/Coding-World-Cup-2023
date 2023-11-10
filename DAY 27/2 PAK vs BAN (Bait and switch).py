''' You are a cricket organizer with 'n'matches scheduled. The matches are held on the X-axis in the coordinate plane and their X-coordinate indicated by array 'a'. A sponsoring airline offers extra revenue to relocate 'k'venues last-minute.
    Relocating a match to X-coordinate 'm'earns '| a[i] = m |' revenue. Return the maximum revenue from these relocations.
    For Example:
        Let 'n' = 2, 'a' = [ 5, 4 ], 'k' = 1, 'm' = 7.
        If you relocate the first match, an extra revenue of | 5-7 = 2' is earned..
        If you relocate the second match, an extra revenue of | 47 | = 3' is earned..
        Therefore, you will change the venue of the second match. Thus, the answer is '3'.
'''

def baitAndSwitch(n: int, a: list, k: int, m: int) -> int:
    li=[]
    for i in range(n):
        li.append(abs(a[i]-m))
    li.sort()
    li.reverse()
    sum=0
    for i in range(k):
        sum+=li[i]
    return sum
    # Write your code here.
