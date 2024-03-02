#Examples of immutability

something = 'Hello, World!'

something[0] = '8'   # This will raise an error because strings are immutable in Python.

# You will need to completely replace the string with a new one if you want to change it. 
# This will create a new string in memory.
something = '8'
something = something + "I'm back"