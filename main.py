
import tkinter

from searchui import searchui
from LEPUI import lepui


#The code to generate the menu interface.
windows = tkinter.Tk()
windows.title('Chemical tools')
windows.geometry('350x350')  
labelName = tkinter.Label(windows, text='Welcome to the tools!', justify=tkinter.RIGHT, width=80)
labelName.place(x=0, y=5, width=300, height=20)
labelName = tkinter.Label(windows, text='Choose the tools you want to use:', justify=tkinter.RIGHT, width=80)
labelName.place(x=0, y=30, width=315, height=20)
# Binding the search tools interface
buttonsearch = tkinter.Button(windows, text='Search tools', command=searchui)
buttonsearch.place(x=30, y=100, width=100, height=50)
# Binding the lep tools interface
buttonlep = tkinter.Button(windows, text='Lep tools', command=lepui)
buttonlep.place(x=200, y=100, width=100, height=50)
windows.mainloop()





