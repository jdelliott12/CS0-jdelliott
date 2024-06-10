def weekday_name(weekday_number):
    if weekday_number == 0:
        return "Sunday"
    elif weekday_number == 1:
        return "Monday"
    elif weekday_number == 2:
        return "Tuesday"
    elif weekday_number == 3:
        return "Wednesday"
    elif weekday_number == 4:
        return "Thursday"
    elif weekday_number == 5:
        return "Friday"
    elif weekday_number == 6:
        return "Saturday"
    else:
        return "Incorrect number for Weekday"
    

for i in range(7):
    print("Weekday", i, "is", weekday_name(i))

weekday_number = int(input("Hello, enter a weekday number (0-6): "))
print("Day", weekday_number, "is", weekday_name(weekday_number))
    