calculation_to_hours = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit}"


def validate_and_execute():
    try:

        user_input_number = int(number_of_days_element)
        if user_input_number > 0:
            calculated_number = days_to_units(user_input_number)
            print(calculated_number)
        elif user_input_number == 0:
            print("You entered a 0, please enter a number greater than 0")
        else:
            print("You entered a negative value, no conversion for you!")

    except ValueError:
        print("Your input is not a valid number. Don't ruin my program!")


user_input = ""
while user_input != "exit":
    user_input = input("Hey User, enter number of days as a comma separated list and I will convert it to hours!\n")
    print(type(user_input.split(",")))
    print(user_input.split(","))
    for number_of_days_element in user_input.split(","):
        validate_and_execute()


