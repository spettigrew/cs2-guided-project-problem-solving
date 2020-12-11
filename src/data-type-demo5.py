"""
Challenge #5:

Create a function that returns the data type of a given argument. There are
seven data types this challenge will be testing for:

- List
- Dictionary
- String
- Integer
- Float
- Boolean
- Date

Examples:
- data_type([1, 2, 3, 4]) ➞ "list"
- data_type({'key': "value"}) ➞ "dictionary"
- data_type("This is an example string.") ➞ "string"
- data_type(datetime.date(2018,1,1)) ➞ "date" 

Notes:
- Return the name of the data type as a lowercase string.
"""
import datetime
value = datetime.date(2018,1,1)
def data_type(value):
    # Your code here

    data = type(value)
    # U - return the data type in a string
    print(data)
    if data == list:
       return "List"
    elif data == dict:
        return "Dictionary"
    elif data == str:
        return "String"
    elif data == int:
        return "Integer"
    elif data == float:
        return "Float"
    elif data == bool:
        return "Boolean"
    elif data == datetime.date:
        return "Date"
print(data_type(value))
