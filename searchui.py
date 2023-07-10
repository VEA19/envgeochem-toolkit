
import tkinter
import tkinter.messagebox
from extraction import fuzzyextract, extract

def searchui():
    def fuzzy():
        searchtext  = entrytext.get()
        num = int(entrynum.get())
        if fuzzyextract(searchtext ,num):
            tkinter.messagebox.showinfo(title='userlogin', message='ok')
        else:
            tkinter.messagebox.showerror(title='userlogin', message='Error')
    
    #def normal():
     #  searchtext = entrytext2.get()
      #  if extract(searchtext):
       #     tkinter.messagebox.showinfo(title='userlogin', message='ok')
      #  else:
      #      tkinter.messagebox.showerror(title='userlogin', message='Error')
        
    def cancel():
        vartext1 .set('')
        varnum.set('')
        vartext2.set('')
     
    window = tkinter.Tk()
    window.title('SEARCH')
    window.geometry('750x300')
    vartext1 = tkinter.StringVar(value='')
    varnum = tkinter.StringVar(value='')
    vartext2 = tkinter.StringVar(value='')
    
    # Create the label for fuzzy search
    labelName = tkinter.Label(window, text='Search text', justify=tkinter.RIGHT, width=80)
    
    labelName.place(x=10, y=5, width=80, height=20)
    # Create the text box and the input text.
    entrytext = tkinter.Entry(window, width=80, textvariable=vartext1)
    entrytext.place(x=100, y=5, width=80, height=20)
    labelPwd = tkinter.Label(window, text='Number:', justify=tkinter.RIGHT, width=80)
    labelPwd.place(x=10, y=30, width=80, height=20)
    # Create the text box for the fuzzy number. 
    entrynum = tkinter.Entry(window,  width=80, textvariable=varnum)
    entrynum.place (x=100, y=30, width=80, height=20)
    
    # Create the buttons and the link related to them
    buttonOk = tkinter.Button(window, text='Search', command=fuzzy)
    buttonOk.place(x=10, y=70, width=100, height=20)
    buttonCancel = tkinter.Button(window, text='Cancel', command=cancel)
    buttonCancel.place(x=120, y=70, width=100, height=20)
    
    # Create the label for exact search 
    #labelName = tkinter.Label(window, text='Search text', justify=tkinter.RIGHT, width=80)
    #labelName.place(x=10, y=200, width=80, height=20)
    #entrytext2 = tkinter.Entry(window, width=80, textvariable=vartext2)
    #entrytext2.place(x=100, y=200, width=80, height=20)
    #buttonOk = tkinter.Button(window, text='Search', command=normal)
    #buttonOk.place(x=10, y=270, width=50, height=20)
    #buttonCancel = tkinter.Button(window, text='Cancel', command=cancel)
    #buttonCancel.place(x=120, y=270, width=50, height=20)
    # Loop show the interface
    labelName = tkinter.Label(window, text='Input related text, for example zncit for Zncitrate', justify=tkinter.RIGHT, width=80)
    
    labelName.place(x=180, y=5, width=300, height=20)
    
    labelName = tkinter.Label(window, text='Input the related result numbers you want to return (suggested range : 15-25)', justify=tkinter.RIGHT, width=80)
    
    labelName.place(x=170, y=30, width=500, height=20)
    
    labelName = tkinter.Label(window, text='Press search to complete the search or cancel to empty the input boxes.', justify=tkinter.RIGHT, width=80)
    
    labelName.place(x=50, y=100, width=480, height=20)
    
    #labelName = tkinter.Label(window, text='Input the specific text you want to search e.g ZnCitrate, Make sure the low and upper case is exactly the same.', justify=tkinter.RIGHT, width=80)
    
    #labelName.place(x=10, y=220, width=600, height=20)
    
    window .mainloop()

searchui()