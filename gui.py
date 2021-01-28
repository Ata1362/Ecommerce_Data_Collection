import cv2 as cv
import tkinter as tk
from PIL import ImageTk, Image
import tkinter.font as font

jmb = 5
lng = 3
rnd = 5


def start():
    print("The procedure is started")
    rs = var_one.get()
    print("the value of Ali is: ", rs)


def checkinout():
    print("Input applied")


def stop_button():
    win.destroy()
    win2.destroy()





# Defining the Second Window
win2 = tk.Tk()
win2.geometry("700x50")
win2.title("Live camera")

# Setting up the first Window
win = tk.Tk()
win.title("Pistachio Type Sorter")
label = tk.Label(win, text="Please adjust the parameters")
label.grid(row=0, column=2, columnspan=4)

# Setting the windows Icons.
win.iconbitmap("ali.ico")
win2.iconbitmap("camera.ico")

# Designing the Menus

our_menu = tk.Menu(win)
win.config(menu=our_menu)
camera_setting = tk.Menu(our_menu)
our_menu.add_cascade(label='Camera Setting', menu=camera_setting)

filter_menu = tk.Menu(our_menu)
our_menu.add_cascade(label='Filters', menu=filter_menu)

Encoder_setting = tk.Menu(our_menu)
our_menu.add_cascade(label='Encoder Setting', menu=Encoder_setting)

button = tk.Button(win, text="Start", command=start, pady=15, padx=25, bg='green', fg='white', font=35).grid(row=2, column=1, sticky=tk.W)
button2 = tk.Button(win, text="Stop", fg="white", command=stop_button, pady=15, padx=25, font=35, bg='red').grid(row=3, column=1, sticky=tk.W)

# Showing the results

tex1 = "We have detected {} of participant".format(jmb)
tex2 = "We have detected {} of Males".format(lng)
tex3 = "We have detected {} of Females".format(rnd)
label1 = tk.Label(win, text=tex1).grid(row=8, column=2)
label2 = tk.Label(win, text=tex2).grid(row=9, column=2)
label3 = tk.Label(win, text=tex3).grid(row=10, column=2)


var_one = tk.IntVar()

#, text="design", variable=ali
# Design the checkboxes & the text
picheck = tk.Checkbutton(win, text="design", variable=var_one).grid(row=2, column=4)
barcheck = tk.Checkbutton(win).grid(row=2, column=3)
scattercheck = tk.Checkbutton(win).grid(row=2, column=5)


# Design a bar to define the parameters.

pie_label = tk.Label(win, text="Pie").grid(row=1, column=3)
bar_label = tk.Label(win, text="Bar").grid(row=1, column=4)
scatter_label = tk.Label(win, text="SCT").grid(row=1, column=5)

# scale1 = tk.Scale(win, from_=0, to=255)
# scale2 = tk.Scale(win, from_=0, to=255)
# scale3 = tk.Scale(win, from_=0, to=255)
# scale1.grid(row=2, column=3)
# scale2.grid(row=2, column=4)
# scale3.grid(row=2, column=5)


canvas = tk.Canvas(win2, width=2000, height=244)
canvas.grid(row=1, column=1)

img = ImageTk.PhotoImage(Image.open("3.jpg"))
canvas.create_image(20, 20, anchor='nw', image=img)


# button.pack(side=tk.LEFT)
# button2.pack(side=tk.RIGHT)

# label1.pack(side=tk.LEFT)
# label2.pack(side=tk.LEFT)
# label3.pack(side=tk.LEFT)

# label.pack()

# Activate the Windows
win.mainloop()
win2.mainloop()


