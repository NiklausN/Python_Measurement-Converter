# Dev. Info:
#  - Developer: Niklaus Newport
#  - Website: HTTPS://NiklausNewport.Dev/
#  - E-Mail: Me@NiklausNewport.Dev (Business or Programming Related Inquiries Only)
#
# Program Info:
#  - Program Name: Measurement Converter
#  - Programming Language: Python
#  - Development Date Range: 30 June 2020 (One Day)
#  - Function of Program:
#    This is a simple program written in Python that can be used to convert Mass, Volume, Height,
#       Temperature, and other measurements to and from various measurement systems.

# Provide a Menu
print("Type a Number From The Selection Below Then Click Enter.")
print("┌──────────────────────────────┐")
print("│        1 = Temperature       │")
print("│        2 = Mass              │")
print("│        3 = Length            │")
print("│        4 = Weight            │")
print("│        5 = Digital Storage   │")
print("│        6 = Fuel Economy      │")
print("│        7 = Pressure          │")
print("│        8 = Energy            │")
print("│        9 = Time              │")
print("│        10 = Volume           │")
print("│        11 = Area             │")
print("│        12 = Speed            │")
print("│        13 = Frequency        │")
print("│        0 = Exit Program      │")
print("└──────────────────────────────┘")

# Retrieve Input from the User
inp1 = str(input("User: "))

# Execute the Users Selection
if inp1 == '1':  # Temperature

    # Import Temperature.py
    from Measurements import Temperature

    # Execute Temperature.py
    callable(Temperature)

elif inp1 == '2':  # Mass

    # Import Mass.py
    from Measurements import Mass

    # Execute Mass.py
    callable(Mass)

elif inp1 == '3':  # Length

    # Import Length.py
    from Measurements import Length

    # Execute Length.py
    callable(Length)

elif inp1 == '4':  # Weight

    # Import Weight.py
    from Measurements import Weight

    # Execute Weight.py
    callable(Weight)

elif inp1 == '0':  # Exit Program

    # Say a Farewell
    print("Goodbye! Please come back again...")

    # Exit the Program
    exit(0)

else:

    # Provide an Error Message
    print("Error: An invalid selection has been made! Please rerun the program and try again.")

    # Terminate the Program
    exit(0)
