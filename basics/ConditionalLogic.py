# Conditional Logic if statements in python

# is_old = True
# is_licensed = True

# if is_old:
#     print("You may drive")  # This will run because the condition is true
# elif is_licensed:
#     print("You can drive now" )   # This won't run because the first statement was true
# else:
#     print("You are not old enough")

# if is_old and is_licensed:
#     # The 'and' keyword returns true only if both conditions are met
#     print("You may drive")
# elif is_old:
#     # If the first condition fails then this one will be checked
#     print("You can drive when you are older")
# else:
#     print("You are not old enough")

# # Truthy and Falsy Examples


# username = "bob"
# password = 123

# if username and password:
#     print("logged in successfully")
# else:
#     print("unable to log in")

# print(bool(0))  # prints False
# print(bool(""))  # prints False
# print(bool(5))  # prints True
# print(bool("hi"))  # prints True


# Ternary Operators

# is_sunny = True
# going_Outside = "sunscreen?" if is_sunny else "umbrella?"
# print(going_Outside)  # prints sunscreen?

# is_friend = False
# can_message = "message allowed" if is_friend else "no message allowed"
# print(can_message)  # prints no message allowed


# Short Circuiting example

# is_Red = False
# is_Something = True

# if is_Red and is_Something:
#     print("something")

is_magician = True
is_expert = False

if is_magician and is_expert:
    print("you are a master magician")
elif is_magician and not is_expert:
    print("At least you're getting there.")  #
else:
    print("You need magic powers.")
