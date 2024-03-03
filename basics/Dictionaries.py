# Examples

dictionary = {"a": 1, "b": 2}

print(dictionary["b"])  # Output: 2

some_dict = {"a": [1, 2, 3], "b": "jack", "c": False}

# Dictionary keys are immutable and can be accessed using the square bracket notation

# Dictionary Methods

user = {"name": "John", "age": 23, "city": "New York"}

print(user.get("name"))  # Output: John
print(user.get("job", "helpdesk"))  # Output: helpdesk (default value if key not found)

# Create a dictionary using dict () function

user2 = dict(name="Jack")
print(user2)  # Output: {'name': 'Jack'}

# Using the key word 'In' with dictionaries

print("name" in user)
# True or False - checks whether a certain key is present in the dictionary

print("age" in user.keys())  # Output: True
print(23 in user.values())  # Output: True

print(user.update({"age": 24}))  # Updates an existing key-value pair

print(user2.popitem())
# Output : ('name', 'Jack') - removes last key value pair from the dictionary and returns it as a tuple
