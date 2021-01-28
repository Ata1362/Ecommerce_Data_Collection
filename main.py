# This program should get the data from a excel files and extract the specific Data
# We can change which unique data we need from the E commerce Excel file.
# it is very important to have the all headers here.
import pandas as pd
import numpy as np
import glob as glb


def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def remove_repeated_data(data):

    new = np.unique(data, axis=1)

    return new


if __name__ == '__main__':
    print_hi('Welcome to the Ecommerce Data extractor')

# Creating the list of headers which we want them to be extract from the Excel
list_interest = ['Receiver Name', 'Phone Number', 'Area', 'State', 'Zip Code']
remover = True

info = []
for header in list_interest:
    sub_info = []

    # Here we are taking the file names in the directory including the address
    for item in glb.glob("G:\Google\Electronic Design\python_projects\Insight of Ecommerce Data/2020\*"):
        data = pd.read_excel(item,
                             sheet_name="orders",
                             header=None,
                             index_col=None)
        data_np = data.to_numpy()
        loc = np.argwhere(data_np == header)
        # if the loc is empty or [0, 0] then loc.any()"OR function" will return False
        if loc.any():
            loc2 = loc[0]
            # Y is the number of ROWs and X is the number of columns
            [y, x] = data_np.shape
            # Collect and add the relevant data from the excel file.
            sub_info.extend(data_np[1:y, loc2[1]])
        else:
            print(header)
            print(loc)
    # Forming the main data which has a few arrays equal to number of members in List_interest
    print('Date Collection of "{}" is finished'.format(header))
    info.append(sub_info)

if remover:
    info = remove_repeated_data(info)
    writer = pd.ExcelWriter('Extracted_Data_Duplicates_removed.xlsx', engine='xlsxwriter')
    print('DATA is unique now and size is "{}"'.format(info.shape))
else:
    writer = pd.ExcelWriter('Extracted_Data_Original.xlsx', engine='xlsxwriter')
    print('The Original DATA is "{}"'.format(np.shape(info)))

# Here we will combine two data and create a dictionary to be saved in Excel file
dic = dict(zip(list_interest, info))
# Change the Numpy format to Pandas format to save in Excel file
panda_dic = pd.DataFrame(dic)
# Data is the Excel's Sheet name to save the data in.
panda_dic.to_excel(writer, 'Data')
writer.save()

print(' Process is finished')
