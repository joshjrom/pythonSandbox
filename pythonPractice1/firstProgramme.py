#Decision making of user inputed number
def check_arg():
	something = int(input("Enter your first number==>"))
	something_again = int(input("Enter your second number==>"))
	addition = something + something_again
	if addition > 100:
		print("You've exceeded the limit")
		check_arg()
	elif addition >= 70:
		return "You passed the course"
	elif addition < 70 and addition >= 60:
		return "You tried"
	else:
		return "You failed"

print(check_arg())
