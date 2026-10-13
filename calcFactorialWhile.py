number = int(input("Enter a Number: "))

x = 1
y = 1

while x < number:
    x += 1
    y *= x
print(int(y))