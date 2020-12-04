"""
Challenge #1:

Write a function that retrieves the last n elements from a list.

Examples:
- last([1, 2, 3, 4, 5], 1) ➞ [5]
- last([4, 3, 9, 9, 7, 6], 3) ➞ [9, 7, 6]
- last([1, 2, 3, 4, 5], 7) ➞ "invalid"
- last([1, 2, 3, 4, 5], 0) ➞ []

Notes:
- Return "invalid" if n exceeds the length of the list.
- Return an empty list if n == 0.
"""
#UPER
# Understand - ask LOTS of questions! Inputs/outputs, list of nums, number of items from end of list. Outputs: list or 'invalid' Edge cases: invalid if n> len of list. [] if n=0
# Plan - Pseudo code. Plain english. (Explain it to your mom). How to handle edge cases (as mentioned above. How to do main problem. Get last n elements of list. Slice [:]. (Get all elements starting from len(-n)) arr[-n:]

def last(a, n):
    # Your code here
    if n > len(a):
        return None
    # elif n == 0:          or include this code
    #     return []
    #main solution code
    return a[leng(a)-n:]   # or [-n:] will work as well

