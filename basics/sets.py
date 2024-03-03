# Sets are like dictionaries but does not have key value pairs. It only has elements.

# my_set = {1, 2, 3, 4, 5, 5}
# print(my_set)  # Output: {1, 2, 3, 4, 5} (Duplicate values removed)

# my_set.add(500)
# my_set.add(3)

# print(my_set)  # Output : {1, 2, 3, 4, 5, 500}

my_list = [1, 2, 3, 4, 5, 5]
print(set(my_list))
# Output : {1, 2, 3, 4, 5} Converting list to set using the built-in function 'set()'

# print(1 in my_set)  # Output : True if element is present else False
# print("6" in my_set)  # Output : False

# Sets Methods difference, discard, difference_update, intersection, isdisjoint, issubset, issuperset and union

my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

# print(my_set.difference(your_set))
# Output : {1, 2, 3} The difference between two sets gives us the elements that

# my_set.discard(5)
# print(my_set)  # Output : {1, 2, 3, 4} Element discarded successfully

# my_set.difference_update(your_set)
# print(my_set)
# Output : {1, 2, 3} After updating the original set with difference_update(), it becomes {1, 2}. Because all common elements were

# print(my_set.intersection(your_set))
# Output: {4, 5} Gives common elements from both sets

# print(my_set.isdisjoint(your_set))
# Output : False If there are no common elements then it returns False, else it returns True

# print(my_set.union(your_set))
# Output : {1, 2, 3, 4, 5,  6, 7, 8,  9, 10} Union of two sets gives us all unique elements from both sets

# print(my_set.issubset(your_set))
# Output : True If all elements of one set is present in another set then it returns True, else it returns False

# print(my_set.issuperset(your_set))
# Output : True if first set is a superset of second set else False
