# Check for duplicates in a list

some_list = ["a", "b", "c", "d", "c", "e"]

duplicates = []

for v in some_list:
    if some_list.count(v) > 1 and v not in duplicates:
        duplicates.append(v)

print(duplicates)  # Output: ['c']
