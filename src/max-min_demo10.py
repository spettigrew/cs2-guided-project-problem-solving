"""
Challenge #10:

Given a string of space separated integers, write a function that returns the
maximum and minimum integers.

Example:
- max_and_min("1 2 3 4 5") -> "5 1"
- max_and_min("1 2 -3 4 5") -> "5 -3"
- max_and_min("1 9 3 4 -5") -> "9 -5"

Notes:
- All inputs are valid integers.
- There will always be at least one number in the input string.
- The return string must be two numbers separated by a single space, and
the maximum number is first.
"""
input_str = "1 2 3 4 5"
def max_and_min(input_str):
    # Your code here
    # U - given integers, find the max and min
    # initialize results to string
    results = ""
    # initizalize max and min to the first integer of the string
    max = int(input_str[0])
    min = int(input_str[0])
    print(max, min)
    # iterate through the string itself
    for char in input_str:
        # if char is not whitespace, by default it is a number
        if char != " ":
        # check if integer is greater than the max
            if int(char) > max:
                # set max = the int
                max = int(char)
            # check if integer is less than the min
            if int(char) < min:
                # set min = the int
                min = int(char)
    # set min and max to the result string
    results += str(max)
    results += " " 
    results += str(min)
    
    return results

print(max_and_min(input_str))