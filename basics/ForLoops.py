# Iterables - lists, dictionaries, tuples, sets and strings
# iterate - one by one check each item in the collection

# Examples of For loops

for item in "Python":
    print(item)
# This will display each character from the string 'Python' on a separate line.

for item in [1, 2, 3, 4, 5]:
    print(item)
# This will display each number in the list [1, 2, 3, 4, 5] on a separate line.

for i in {1, 2, 3, 4, 5}:
    print(i)  # This is another way to write it using set data

for i in (1, 2, 3, 4, 5):
    print(i)  # This is another way to define the sequence with  tuple instead of list.


for i in (1, 2, 3, 4, 5):
    for x in ["a", "b", "c"]:
        print(i, x)
        # This nested loop displays each combination of numbers and letters on a separate line.


# for loop with a dictionary

user = {"name": "Golem", "age": 2000, "can_swim": False}

for item in user:
    print(item)  # this will show all keys in the dictionary

for k, v in user.items():
    print(k, v)
# Output:  name Golem age 2000 can_swim False

for item in user.values():
    print(item)  #  Output: Golem 2000 False
for item in user.keys():
    print(item)  # Output: name age can_swim

# Create a counter that adds up all the numbers in a list with a for loop
numbers = [1, 2, 3, 4, 5]
count = 0
for num in numbers:
    count += num
    print("The sum of the numbers is: ", count)
# Output: The sum of the numbers is:  15

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0

for num in my_list:
    count += num
print(count)
# Output:  55

# Range

for i in range(0, 5):
    print(i)
# Output: 0 1 2 3 4

for i in range(0, 10, 2):
    print(i)
# Output: 0 2 4 6 8

for _ in range(10, 0, -1):
    print(_)
# Output : 10 9 8 7 6 5 4 3 2 1

for _ in range(2):
    print(list(range(5)))
# Output  : [0, 1, 2, 3, 4] [0, 1, 2, 3, 4]

# Enumerate

for i, char in enumerate("Hello"):
    print(i, char)
# Output: 0 H 1 e 2 l 3 o

for i, char in enumerate([1, 2, 3]):
    print(i, char)
# Output: 0 1 1 2 3

for i, char in enumerate((1, 2, 3)):
    print(i, char)
# Output : 0 1 2

for i, char in enumerate(list(range(100))):
    if char == 50:
        print(f"index of 50 is: {i}")
# Output:     index of 50 is: 49
