givenNumber = int(input("Enter a Number: "))

guessNumber = 0

if(givenNumber < 0):
    print("Square root of negative numbers is not a real number.")

else:
    while guessNumber**2 < givenNumber:
        guessNumber += 1        
    if(guessNumber**2 == givenNumber):
        print("Square root is:", guessNumber )
    
    elif(guessNumber**2 > givenNumber):
        print("Number is not a perfect square.")