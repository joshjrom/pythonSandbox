userInput = str(input("> "))
words = userInput.split(" ")
wordEmoji = {
    ":)": "Happy",
    ":(": "Sad"
}

output = ""
for word in words:
    output += wordEmoji.get(word, word) + " "

print(output)