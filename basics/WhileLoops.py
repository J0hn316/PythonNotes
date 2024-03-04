# While Loops Examples

i = 0
while i < 5:
    print(i)
    i += 1
# Output: 0 1 2 3 4

while i < 6:
    print(i)
    i += 1
else:
    print("done")

# Output: 0 1 2 3  4 5 done

while i < 6:
    print(i)
    i += 1
    break
else:
    print("done")
# Output : 0

# While loops vs for loops

my_list = [1, 2, 3]

for i in my_list:
    print(i)

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

while True:
    res = input("say something: ")
    if res == "bye":
        break
