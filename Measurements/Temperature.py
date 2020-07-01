# Provide a Menu
print("What unit are you converting from?")
print("┌──────────────────────────────┐")
print("│        1 = Celsius           │")
print("│        2 = Fahrenheit        │")
print("│        3 = Kelvin            │")
print("│        0 = Exit Program      │")
print("└──────────────────────────────┘")

# Retrieve Input from the User
inp1 = str(input("User: "))

# Execute Users Selection
if inp1 == '1':  # From Celsius

    # Provide a Menu
    print("What unit are you converting to?")
    print("┌──────────────────────────────┐")
    print("│        1 = Fahrenheit        │")
    print("│        2 = Kelvin            │")
    print("│        0 = Exit Program      │")
    print("└──────────────────────────────┘")

    # Retrieve Input from the User
    inp2 = str(input("User: "))

    # Execute Users Selection
    if inp2 == '1':  # To Fahrenheit

        # Retrieve Temperature Converting From
        print("What is the temperature in Celsius?")
        inp3 = float(input("User: "))

        # Convert the Temperature
        temp = ((inp3 * (9.00/5.00)) + 32.00)

        # Display the Results
        print(f'{inp3}° Celsius will convert to {temp}° Fahrenheit.')

    elif inp2 == '2':  # To Kelvin

        # Retrieve Temperature Converting From
        print("What is the temperature in Celsius?")
        inp3 = float(input("User: "))

        # Convert the Temperature
        temp = (inp3 + 273.15)

        # Display the Results
        print(f'{inp3}° Celsius will convert to {temp}° Kelvin.')

    elif inp2 == '0':  # Exit Program

        # Say a Farewell
        print("Goodbye! Please come back again...")

        # Exit the Program
        exit(0)

    else:

        # Provide an Error Message
        print("Error: An invalid selection has been made! Please rerun the program and try again.")

        # Terminate the Program
        exit(0)

elif inp1 == '2':  # From Fahrenheit

    # Provide a Menu
    print("What unit are you converting to?")
    print("┌──────────────────────────────┐")
    print("│        1 = Celsius           │")
    print("│        2 = Kelvin            │")
    print("│        0 = Exit Program      │")
    print("└──────────────────────────────┘")

    # Retrieve Input from the User
    inp2 = str(input("User: "))

    # Execute Users Selection

elif inp1 == '3':  # From Kelvin

    # Provide a Menu
    print("What unit are you converting to?")
    print("┌──────────────────────────────┐")
    print("│        1 = Fahrenheit        │")
    print("│        2 = Celsius           │")
    print("│        0 = Exit Program      │")
    print("└──────────────────────────────┘")

    # Retrieve Input from the User
    inp2 = str(input("User: "))

    # Execute Users Selection

elif inp1 == 0:  # Exit Program

    # Say a Farewell
    print("Goodbye! Please come back again...")

    # Exit the Program
    exit(0)

else:

    # Provide an Error Message
    print("Error: An invalid selection has been made! Please rerun the program and try again.")

    # Terminate the Program
    exit(0)
