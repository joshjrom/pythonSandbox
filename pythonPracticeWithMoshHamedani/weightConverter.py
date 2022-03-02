

def prompt():

    def firstStep() :
        userInput = input("Enter weight number: ")
        return userInput

    def secondStep():
        unit = input("(L)lbs or (K)g: ")
        return unit

    try:
        userEntry = firstStep()
        if userEntry.lower() == "stop":
            return
        weight = float(userEntry)
    except:
        print("Please enter a number")
        prompt()

    unitFromUser = secondStep

    if unitFromUser.upper() == "L":
        converted = round(weight * 0.45, 2) 
        print(f"Weight {weight} is converted to {converted} kilos")


    elif unitFromUser.upper() == "K":
        converted = round(weight // 0.45, 2)
        print(f"Weight {weight} is converted to {converted} pounds")

    else:
        print("Please type either L or K")
        secondStep()

prompt()
