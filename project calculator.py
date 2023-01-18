from tkinter import *

class calculator(Frame):
    def __init__(self):
        # Initialize the frame with a gray background
        Frame.__init__(self, bg = 'gray')
        
        # Set the font for all widgets in the frame
        self.option_add('*font', 'arial 25 bold')
        
        # Pack the frame to fill the entire window
        self.pack(expand = YES , fill = BOTH)
        
        # Set the title of the window
        self.master.title('calculator')
        
        # Create a variable to store the input and output
        display = StringVar()
        
        # Create the input field (an Entry widget)
        obj = Entry(self, relief = RIDGE ,textvariable = display,justify = 'right' , bd = 20, bg = 'powder blue', width =30)
        obj.pack(side = TOP ,expand = YES, fill = BOTH)
        
        # Create the "clear" button
        clearbutton = Button(self, text = 'clear', bg = 'red', bd = 3, command = lambda stored = display: stored.set(""))
        clearbutton.pack(side = TOP,expand = YES, fill = BOTH)
        
        # Create the buttons for digits and mathematical operators
        for exp in ('987/', '456*', '123-', '0.*'):
            frame = Frame(self, bd = 3, bg ='black')
            frame.pack(side = TOP, expand = YES, fill = BOTH)
            for char in exp :
                butt = Button(frame, text = char, bg = 'black',fg ='white', command =lambda stored = display, ch= char: stored.set(stored.get()+ch))
                butt.pack(side = LEFT, expand = YES ,fill = BOTH)
        
        # Create the "=" button
        equal = Button(self, text = '=', bg = 'yellow', bd = 3, command = lambda a = display: evaluate(a))
        equal.pack(side = TOP , expand = YES, fill = BOTH)
        
# Function to evaluate the input expression
def evaluate(stored):
    try:
        stored.set(eval(stored.get()))
    except:
        stored.set('Error')
        
# Create an instance of the calculator class and start the event loop
calculator().mainloop()
