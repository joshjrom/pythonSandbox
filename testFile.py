command = "".lower()

while True:
    userInput = input("> ").lower()
    if userInput == "start":
        print("Car started and ready to go!")
    elif userInput == "stop":
        print("Car stopped")
    elif userInput == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif userInput == "quit":
        print("The programme has stopped")
        break
    else:
        print("I don't understand" )

