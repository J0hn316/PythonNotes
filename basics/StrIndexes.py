# Examples 

numbers = '01234567'

#[start:stop:stepOver]

print(numbers[:]) #all numbers  from the beginning to the end of string.

print(numbers[0:7:1]) # from first number (index 0) till seventh number, step by one.

print(numbers[0:7:2]) #from first number till seventh number, but step  by two - skipping every second number.

print(numbers[0:3])   # Output: 012

print(numbers[1:])    # Output:  1234567 - all   numbers starting from second number till the end of string

print(numbers[:5]) #Output: 01234 - all   numbers till fifth number

print(numbers[::1])   # Output: 01234567 (default step is 1, so it prints all elements)

print(numbers[-1])     # Output: 7 - last element in a string

print(numbers[::-1]) # Output:   76543210 -  reverse order of all characters in a string