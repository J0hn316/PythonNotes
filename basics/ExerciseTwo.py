username = input("Enter your username: ")
password = input("Enter password: ")

length = len(password)
stars = "*"  * length



print(f"Hello {username}, your password {stars} is {length} letters long.")