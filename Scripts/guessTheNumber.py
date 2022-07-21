import random

RandomNumber = random.randrange(1, 50)

Continue = True

while Continue:
    print(RandomNumber)  #For testing
    Input = int(input("Guess a number between 1 and 50: "))
    if Input == RandomNumber:
        print("You scored")
        Continue = False
    elif Input < RandomNumber:
        print("You need to guess higher. Try Again")
    elif Input > RandomNumber:
        print("You need to guess lower. Try Again")
