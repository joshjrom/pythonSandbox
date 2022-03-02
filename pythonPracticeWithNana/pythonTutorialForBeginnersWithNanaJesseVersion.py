def days_to_minutes_and_seconds():
    user_input = int(input("Please enter a value here "))
    days_to_minutes = user_input * 24 * 60
    days_to_seconds = user_input * 24 * 60 * 60
    
    print(f"{user_input} days is {days_to_minutes} minutes \n{user_input} days is {days_to_seconds} seconds")


days_to_minutes_and_seconds()