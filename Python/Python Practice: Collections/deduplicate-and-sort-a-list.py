# Python code​​​​​​‌​‌‌‌‌‌​‌‌‌​‌‌‌‌‌​​​​​​​‌ below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False

def prepare_list(animals):
    list = []
    for i in animals:
        if i not in list:
            list.append(i)
    return sorted(list)
