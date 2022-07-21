Continue = True

while Continue == True:
    print("give me a number")
    tom = int(input(">"))
    if tom % 2 == 1:
        print("ungerade")
    else:print("gerade")
    print("do you want to continue")
    Input = input(">")
    if Input == "No":
        Continue = False



