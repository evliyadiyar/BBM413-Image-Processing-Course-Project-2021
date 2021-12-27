from tkinter import *
import tkinter as tk
import tkinter.constants
import tkinter.font as tkFont
from tkinter.filedialog import askopenfile
from PIL import ImageGrab, ImageFilter
from PIL import ImageTk, Image, ImageEnhance
from skimage.util import random_noise
from tkinter import filedialog
from tkinter import ttk

import PIL
import cv2
import numpy as np


def noise(img):
    # Generate Gaussian noise
    gauss = np.random.normal(0, 1, img.size)
    if(len(img.shape)>2):
        gauss = gauss.reshape(img.shape[0], img.shape[1], img.shape[2]).astype('uint8')
    else:
        gauss = gauss.reshape(img.shape[0], img.shape[1]).astype('uint8')
    # Add the Gaussian noise to the image
    img_gauss = cv2.add(img, gauss)
    return img_gauss


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

        Crop = tk.Button(root)
        Crop["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        Crop["font"] = ft
        Crop["fg"] = "#000000"
        Crop["justify"] = "center"
        Crop["text"] = "Crop"
        Crop.place(x=100, y=60, width=70, height=25)
        Crop["command"] = self.Crop_command

        Flip = tk.Button(root)
        Flip["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        Flip["font"] = ft
        Flip["fg"] = "#000000"
        Flip["justify"] = "center"
        Flip["text"] = "Flip"
        Flip.place(x=100, y=90, width=70, height=25)
        Flip["command"] = self.Flip_command

        Mirror = tk.Button(root)
        Mirror["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        Mirror["font"] = ft
        Mirror["fg"] = "#000000"
        Mirror["justify"] = "center"
        Mirror["text"] = "Mirror"
        Mirror.place(x=100, y=120, width=70, height=25)
        Mirror["command"] = self.Mirror_command

        Rotate = tk.Button(root)
        Rotate["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        Rotate["font"] = ft
        Rotate["fg"] = "#000000"
        Rotate["justify"] = "center"
        Rotate["text"] = "Rotate"
        Rotate.place(x=100, y=150, width=70, height=25)
        Rotate["command"] = self.Rotate_command

        InverseColor = tk.Button(root)
        InverseColor["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        InverseColor["font"] = ft
        InverseColor["fg"] = "#000000"
        InverseColor["justify"] = "center"
        InverseColor["text"] = "Inverse Color"
        InverseColor.place(x=200, y=30, width=70, height=25)
        InverseColor["command"] = self.InverseColor_command

        ChangeRGB = tk.Button(root)
        ChangeRGB["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        ChangeRGB["font"] = ft
        ChangeRGB["fg"] = "#000000"
        ChangeRGB["justify"] = "center"
        ChangeRGB["text"] = "ChangeRGB"
        ChangeRGB.place(x=200, y=60, width=70, height=25)
        ChangeRGB["command"] = self.ChangeRGB_command

        Button5 = tk.Button(root)
        Button5["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        Button5["font"] = ft
        Button5["fg"] = "#000000"
        Button5["justify"] = "center"
        Button5["text"] = "Deblur"
        Button5.place(x=200, y=90, width=70, height=25)
        Button5["command"] = self.deblur_image

        Button6 = tk.Button(root)
        Button6["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        Button6["font"] = ft
        Button6["fg"] = "#000000"
        Button6["justify"] = "center"
        Button6["text"] = "adjust_brightness"
        Button6.place(x=200, y=120, width=70, height=25)
        Button6["command"] = self.adjust_brightness

        Button7 = tk.Button(root)
        Button7["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        Button7["font"] = ft
        Button7["fg"] = "#000000"
        Button7["justify"] = "center"
        Button7["text"] = "adjust_contrast"
        Button7.place(x=200, y=150, width=70, height=25)
        Button7["command"] = self.adjust_contrast

        Button8 = tk.Button(root)
        Button8["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        Button8["font"] = ft
        Button8["fg"] = "#000000"
        Button8["justify"] = "center"
        Button8["text"] = "add noise"
        Button8.place(x=200, y=180, width=70, height=25)
        Button8["command"] = self.add_noise

        Button9 = tk.Button(root)
        Button9["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        Button9["font"] = ft
        Button9["fg"] = "#000000"
        Button9["justify"] = "center"
        Button9["text"] = "adjust saturation"
        Button9.place(x=100, y=180, width=70, height=25)
        Button9["command"] = self.adjust_saturation

        Edges = tk.Button(root)
        Edges["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        Edges["font"] = ft
        Edges["fg"] = "#000000"
        Edges["justify"] = "center"
        Edges["text"] = "detect edges"
        Edges.place(x=300, y=30, width=70, height=25)
        Edges["command"] = self.detect_Edges

    # ************ EDIT ************

    def loadFile_command(self):
        global input
        global img_will_be_saved
        global img_will_be_changed

        path = askopenfile(filetypes=[("Image File", "*.jpg"), ("Image File", "*.png")])
        im = Image.open(path.name)
        imlist = im.size

        new_image = im.resize(
            (int(imlist[0] / 3), int(imlist[1] / 3)) if (int(imlist[0]) > 600 or int(imlist[1]) > 600) else (
                imlist[0], imlist[1]))
        img_will_be_saved = new_image
        img_will_be_changed = path.name
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

            im = img_will_be_saved
            im = im.filter(ImageFilter.BLUR)
            img_will_be_saved = im
            imlist = im.size
            new_image = im.resize(
                (int(imlist[0] / 3), int(imlist[1] / 3)) if (int(imlist[0]) > 600 or int(imlist[1]) > 600) else (
                    imlist[0], imlist[1]))
            img_will_be_changed = ImageTk.PhotoImage(new_image)

            lbl = Label(image=img_will_be_changed)
            lbl.grid(column=0, row=0)
            lbl.place(x=600, y=150, width=600, height=600)
            print("blured")
        except:
            from tkinter import messagebox

            messagebox.showerror("Error", "U cannot use this process to this image.")

    def deblur_image(self):
        global input
        global img_will_be_saved
        global img_will_be_changed
        try:

            im = img_will_be_saved
            enhancer = ImageEnhance.Sharpness(im)
            im = enhancer.enhance(2)
            img_will_be_saved = im
            imlist = im.size
            new_image = im.resize(
                (int(imlist[0] / 3), int(imlist[1] / 3)) if (int(imlist[0]) > 600 or int(imlist[1]) > 600) else (
                    imlist[0], imlist[1]))
            img_will_be_changed = ImageTk.PhotoImage(new_image)

            lbl = Label(image=img_will_be_changed)
            lbl.grid(column=0, row=0)
            lbl.place(x=600, y=150, width=600, height=600)
            print("not working properly look at that later!!")
        except:
            from tkinter import messagebox

            messagebox.showerror("Error", "U cannot use this process to this image.")

    def Crop_command(self):

        global input
        global img_will_be_saved
        global img_will_be_changed

        im = img_will_be_saved

        root2 = Tk()
        root2.title("crop sizes left right uppper lower")
        root2.geometry("400x400")

        left = tk.Text(root2, height=1)
        left.pack()

        top = tk.Text(root2, height=1)
        top.pack()

        right = tk.Text(root2, height=1)
        right.pack()

        bottom = tk.Text(root2, height=1)
        bottom.pack()

        def getTextInput():
            global lresult
            global rresult
            global tresult
            global bresult
            lresult = int(left.get("1.0", tk.END + "-1c"))
            rresult = int(right.get("1.0", tk.END + "-1c"))
            tresult = int(top.get("1.0", tk.END + "-1c"))
            bresult = int(bottom.get("1.0", tk.END + "-1c"))

        l = Label(root2, text="Type pixels for the crop. Example: 50,50,200,200")
        l.pack()
        b2 = Button(root2, text='finish', command=root2.destroy)
        b2.pack(side='bottom')
        b = Button(root2, text='apply', command=getTextInput)
        b.pack(side='bottom')

        root2.wait_window(b)
        im1 = im.crop((lresult, tresult, rresult, bresult))

        print("croppped")
        img_will_be_saved = im1
        imlist = im1.size
        new_image = im1.resize(
            (int(imlist[0] / 3), int(imlist[1] / 3)) if (int(imlist[0]) > 600 or int(imlist[1]) > 600) else (
                imlist[0], imlist[1]))
        img_will_be_changed = ImageTk.PhotoImage(new_image)

        lbl = Label(image=img_will_be_changed)
        lbl.grid(column=0, row=0)
        lbl.place(x=600, y=150, width=600, height=600)

    def Flip_command(self):
        global input
        global img_will_be_saved
        global img_will_be_changed
        try:

            im = img_will_be_saved
            im = im.transpose(Image.FLIP_TOP_BOTTOM)
            img_will_be_saved = im
            imlist = im.size
            new_image = im.resize(
                (int(imlist[0] / 3), int(imlist[1] / 3)) if (int(imlist[0]) > 600 or int(imlist[1]) > 600) else (
                    imlist[0], imlist[1]))
            img_will_be_changed = ImageTk.PhotoImage(new_image)

            lbl = Label(image=img_will_be_changed)
            lbl.grid(column=0, row=0)
            lbl.place(x=600, y=150, width=600, height=600)
            print("flipped")
        except:
            from tkinter import messagebox

            messagebox.showerror("Error", "U cannot use this process to this image.")
        print("command")

    def Mirror_command(self):
        global input
        global img_will_be_saved
        global img_will_be_changed
        try:

            im = img_will_be_saved
            im = im.transpose(Image.FLIP_LEFT_RIGHT)
            img_will_be_saved = im
            imlist = im.size
            new_image = im.resize(
                (int(imlist[0] / 3), int(imlist[1] / 3)) if (int(imlist[0]) > 600 or int(imlist[1]) > 600) else (
                    imlist[0], imlist[1]))
            img_will_be_changed = ImageTk.PhotoImage(new_image)

            lbl = Label(image=img_will_be_changed)
            lbl.grid(column=0, row=0)
            lbl.place(x=600, y=150, width=600, height=600)
        except:
            from tkinter import messagebox

            messagebox.showerror("Error", "U cannot use this process to this image.")
        print("command")

    def Rotate_command(self):
        global input
        global img_will_be_saved
        global img_will_be_changed
        try:

            im = img_will_be_saved
            im = im.transpose(Image.ROTATE_90)
            img_will_be_saved = im
            imlist = im.size
            new_image = im.resize(
                (int(imlist[0] / 3), int(imlist[1] / 3)) if (int(imlist[0]) > 600 or int(imlist[1]) > 600) else (
                    imlist[0], imlist[1]))
            img_will_be_changed = ImageTk.PhotoImage(new_image)

            lbl = Label(image=img_will_be_changed)
            lbl.grid(column=0, row=0)
            lbl.place(x=600, y=150, width=600, height=600)
        except:
            from tkinter import messagebox

            messagebox.showerror("Error", "U cannot use this process to this image.")
        print("command")

    def InverseColor_command(self):
        global input
        global img_will_be_saved
        global img_will_be_changed


        im = img_will_be_saved
        im = PIL.ImageOps.invert(im)
        img_will_be_saved = im
        imlist = im.size
        new_image = im.resize(
            (int(imlist[0] / 3), int(imlist[1] / 3)) if (int(imlist[0]) > 600 or int(imlist[1]) > 600) else (
                imlist[0], imlist[1]))
        img_will_be_changed = ImageTk.PhotoImage(new_image)

        lbl = Label(image=img_will_be_changed)
        lbl.grid(column=0, row=0)
        lbl.place(x=600, y=150, width=600, height=600)


        print("command")
    def detect_Edges(self):
        global input
        global img_will_be_saved
        global img_will_be_changed


        im = img_will_be_saved
        im_array=np.array(im)
        gray = cv2.cvtColor(im_array, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, threshold1=30, threshold2=100)
        im=Image.fromarray(edges)

        img_will_be_saved = im
        imlist = im.size
        new_image = im.resize(
            (int(imlist[0] / 3), int(imlist[1] / 3)) if (int(imlist[0]) > 600 or int(imlist[1]) > 600) else (
                imlist[0], imlist[1]))
        img_will_be_changed = ImageTk.PhotoImage(new_image)

        lbl = Label(image=img_will_be_changed)
        lbl.grid(column=0, row=0)
        lbl.place(x=600, y=150, width=600, height=600)

        print("command")

    def ChangeRGB_command(self):
        global input
        global img_will_be_saved
        global img_will_be_changed

        im = img_will_be_saved

        arr = np.array(im)
        asize = arr.shape

        root3 = Tk()
        root3.title("crop sizes left right uppper lower")
        root3.geometry("400x400")

        name_var = tk.IntVar()
        red = tk.Text(root3, height=1)
        red.pack()

        name_var2 = tk.IntVar()
        green = tk.Text(root3, height=1)
        green.pack()

        name_var3 = tk.IntVar()
        blue = tk.Text(root3, height=1)
        blue.pack()

        def getTextInput():
            global redresult
            global greenresult
            global blueresult

            redresult = int(red.get("1.0", tk.END + "-1c"))
            greenresult = int(green.get("1.0", tk.END + "-1c"))
            blueresult = int(blue.get("1.0", tk.END + "-1c"))

        l = Label(root3, text="Type red green blue ")
        l.pack()
        b2 = Button(root3, text='finish', command=root3.destroy)
        b2.pack(side='bottom')
        b = Button(root3, text='apply', command=getTextInput)
        b.pack(side='bottom')

        root3.wait_window(b)

        for j in range(asize[0] - 10):
            for i in range(asize[1] - 10):
                [r, g, b] = im.getpixel((i, j))
                r = redresult
                g = greenresult
                b = blueresult
                value = (r, g, b)
                im.putpixel((i, j), value)

        img_will_be_saved = im
        imlist = im.size
        new_image = im.resize(
            (int(imlist[0] / 3), int(imlist[1] / 3)) if (int(imlist[0]) > 600 or int(imlist[1]) > 600) else (
                imlist[0], imlist[1]))
        img_will_be_changed = ImageTk.PhotoImage(new_image)

        lbl = Label(image=img_will_be_changed)
        lbl.grid(column=0, row=0)
        lbl.place(x=600, y=150, width=600, height=600)

    def adjust_brightness(self):
        global input
        global img_will_be_saved
        global img_will_be_changed

        im = img_will_be_saved

        root3 = Tk()
        root3.title("brightness")
        root3.geometry("400x400")

        name_var = tk.StringVar()
        red = tk.Text(root3, height=1)
        red.pack()

        def getTextInput():
            global redresult
            redresult = float(red.get("1.0", tk.END + "-1c"))

        l = Label(root3, text="Type a value to adjust brightness of image.")
        l.pack()
        b2 = Button(root3, text='finish', command=root3.destroy)
        b2.pack(side='bottom')
        b = Button(root3, text='apply', command=getTextInput)
        b.pack(side='bottom')

        root3.wait_window(b)

        factor = redresult
        img_brightness_obj = ImageEnhance.Brightness(im)
        im = img_brightness_obj.enhance(factor)

        img_will_be_saved = im
        imlist = im.size
        new_image = im.resize(
            (int(imlist[0] / 3), int(imlist[1] / 3)) if (int(imlist[0]) > 600 or int(imlist[1]) > 600) else (
                imlist[0], imlist[1]))
        img_will_be_changed = ImageTk.PhotoImage(new_image)

        lbl = Label(image=img_will_be_changed)
        lbl.grid(column=0, row=0)
        lbl.place(x=600, y=150, width=600, height=600)

    def adjust_contrast(self):
        global input
        global img_will_be_saved
        global img_will_be_changed

        im = img_will_be_saved

        root3 = Tk()
        root3.title("contrast")
        root3.geometry("400x400")

        name_var = tk.StringVar()
        red = tk.Text(root3, height=1)
        red.pack()

        def getTextInput():
            global redresult
            redresult = float(red.get("1.0", tk.END + "-1c"))

        l = Label(root3, text="Type a value to adjust contrast of image.")
        l.pack()
        b2 = Button(root3, text='finish', command=root3.destroy)
        b2.pack(side='bottom')
        b = Button(root3, text='apply', command=getTextInput)
        b.pack(side='bottom')

        root3.wait_window(b)

        factor = redresult
        img_brightness_obj = ImageEnhance.Contrast(im)
        im = img_brightness_obj.enhance(factor)

        img_will_be_saved = im
        imlist = im.size
        print(im.size)
        new_image = im.resize(
            (int(imlist[0] / 3), int(imlist[1] / 3)) if (int(imlist[0]) > 650 or int(imlist[1]) > 650) else (
                imlist[0], imlist[1]))
        img_will_be_changed = ImageTk.PhotoImage(new_image)

        lbl = Label(image=img_will_be_changed)
        lbl.grid(column=0, row=0)
        lbl.place(x=600, y=150, width=600, height=600)

    def adjust_saturation(self):
        global input
        global img_will_be_saved
        global img_will_be_changed

        im = img_will_be_saved

        img_enhanced=ImageEnhance.Color(im)
        root3 = Tk()
        root3.title("contrast")
        root3.geometry("400x400")

        name_var = tk.StringVar()
        red = tk.Text(root3, height=1)
        red.pack()

        def getTextInput():
            global redresult
            redresult = float(red.get("1.0", tk.END + "-1c"))

        l = Label(root3, text="Type a value to adjust contrast of image.")
        l.pack()
        b2 = Button(root3, text='finish', command=root3.destroy)
        b2.pack(side='bottom')
        b = Button(root3, text='apply', command=getTextInput)
        b.pack(side='bottom')

        root3.wait_window(b)

        factor = redresult
        im=img_enhanced.enhance(factor)





        img_will_be_saved = im
        imlist = im.size
        print(im.size)
        new_image = im.resize(
            (int(imlist[0] / 3), int(imlist[1] / 3)) if (int(imlist[0]) > 650 or int(imlist[1]) > 650) else (
                imlist[0], imlist[1]))
        img_will_be_changed = ImageTk.PhotoImage(new_image)

        lbl = Label(image=img_will_be_changed)
        lbl.grid(column=0, row=0)
        lbl.place(x=600, y=150, width=600, height=600)

    def add_noise(self):
        global input
        global img_will_be_saved
        global img_will_be_changed

        im = img_will_be_saved
        np_im = np.array(im)
        np_im = noise(np_im)
        im = Image.fromarray(np_im)
        img_will_be_saved = im
        imlist = im.size

        new_image = im.resize(
            (int(imlist[0] / 3), int(imlist[1] / 3)) if (int(imlist[0]) > 650 or int(imlist[1]) > 650) else (
                imlist[0], imlist[1]))
        img_will_be_changed = ImageTk.PhotoImage(new_image)

        lbl = Label(image=img_will_be_changed)
        lbl.grid(column=0, row=0)
        lbl.place(x=600, y=150, width=600, height=600)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
