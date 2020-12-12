"""
Challenge #2:

Given a list of numbers, create a function that returns the list but with each
element's index in the list added to itself. You should add 0 to the number at
index 0, add 1 to the number at index 1, etc.

Examples:
- add_indexes([0, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4]
- add_indexes([1, 2, 3, 4, 5]) ➞ [1, 3, 5, 7, 9]
- add_indexes([5, 4, 3, 2, 1]) ➞ [5, 5, 5, 5, 5]

Notes:
- The input list will only contain integers.
"""
numbers = [1, 2, 3, 4, 5]

def add_indexes(numbers):
    # Your code here

    # initiliaze results array to hold result
    results = []

    # iterate thourgh the array. Enumerate gives me the index/value
    for idx, value in enumerate(numbers):
        # add idx and value and append it to results array
        results.append(idx + value)
        
    # return the array
    return results
print(add_indexes(numbers))


# ENUMERATE - the function five you back 2 loop variables:
    # 1. the count of the current iteration
    # 2. the valuse of the item at the current iteration.
    # - With enumerate, you don't need to remember to access the item from the iterable, and you don't need to remeber to advance the index at the end of the loop. 
