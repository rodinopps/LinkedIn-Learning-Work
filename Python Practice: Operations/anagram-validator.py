# Python code​​​​​​‌​‌‌‌‌‌​‌‌‌​‌‌‌​‌‌‌‌​‌​​‌ below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False

def is_anagram(first_string, second_string):
    letter1 = ""
    letter2 = ""
    for i in first_string.lower():
        letter1 += i if i.isalpha() else ""
    for i in second_string.lower():
        letter2 += i if i.isalpha() else ""
    return (sorted(letter1) == sorted(letter2))
