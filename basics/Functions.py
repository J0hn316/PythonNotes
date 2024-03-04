# # Examples of Functions


# def greet():
#     print("hello")


# greet()  # Call the function
# # output: hello


# def say_hi(name, age):
#     print(f"Hello, {name} and you are {age} years old.")


# say_hi("John", 25)  # Call the function with arguments
# # output: Hello, John and you are 25 years old.

# # Default argument values can be assigned using the following syntax:
# #     def function_name(parameter=default_value)


# def greet1(name="jack", age=15):
#     print(f"Hello, {name} and you are {age} years old.")


# greet1()  # If no arguments provided, use default values
# # output: Hello, jack and you are 15 years old.

# greet1("Jane")
# # Only one argument provided - uses that as name and uses default value for age
# # output: Hello, Jane and you are 15 years old.

# greet1("Tom", 30)  # Both name and age provided - uses those values


# def add_numbers(a, b=10):
#     print(a + b)


# print(add_numbers(3))
# # The second parameter is not provided so it uses the default value (10).
# # output: 13

# print(add_numbers(4, 7))  # Both parameters are given - no problem!
# # output: 11


# # Return with functions


# def multiply(x, y):
#     return x * y


# result = multiply(3, 4)
# print(result)
# # This will display "12".


# def checkDriverAge(age):
#     age = input(f"Enter your age: ")
#     if int(age) < 18:
#         print("Sorry, you are too young to drive this car. Powering off")
#     elif int(age) > 18:
#         print("Powering On. Enjoy the ride!")
#     elif int(age) == 18:
#         print("Congratulations on your first year of driving. Enjoy the ride!")


# checkDriverAge(16)
# # Output: Sorry, you are too young to drive this car. Powering Off
# checkDriverAge(19)
# # Output: Congratulations on your first year of driving. Enjoy the ride!
# checkDriverAge(18)
# # Output: Powering On. Enjoy the ride!


# def checkDriverAge1(age=17):
#     if int(age) < 18:
#         print("Sorry, you are too young to drive this car. Powering off")
#     elif int(age) > 18:
#         print("Powering On. Enjoy the ride!")
#     elif int(age) == 18:
#         print("Congratulations on your first year of driving. Enjoy the ride!")


# checkDriverAge1()
# # Output: Sorry, you are too young to drive this car. Powering off
# checkDriverAge1(19)
# # Output: Powering On. Enjoy the ride!
# checkDriverAge1(18)
# # Output: Congratulations on your first year of driving. Enjoy the ride!


# # *args  and **kwargs allow functions to accept a variable number of arguments.
# # Order of args: params, *args, default parameters, **kwargs


# def my_func(*args):
#     print(args)
#     return sum(args)


# print(my_func(1, 2, 3, 4, 5))
# # Output:  (1, 2, 3, 4,5)
# #         1 + 2 + 3 + 4 + 5 = 15


# def my_func2(*args, **kwargs):
#     total = 0
#     for item in kwargs.values():
#         total += item
#     return sum(args) + total


# # **kwargs creates a dictionary with keyword arguments passed to the function.

# print(my_func2(1, 2, 3, 4, 5, num1=5, num2=10))
# Output :  6

# create a function that takes a list as an arg and returns the highest even number


def find_highest_even(li):
    evens = []
    for item in li:
        if not item % 2 and item not in evens:
            evens.append(item)
    return max(evens)


print(find_highest_even([10, 2, 3, 4, 8, 11]))
# Output: 10
