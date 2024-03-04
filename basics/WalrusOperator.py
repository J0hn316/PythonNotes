a = "Hello"
if (n := len(a)) > 5:
    print(f"too long {n} elements")

while (n := len(a)) > 1:
    print(n)
    a = a[:-1]

print(a)
