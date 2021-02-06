import pandas as pd
import numpy as np
import glob as glb

def remove_repeated_data(data):
    new = np.unique(data, axis=1)
    return new

# We collect a list of all headers in each excel file

# A Better way to extract HEADER is after read the excel, use "data.head()" will read whole headers.

header = []
for item in glb.glob("G:\Google\Electronic Design\python_projects\Insight of Ecommerce Data/2020\*"):
    data = pd.read_excel(item,
                         sheet_name="orders",
                         header=None,
                         index_col=None)
    data_np = data.to_numpy()
    header.append(data_np[0, :])

# Now we just make sure that the extracted labels are mutual among all files...
# to avoid wrong attributes enter to our data

mutual_headers = np.intersect1d(header[0], header[1])
for i in range(len(header)):
    mutual_headers = np.intersect1d(mutual_headers, header[i])

# We will extract all info below the headers from all files and create a new file with all extracted data.

info = []
header = []
for header in mutual_headers:
    sub_info = []
    print('Extracting the data for "{}" header'.format(header))

    # Here we are taking the file names in the directory including the address
    for item in glb.glob("G:\Google\Electronic Design\python_projects\Insight of Ecommerce Data/2020\*"):

        data = pd.read_excel(item,
                             sheet_name="orders",
                             header=None,
                             index_col=None)
        data_np = data.to_numpy()
        loc = np.argwhere(data_np == header)
        #if the loc is empty or [0, 0] then loc.any()"OR function" will return False
        loc2 = loc[0]
        # Y is the number of ROWs and X is the number of columns
        [y, x] = data_np.shape
        # Collect and add the relevant data from the excel file.
        sub_info.extend(data_np[1:y, loc2[1]])
    # Forming the main data which has a few arrays equal to number of members in List_interest
    print('Date Collection of "{}" is finished'.format(header))
    info.append(sub_info)

remover = False
if remover:
    info = remove_repeated_data(info)
    writer = pd.ExcelWriter('Full_Extracted_Data_Duplicates_removed.xlsx', engine='xlsxwriter')
    print('Full DATA is unique now and size is "{}"'.format(info.shape[0]))
else:
    writer = pd.ExcelWriter('Full_Extracted_Data_Original.xlsx', engine='xlsxwriter')
    print('The Full Original DATA is "{}"'.format(np.shape(info)))

# Here we will combine two data and create a dictionary to be saved in Excel file
dic = dict(zip(mutual_headers, info))
# Change the Numpy format to Pandas format to save in Excel file
panda_dic = pd.DataFrame(dic)
# Data is the Excel's Sheet name to save the data in.
panda_dic.to_excel(writer, 'Data')
writer.save()

print(' Process is finished')
