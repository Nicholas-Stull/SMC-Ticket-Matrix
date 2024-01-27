Matrix0 = {
    "AvSupport":"Just change the input",
    "Banner":"Not a Flyer, A banner",
    "HelpDesk":"Most likley a Password Reset",
    "Networking":"Not another Port",
    "Imaging":"Windows Update Again",
    "Printer":"Didn't you see the no black magic sign",
    "Misc":"Right, It goes in the square hole",
    "Security":"how hard is it to shut the door",
    "Server":"I'm not a server, I'm a person",
}
AvSupport = {
    'Event (Excluding Theater & Sac)': ['Adam', 'Gatlin'],
    'Instructional ': ['Tiffany', 'Daryl', 'Tyler', 'Adam', 'Gatlin'],
}
Banner= {
    'Access Security': 'Martin',
    'Backup': 'Martin',
    'Financial Aid': ['John', 'Dave', 'Martin'],
    'General': ['Martin', 'Dave'],
    'Human Resources': ['John', 'Dave', 'Martin'],
    'Payroll': ['John', 'Dave', 'Martin'],
    'Position Control': ['John', 'Dave', 'Martin'],
    'Registration': ['Dave', 'Martin', 'John'],
    'Self Service': ['Dave', 'Martin'],
    'Student': ['Dave', 'Walter', 'John', 'Martin'],
    'Technical': ['Martin', 'Dave', 'John'],
    'Web Tailor': ['Dave', 'Martin', 'Diana'],
    'Workflow': ['Diana', 'Martin'],
}

HelpDesk = {
    'Beaksquad': ['Matt', 'Adam', 'Gatlin'],
    'Management': ['Matt', 'Adam', 'Gatlin'],
    'SysAid': ['Matt', 'Daryl', 'Adam'],
    'Training': ['Tiffany', 'Martin', 'Daryl', 'Adam', 'Gatlin'],
}

Networking = {
    'AP Wireless': ['Allen', 'Daryl'],
    'Comcast': ['Allen', 'Daryl'],
    'Firewall': ['Allen', 'Daryl'],
    'Phones': ['Allen', 'Daryl'],
    'Switches ': ['Allen', 'Daryl'],
    'UPS': ['Allen', 'Daryl'],
    'Wiring': ['Allen', 'Daryl'],
    'DirecTV': ['Allen', 'Daryl'],
}
Imaging = {
    'MAC': ['Adam', 'Gatlin', 'Tyler'],
    'PC': ['Tyler', 'Adam', 'Gatlin', 'Tiffany', 'Daryl'],
}
Printer = {
    'CUPS': ['Manoj', 'John', 'Tyler', 'Martin'],
    'Hardware': ['Tyler', 'Adam', 'Gatlin'],
    'Papercut': ['Tyler', 'Adam', 'Gatlin', 'Manoj', 'Theresa'],
}
Misc = {
    'CrystalReport - Reporting': [],
    'CrystalReport/Logicity Installs': ['Tiffany', 'Tyler'],
    'Department Budgeting': ['Mick', 'Matt'],
    'Digital Signage (YoDeck)': ['Gatlin'],
    'ESM - Job Scheduler': ['John', 'Martin'],
    'Envisions - FormFusion ': ['John', 'Martin'],
    'Envisions - Intellecheck ': ['John', 'Martin'],
    'Filewave': ['Daryl', 'Matt', 'Adam', 'Jeanne'],
    'Google Administration': ['Dave', 'Gatlin', 'Manoj', 'Diana', 'John'],
    'Announcement Administrator': ['Dave', 'Diana'],
    'Asset Tiger -Inventory': ['Matt', 'Daryl', 'Tyler', 'Adam', 'Gatlin'],
    'LDAP - CAS User Authentication': ['Martin', 'Dave', 'Theresa'],
    'Life Ray (Wired) - Content': ['Theresa', 'Martin'],
    'LMS - Moodle': ['Martin'],
    'Presence': ['John'],
    'Program - Groovy/Grails': ['Dave', 'John'],
    'Program - PHP': ['Dave'],
    'Rave Administrator': ['Dave', 'Jeanne', 'Diana', 'Theresa'],
    'Software Licensing & Renewals': ['Mick', 'Matt', 'Jeanne', 'Tiffany', 'Theresa'],
    'Student Dashbaord': ['John', 'Dave'],
    'SysAid Admistrator': ['Matt', 'Daryl'],
    'Testing Center (Dowagiac)': ['Tyler', 'Allen', 'Tiffany', 'Daryl', 'Adam'],
    'TouchNet': ['Martin'],
    'Web - Swmich.edu': ['Diana']
}
Security = {
    'Administrator': ['Theresa', 'Manoj'],
    'Badges': ['Theresa', 'Tiffany'],
    'Cameras': ['Theresa', 'Tiffany'],
    'Door Secuirty': ['Theresa', 'Tiffany'],
}
Server = {
    'Active Directory Management': ['Matt', 'Allen', 'Manoj'],
    'Backups': ['Manoj'],
    'Cooling System': ['Eberhert'],
    'Hardware Support': ['Manoj', 'Allen'],
    'OS Maintance': ['Manoj', 'Tyler'],
    'Storage Adminstrator': ['Manoj', 'Allen'],
    'UPS': ['Eberhert', 'Allen'],
    'VMWare Adminstrator': ['Manoj', 'Allen', 'Tyler'],
    'Public & Open DNS': ['Manoj', 'Allen'],
    'Software Upgrade & Support': ['Manoj'],
}


# Defining what flavor message
Cat = ("Please Pick a Category: ")
ice_cream = True  # Set the ice_cream variable to True
Ope= ("Here are your options: ")
# Check if the user's choice is in the dictionary of flavors
while ice_cream == True:
    choice = input(Ope+ ", ".join(Matrix0) + "\n" + Cat).strip()
    if choice in Matrix0:
        print(f"You chose {choice}: {Cat[choice]}")

    else:
        # If the choice is not valid, display an error message
        print("Thats not an option, pick an option")

        # ", ".join(Matrix0.keys()) + "\n" + '.' + Ope).strip()
   
        # Display a random response + Your ice cream's coming up!
     #   ice_cream = False  # Set the ice_cream variable to False
      #  if choice == "AvSupport":
       #     AvSupport = input(Ope +  # Get user's choice of ice cream flavor
        #                   ", ".join(AvSupport.keys()) + "\n" + '.' + Op2).strip()
