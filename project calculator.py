from tkinter import *

class calculator(Frame):
    def __init__(self):
        Frame.__init__(self, bg = 'gray')
        self.option_add('*font', 'arial 25 bold')
        self.pack(expand = YES , fill = BOTH)
        self.master.title('calculator')
        
        display = StringVar()
        obj = Entry(self, relief = RIDGE ,textvariable = display,justify = 'right' , bd = 20, bg = 'powder blue', width =30)
        obj.pack(side = TOP ,expand = YES, fill = BOTH)
        
        
        clearbutton = Button(self, text = 'clear', bg = 'red', bd = 3, command = lambda stored = display: stored.set(""))
        clearbutton.pack(side = TOP,expand = YES, fill = BOTH)
        
        for exp in ('987/', '456*', '123-', '0.*'):
            frame = Frame(self, bd = 3, bg ='black')
            frame.pack(side = TOP, expand = YES, fill = BOTH)
            for char in exp :
                butt = Button(frame, text = char, bg = 'black',fg ='white', command =lambda stored = display, ch= char: stored.set(stored.get()+ch))
                butt.pack(side = LEFT, expand = YES ,fill = BOTH)
        equal = Button(self, text = '=', bg = 'yellow', bd = 3, command = lambda a = display: evaluate(a))
        equal.pack(side = TOP , expand = YES, fill = BOTH)
def evaluate(stored):
    try:
        stored.set(eval(stored.get()))
    except:
        stored.set('Error')
        
calculator().mainloop()