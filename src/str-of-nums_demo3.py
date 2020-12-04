"""
Challenge #3:

Given a string of numbers separated by a comma and space, return the product of the numbers.

Examples:
- multiply_nums("2, 3") ➞ 6
- multiply_nums("1, 2, 3, 4") ➞ 24
- multiply_nums("54, 75, 453, 0") ➞ 0
- multiply_nums("10, -2") ➞ -20

Notes:
- Bonus: Try to complete this challenge in one line!
"""
# product of numbers (multiply)
# Plan - convert input into numbers, maybe an array. Multiply array of nums
    # convert using .split(", ")
    # final value = 1
    # use a for loop ov all nums. Turn it into an int(). Multiply into final value

def multiply_nums(nums):
    # Your code here
    #return nums * str(.split(", ")[nums])

    nums_array = nums.split(', ')
    final_val = 1
    for num in nums_array:
        final_val *= int(num) 
        final_val = final_val * int(num)  # turns nums into integers
    return final_val

