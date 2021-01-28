from tkinter import *
import pandas as pd
import numpy as np



win = Tk()
win.geometry("250x250")
def process():

    print("Pi Chart: %d,\nBar Chart: %d" % (var1.get(), var2.get()))

    if var1.get():
        print("we can proceed to show the Pi chart")
        list_interest = ['Receiver Name', 'Phone Number', 'Area', 'State', 'Zip Code']






        series = pd.Series(data, index=list_interest, name="series")
        #, figsize=(6,6)
        series.plot.pie(labels=list_interest, colors=["r", "g", "b", "c", "y"], autopct="%.2f", fontsize=20)

    if var2.get():
        print("we can proceed with Bar chart")

    if not var2.get() and not var1.get():
        print("no data is chosen")





def stop():
    print("Thank you for using this APP")
    win.destroy()
    win.quit()


def extract():
    # Get the file link to load the prepared excel file.
    list_interest = ['Receiver Name', 'Phone Number', 'Area', 'State', 'Zip Code']

    file_loc = 'G:\Google\Electronic Design\python_projects\Insight of Ecommerce Data/Updating_Extracted_Data_Duplicates_removed.xls'
    global info, data

    info = []
    data = pd.read_excel(file_loc,
                         sheet_name="Data",
                         header=None,
                         index_col=None)
    # To change the Panda format to Numpy for easy using the Data
    data_np = data.to_numpy()
    # Search and locate the headers we want.
    for header in list_interest:
        loc = np.argwhere(data_np == header)
        loc2 = loc[0]
        # Y is the number of ROWs and X is the number of columns
        [y, x] = data_np.shape
        # Collect and add the relevant data from the excel file.
        info.append(data_np[1:y, loc2[1]])
        # Forming the main data which has a few arrays equal to number of members in List_interest
        print('Date Collection of "{}" is finished'.format(header))




Label(win, text="Past the file .xls location").grid(row=0, sticky=W)
address = Entry(win)
Label(win, text="Your Chart:").grid(row=2, sticky=W)
var1 = IntVar()
Checkbutton(win, text="Pi Chart", variable=var1).grid(row=3, sticky=W)
var2 = IntVar()
Checkbutton(win, text="Bar Chart", variable=var2).grid(row=4, sticky=W)
Button(win, text=' Quit ', command=stop, bg='red', fg='white').grid(row=7, column=0, sticky=W, pady=4)
Button(win, text='Process', command=process, bg='green', fg='white').grid(row=6, column=1, sticky=W, pady=4)
Button(win, text='Extract', command=extract, bg='yellow', fg='blue').grid(row=6, column=0, sticky=W, pady=4)

mainloop()
