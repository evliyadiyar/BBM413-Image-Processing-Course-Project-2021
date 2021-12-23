from tkinter import *
import tkinter as tk
import tkinter.constants
import tkinter.font as tkFont
from tkinter.filedialog import askopenfile
from PIL import ImageGrab, ImageFilter
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import ttk


class App:

    def __init__(self, root):
        # setting title
        root.title("undefined")
        # setting window size
        width = 1200
        height = 800
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        # ************ FILE ************

        File = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        File["font"] = ft
        File["fg"] = "#333333"
        File["justify"] = "center"
        File["text"] = "File"
        File.place(x=10, y=0, width=70, height=25)

        loadFile = tk.Button(root)
        loadFile["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        loadFile["font"] = ft
        loadFile["fg"] = "#000000"
        loadFile["justify"] = "center"
        loadFile["text"] = "Load Image"
        loadFile.place(x=10, y=30, width=70, height=25)
        loadFile["command"] = self.loadFile_command

        saveFile = tk.Button(root)
        saveFile["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        saveFile["font"] = ft
        saveFile["fg"] = "#000000"
        saveFile["justify"] = "center"
        saveFile["text"] = "Save Image"
        saveFile.place(x=10, y=60, width=70, height=25)
        saveFile["command"] = self.saveFile_command

        # ************ FILE ************

        # ************ EDIT ************

        Edit = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        Edit["font"] = ft
        Edit["fg"] = "#333333"
        Edit["justify"] = "center"
        Edit["text"] = "Edit"
        Edit.place(x=100, y=0, width=70, height=25)

        blurbutton = tk.Button(root)
        blurbutton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        blurbutton["font"] = ft
        blurbutton["fg"] = "#000000"
        blurbutton["justify"] = "center"
        blurbutton["text"] = "Blur"
        blurbutton.place(x=100, y=30, width=70, height=25)
        blurbutton["command"] = self.blur_image

        GButton_417 = tk.Button(root)
        GButton_417["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        GButton_417["font"] = ft
        GButton_417["fg"] = "#000000"
        GButton_417["justify"] = "center"
        GButton_417["text"] = "Button"
        GButton_417.place(x=100, y=60, width=70, height=25)
        GButton_417["command"] = self.GButton_417_command

        GButton_440 = tk.Button(root)
        GButton_440["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        GButton_440["font"] = ft
        GButton_440["fg"] = "#000000"
        GButton_440["justify"] = "center"
        GButton_440["text"] = "Button"
        GButton_440.place(x=100, y=90, width=70, height=25)
        GButton_440["command"] = self.GButton_440_command

    # ************ EDIT ************

    def loadFile_command(self):
        global input
        global img_will_be_saved
        global img_will_be_changed

        path = askopenfile(filetypes=[("Image File", "*.jpg"), ("Image File", "*.png")])
        im = Image.open(path.name)
        imlist = im.size

        new_image = im.resize(
            (int(imlist[0] / 2), int(imlist[1] / 2)) if (int(imlist[0] ) > 600 or int(imlist[1]  ) > 600) else (
                imlist[0], imlist[1]))
        img_will_be_saved=new_image
        img_will_be_changed=path.name
        input = ImageTk.PhotoImage(new_image)
        lbl = Label(image=input)
        lbl.grid(column=0, row=0)
        lbl.place(x=0, y=260)



    def saveFile_command(self):
        img_will_be_saved.save("photsaved.jpg")


    def blur_image(self):
        global input
        global img_will_be_saved
        global img_will_be_changed
        try:
            path = img_will_be_changed
            im = Image.open(path)
            im = im.filter(ImageFilter.BLUR)
            img_will_be_saved = im
            imlist = im.size
            new_image = im.resize(
                (int(imlist[0] / 2), int(imlist[1] / 2)) if (int(imlist[0]) > 600 or int(imlist[1]) > 600) else (
                    imlist[0], imlist[1]))
            img_will_be_changed = ImageTk.PhotoImage(new_image)

            lbl = Label(image=img_will_be_changed)
            lbl.grid(column=0, row=0)
            lbl.place(x=600, y=150, width=600, height=600)
            print("blured")
        except:
            from tkinter import messagebox

            messagebox.showerror("Error", "U cannot use this process to this image.")


    def GButton_417_command(self):
        print("command")

    def GButton_440_command(self):
        print("command")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
