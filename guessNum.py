from secretNumber import secretNum

attempts = 0

while True:
    GuessNum = int(input("Guess Number: "))
    
    attempts += 1

    if(secretNum == GuessNum):
        print("the same")
        break
    
    elif(secretNum < GuessNum):
        print("too high")

    elif(secretNum > GuessNum):
        print("too low")
    
    if(attempts == 5):
        while True:
            print("Oh! Noooo...")