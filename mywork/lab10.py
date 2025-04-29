# Part 1: 
def throw_me_an_error():
    val1 = 14
    val2 = 0
    try:
        return val1 / val2
    except ZeroDivisionError as e:
        print(f"Error: {e}")

# Part 2:
# The finally block makes sure the file always closes even when an error occurs.

#Part 3:
import json

data = '{"valid_key": "value"}'

try:
    jsonD = json.loads(data)
    print(jsonD)
except json.JSONDecodeError as e:
    print(f"JSON import error: {e}")

