# Examples

shopping_cart = ["notebooks", "laptops"]
print(shopping_cart[0])  # Output: notebooks
print(shopping_cart[1])  # Output: laptops
# print(shopping_cart[2])    #IndexError: list index out of range

# List Slicing

game_cart = ["halo", "pokemon", "minecraft", "fortnite"]
print(game_cart[:3])
# Output: ['halo', 'pokemon', ' minecraft'] It takes elements from the beginning
print(game_cart[3:])
# Output  : ['fortnite'] It takes all elements starting from a specific index until the end
print(game_cart[0::2])
# Output: ['halo', 'minecraft'] It takes every second element starting from the first one.
print(game_cart[1:3])
# Output: ['pokemon', 'minecraft'] It doesn't take the first element , it starts at the second one.

# When slicing a list it will create a new list in memory.
games = game_cart[1:3]
# It creates a new list with two elements, 'pokemon' and 'minecraft'

games = game_cart[:]
#  This is called shallow copy, it creates a new reference to the same data


# List are  mutable, we can change their values.
game_cart[1] = "red dead redemption"
print(game_cart)  # Output  :['halo', 'red dead redemption ', 'minecraft', 'fortnite']

# Matrix example

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0][0])  # Output: 1
print(matrix[1][1])  # Output: 5
# We can also modify matrixes
matrix[0][0] = 4
print(matrix)  # Output:   [[4, 2, 3], [4, 5, 6], [7, 8, 9]]


# List Methods

basket = [1, 2, 3, 4, 5]

# Adding to a list using append, insert and extend  methods

# Append method

basket.append(6)  # Adds element at the end of the list

# new_li = basket.append(7)
# Returns None because append doesn't return anything to variable

new_li = basket  # Assigns entire list to another variable

print(new_li)  # Output: [1, 2, 3, 4, 5,  6]

# insert method

basket1 = [1, 2, 3, 4, 5]

basket1.insert(3, 100)  # Inserts element at specific position

# new_li1 = basket1.insert(3, 100)  # Returns none because insert doesn't return anything.

print(basket1)  # Output : [1, 2, 3, 100, 4, 5]

# Extend method

basket2 = [1, 2, 3, 4, 5]

basket2.extend([50, 160])  # Add multiple elements at once from another list

# new_li2 = basket2.extend([50, 160])  # This will give error as extend doesn't return any value

print(basket2)  # Output : [1, 2, 3, 4, 5, 50, 160]

# Removing from a list using  pop, remove and clear methods

# Pop method
basket3 = [1, 2, 3, 4, 5]

# basket3.pop()  # Remove last item in the list. 5 will be removed from the list.
# print(basket3) # Output : [1, 2, 3, 4]

basket3.pop(0)  # Remove first item in the list.  1 will be removed from the list.
print(basket3)  # Output : [2, 3, 4, 5]

# Remove method
basket4 = [1, 2, 3, 4, 5]

basket4.remove(
    3
)  # It removes only one occurrence of the specified value. If there are more than one '3' present then it will remove only one '3'

# new_li3 = basket4.remove(1)
# print(new_li3)  # Output : None as remove method does not return anything

print(basket4)  # Output : [1, 2, 4, 5]

# Clear Method

basket5 = [1, 2, 3, 4, 5]

basket5.clear()  # It removes all items from the list.

print(basket5)  # Output: []

# Index Method

basket6 = ["a", "b", "c", "d", "e"]

print(basket6.index("c"))  # Output :  2 ,because 'c' is at index position 2
print(basket6.index("a"))  # Output : 0 because index of 'a' is 0
print(basket6.index("d", 0, 4))  # Output : 3 because d is at 3rd position

# The in Keyword in python

print("a" in basket6)  # Output : True if 'a' exists in the list else False

# Count Method

print(basket6.count("a"))  # Output : Number of times 'a' appears in the list

# Sort, Sorted and Reverse Methods

basket7 = [5, 3, 8, 9, 2]

basket7.sort()  # It sorts the elements of a given list in ascending order.

print(basket7)  # Output : [2, 3, 5, 8, 9]

print(
    sorted(basket7)
)  # Output : [2, 3, 5, 8, 9] Returns a new sorted list from the elements of any sequence.

basket7.reverse()  # It reverses the sorted or original list.

print(basket7)  # Output : [9, 8, 5, 3, 2]

# Creating a list using Range keyword

print(list(range(50)))  # Output : List with numbers from 0 to  49

# Join Method works with strs and lists


new_sentence = " ".join(["Hello", "how", "are", "you"])

print(new_sentence)  # Output :   Hello how are you

# List unpacking

a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Here other will contain all the remaining values after b, c

print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3
print(other)  # Output: [4, 5, 6, 7, 8]
print(d)  # Output: 9
