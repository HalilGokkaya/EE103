givenNumber = int(input("Enter a Number: "))

guessNumber = 0

if(givenNumber < 0):
    isNegative = True
else:
    isNegative = False
    
while guessNumber**3 < abs(givenNumber):
    guessNumber += 1
    
if(guessNumber**3 == abs(givenNumber)):
    if(isNegative == True):
        print("Cube root is:", -guessNumber)
    else:
        print("Cube root is:", guessNumber)
elif(guessNumber**3 > abs(givenNumber)):
    print("Number is not a perfect cube.")