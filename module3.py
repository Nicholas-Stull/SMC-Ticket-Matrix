# Nicholas Stull
# 02.17.2023
# Week 6 Hands On
# Module 3
# github.com/nicholas-stull
# Program Starts after this line at line 9
# --------------------------------------------------------------

import random # Import the random module
flavors = { # Dictionary of ice cream flavors
    "Code Crunch": "Vanilla ice cream with chunks of dark chocolate and a swirl of caramel.",
    "Raspberry Pi": "Raspberry ice cream with pieces of dark chocolate and a raspberry swirl.",
    "Root Beer Overflow": "Root beer flavored ice cream with a caramel swirl and chunks of toffee.",
    "Cyber Cookies and Cream": "Cookies and cream ice cream with chunks of Oreo cookies and a fudge swirl.",
    "Caramel Commando": "Caramel ice cream with a caramel swirl and chunks of pretzels.",
    "Java Jolt": "Coffee ice cream with a fudge swirl and chunks of chocolate-covered espresso beans.",
    "Digital Delight": "A mix of strawberry, blueberry, and raspberry ice cream with a berry swirl.",
    "The Dark Web": "Dark chocolate ice cream with a fudge swirl and chunks of chocolate fudge brownies.",
    "Robot Raspberry": "Raspberry ice cream with a raspberry swirl and chunks of dark chocolate.",
    "Mint Hack": "Mint ice cream with a fudge swirl and chunks of dark chocolate."
}
Matrix0 = ["AvSupport", "Banner", "HelpDesk", "Networking",
           "Imaging", "Printer", "Misc", "Security", "Server"]

welcome = (
    "Please Pick a Category: ")  # Defining Welcome message
whatFlavor = ("Which flavor would you like to get? ") # Defining what flavor message
ice_cream = True # Set the ice_cream variable to True
# Check if the user's choice is in the dictionary of flavors
while ice_cream == True:
    choice = input(welcome +  # Get user's choice of ice cream flavor
                   ", ".join(flavors.keys()) + "\n" + '.' + whatFlavor).strip()
    if choice in flavors:
        # If the choice is valid, display the name and description of the flavor
        print(f"You chose{choice}: {flavors[choice]}") # Display the name and description of the flavor
        print("Your ice cream's coming up!")  # Display a random response + Your ice cream's coming up!
        ice_cream = False # Set the ice_cream variable to False
    else:
        # If the choice is not valid, display an error message
        print("We don't currently have that flavor. Maybe we can add it. Until then, why don't you try a flavor we have.: " +
              ", ".join(flavors.keys()))
