def readposint():
    while True:
        value = input("Enter a positive integer please (any int greater than zero): ")
        try:
            num = int(value)
            if num > 0:
                return num
            else:
                print("That is not a positive integer.. Please enter an postive integer.")
        except ValueError:
            print("A valid integer was not entered. Please enter a valid and positive integer.")

print(readposint())