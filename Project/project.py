from tkinter import *
import tkinter as tk
import tkinter.constants 
import tkinter.font as tkFont
from PIL import ImageTk,Image  
from tkinter import filedialog
from tkinter import ttk

class App:

    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=1200
        height=800
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

# ************ FILE ************ 

        File=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        File["font"] = ft
        File["fg"] = "#333333"
        File["justify"] = "center"
        File["text"] = "File"
        File.place(x=10,y=0,width=70,height=25)

        loadFile=tk.Button(root)
        loadFile["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        loadFile["font"] = ft
        loadFile["fg"] = "#000000"
        loadFile["justify"] = "center"
        loadFile["text"] = "Load Image"
        loadFile.place(x=10,y=30,width=70,height=25)
        loadFile["command"] = self.loadFile_command

        saveFile=tk.Button(root)
        saveFile["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        saveFile["font"] = ft
        saveFile["fg"] = "#000000"
        saveFile["justify"] = "center"
        saveFile["text"] = "Save Image"
        saveFile.place(x=10,y=60,width=70,height=25)
        saveFile["command"] = self.saveFile_command

# ************ FILE ************ 
    

# ************ EDIT ************ 

        Edit=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        Edit["font"] = ft
        Edit["fg"] = "#333333"
        Edit["justify"] = "center"
        Edit["text"] = "Edit"
        Edit.place(x=100,y=0,width=70,height=25)

        GButton_920=tk.Button(root)
        GButton_920["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_920["font"] = ft
        GButton_920["fg"] = "#000000"
        GButton_920["justify"] = "center"
        GButton_920["text"] = "Button"
        GButton_920.place(x=100,y=30,width=70,height=25)
        GButton_920["command"] = self.GButton_920_command

        GButton_417=tk.Button(root)
        GButton_417["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_417["font"] = ft
        GButton_417["fg"] = "#000000"
        GButton_417["justify"] = "center"
        GButton_417["text"] = "Button"
        GButton_417.place(x=100,y=60,width=70,height=25)
        GButton_417["command"] = self.GButton_417_command

        GButton_440=tk.Button(root)
        GButton_440["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_440["font"] = ft
        GButton_440["fg"] = "#000000"
        GButton_440["justify"] = "center"
        GButton_440["text"] = "Button"
        GButton_440.place(x=100,y=90,width=70,height=25)
        GButton_440["command"] = self.GButton_440_command

# ************ EDIT ************ 


    def loadFile_command(self):
        global input
        input = PhotoImage(file = '1.png')
        lbl = Label(image=input)
        lbl.grid(column=0,row=0)
        lbl.place(x=10,y=150,width=500,height=500)

    def saveFile_command(self):
        print("command")


    def GButton_920_command(self):
        print("command")


    def GButton_417_command(self):
        print("command")


    def GButton_440_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
