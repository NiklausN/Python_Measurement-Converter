# Dev. Info:
#  - Developer: Niklaus Newport
#  - Website: HTTPS://NiklausNewport.Dev/
#  - E-Mail: Me@NiklausNewport.Dev (Business or Programming Related Inquiries Only)
#
# Program Info:
#  - Program Name: Converter
#  - Programming Language: Python
#  - Development Date Range: 30 June 2020 (One Day)
#  - Function of Program:
#    This is a simple program written in Python that can be used to convert Mass, Volume, Height,
#       Temperature, and other measurements to and from various measurement systems.

# Provide a Menu
print("Enter a Number from the selection below.")
print("┌──────────────────────────────┐")
print("│        1 = Temperature       │")
print("│        2 = Mass              │")
print("│        3 = Distance          │")
print("│        4 = Weight            │")
print("│        0 = Exit Program      │")
print("└──────────────────────────────┘")

# Retrieve Input from the User
inp1 = int(input("User: "))

# Execute the Users Selection
if inp1 == 1:  # Temperature

    # Import Temperature.py
    from Measurements import Temperature

    # Execute Temperature.py
    callable(Temperature)

elif inp1 == 2:  # Mass

    # Import Mass.py
    from Measurements import Mass

    # Execute Mass.py
    callable(Mass)

elif inp1 == 3:  # Distance

    # Import Distance.py
    from Measurements import Distance

    # Execute Distance.py
    callable(Distance)

elif inp1 == 4:  # Weight

    # Import Weight.py
    from Measurements import Weight

    # Execute Weight.py
    callable(Weight)

elif inp1 == 0:  # Exit Program

    # Say a Farewell
    print("Goodbye! Please come back again...")

    # Exit the Program
    exit(0)

else:

    # Provide an Error Message
    print("Error: An invalid selection has been made! Please rerun the program and try again.")
