n = int(input("Enter a Number: "))

x = 0
sumGauss = n * (n+1) // 2

for i in range(n + 1):
    x += i

print(x)
print(sumGauss)

if(x == sumGauss):
    print("My running sum code works correctly")
    
else:
    print("My running sum code failed badly")
    