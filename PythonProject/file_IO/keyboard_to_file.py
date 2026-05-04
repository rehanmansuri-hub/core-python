def keyboardtofilecopty():
    file = open("../files/keybpooard.txt","w")
    text = input("enter your message = ")

    while (text != "quit"):
        file.write(text)
        file.write("\n")
        text = input('')
    file.close()


keyboardtofilecopty()