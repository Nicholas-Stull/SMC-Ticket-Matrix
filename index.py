import PySimpleGUI as sg

sg.theme('Dark Grey 13')# Add a touch of color
# All the stuff inside your window.
layout = [
[sg.Text("The ouput will show the Primary first, then secondary, then tertiary")],
[sg.Text("Enter what you're working on"), sg.InputText()],
window['-TEXT-'].update(values="One")
[sg.Button('Enter'), sg.Button('Cancel')]
]
Matrix = {  # Dictionary of duties per person
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
# Create the Window
window = sg.Window('SMC Ticket Matrix', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()