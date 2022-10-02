def emojiGreeting(userInput):
    words = userInput.split(" ")
    wordEmoji = {
    ":)": "[Happy Emoji]",
    ":(": "[Sad Emoji]"
    }
    
    output = ""
    for word in words:
        output += wordEmoji.get(word, word) + " "
    return output

try:
    userInput = str(input("> "))
    if userInput is not str:
        print("Please input a string")
        userInput = str(input("> "))
    else:
        print(emojiGreeting(userInput))
except: 
    print("The seems to be a problem; Please ensure you input a string")



