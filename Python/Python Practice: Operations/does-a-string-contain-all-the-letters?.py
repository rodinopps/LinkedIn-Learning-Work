# Python code​​​​​​‌​‌‌‌‌‌​‌‌‌​‌‌‌​‌‌​​​‌​​‌ below
# Use print("messages...") to debug your solution.
from string import ascii_lowercase

show_expected_result = False
show_hints = False

def check_string(my_string):
    string = ""
    for i in ascii_lowercase:
        if i not in my_string.lower():
            string += i
    if string == "":
        return "The string contains all the letters of the alphabet."
    else:
        return f"The string is missing the following letters: {string}"
