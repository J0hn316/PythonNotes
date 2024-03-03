# Tuples Examples

# Tuples are like lists but can not be modified.
# They are immutable, meaning that you cannot change their values once they have been assigned.
# Tuples can be used when you want to create a list that you dont want to modify.

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])  # Output : 1
print(5 in my_tuple)  # Output: True


new_tup = my_tuple[1:2]
print(new_tup)  # Output: (2,)

a, b, c, *other = (2, 4, 6, 8, 10)
print(a)  # Output: 2
print(b)  # Output: 4
print(c)  # Output : 6
print(other)  # Output: [8, 10]

# Methods for Tuples are count,index and len

print(my_tuple.count(4))  # Output: 1
print(my_tuple.index(3))  # Output: 2
print(len(my_tuple))  # Output: 5
