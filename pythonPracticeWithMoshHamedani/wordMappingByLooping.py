userInput = str(input("Phone: "))
phoneMapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}

output = ""
for ch in userInput: 
    output += phoneMapping.get(ch, "!") + " "
    

print(output)