def days_to_units(num_of_days_hours, num_of_days_minutes, num_of_days_seconds):
    days_to_hours = 24
    name_of_hours = "hours"
    days_to_minutes = 24 * 60
    name_of_minutes = "minutes"
    days_to_seconds = 24 * 60 * 60
    name_of_seconds = "seconds"
    print(f"{num_of_days_hours} days are in {num_of_days_hours * days_to_hours} {name_of_hours}")
    print(f"{num_of_days_minutes} days are in {num_of_days_minutes * days_to_minutes} {name_of_minutes}")
    print(f"{num_of_days_seconds} days are in {num_of_days_seconds * days_to_seconds} {name_of_seconds}")
    print("All good!")


days_to_units(20,20,20)