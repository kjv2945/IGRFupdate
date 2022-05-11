from os import sep
import h5py
import numpy as np
import pandas as pd


# def open_hdf5 (): 
#     filename = "igrfDB.hf" #file name to use throughout


#     with h5py.File("igrfDB.h5", mode="r") as h5file: #use with so everything indented know to call to file
#         print (h5file.name) ## root group called /
#         print (h5file.keys()) ## views groups 
#         print (h5file["data"]) ## view amount of 'members' in each group
#         print (h5file["header"])
#         print (h5file.values())
#         print (h5file["data"]["dvGh2020"]["DATA"][:]) # prints all data in group 

# open_hdf5 () # to run function 

# def open_csv ():
#     import csv

#     with open("igrf12coeffs.txt") as csvfile: 
#         txtreader = csv.reader(csvfile, delimiter = " ")
#         rows = [x for x in txtreader]
#         # for row in rows:
#         #     print (",".join(row))
#         print (" ".join(rows[2:198]))


# # open_csv ()
# df = pd.read_table("igrf12coeffs.txt" , delimiter= " ")

# print (df)

# read text file into pandas DataFrame
df = pd.read_csv("igrf12coeffs.txt", sep=None, skiprows= 3)
pd.isna(df)
# display DataFrame
print(df)
# names = ["g/h", '1900.0', '1910.0 ', '1915.0',  '1920.0','1925.0','1930.0','1935.0','1940.0','1945.0','1950.0','1955.0','1960.0','1965.0','1970.0','1975.0','1980.0','1985.0','1990.0','1995.0', '2000.0','2005.0', '2010.0' ,'2015.0','2015-20']
# open_panda

