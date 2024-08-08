# Import the Tkinter Module
from tkinter import *

# Define the press Function
def press(event):
    global expression                             # make expression globally accessible
    text = event.widget.cget("text")              #  get the current text displayed on the button that triggered the event and store it in a variable

    # if '=' is pressed , evaluate the expression and the result is stored in expression & set the value of expression to the variable data 
    if text == "=":
        try:
            expression = str(eval(expression))
            data.set(expression)
        except Exception as e:
            data.set("Error")
            expression = ""

    # if 'C' is pressed , empty the expression, & set the value of expression to the variable data
    elif text == "C":
        expression = ""
        data.set(expression)

    # if any button other than '= or 'C' is pressed , append the string expression & set the value of expression to the variable data
    else:
        expression += text
        data.set(expression)
    
# Create the Main Window
window = Tk()
window.geometry("400x400")
window.title("CALCULATOR")

# Initialize Variables
expression = ""
data = StringVar()

# Create and Pack the Display Entry Widget
inp = Entry(window, textvar = data, font = "lucida 20 bold", justify='right')
inp.pack(padx=10,pady=10,ipady=10)

# Create and Pack the Frame for Buttons
button_frame = Frame(window)
button_frame.pack()

# Define the Buttons  
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Place the buttons in the Frame
r = 0
c = 0
for button_text in buttons:
    b = Button(button_frame, text = button_text, font = "lucida 15 bold", padx = 20, pady = 20)
    b.grid(row = r, column = c, padx = 10, pady = 10)
    b.bind("<Button-1>", press)         # bind left click of button with the event press    
    c += 1                              # increment grid position to next column 
    if(c > 3):                          # if column > 3, increment grid position to first position of next row
        c = 0
        r += 1

# Run the Main Event Loop
window.mainloop()
