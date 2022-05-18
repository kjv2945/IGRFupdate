import array
import h5py
import numpy as np
import pandas as pd



def open_hdf5 (): #function to view data within file
    with h5py.File("igrfDB.h5", mode="r") as h5file: #use with so everything indented know to call to file
        # print (h5file.name) ## root group called /
        # print (h5file.keys()) ## views groups 
        # print (h5file["data"]) ## view amount of 'members' in each group
        # print (h5file["header"])
        # print (h5file.values())
        # print (h5file["data"]["dvGh2015"]["DATA"][:]) # prints all data in group 
        data2015 = h5file["data"]["dvGh2015"]["DATA"][:]
        data2020 = h5file["data"]["dvGh2020"]["DATA"][:]
        print (data2015)
        print (data2020)
open_hdf5 () # to run function 

# def edit_hdf5 ():
        
# # edit_hdf5 ()

def open_12coeffs ():
    df12 = pd.read_csv("igrf12coeffs.txt", sep="\s+", skiprows= 3)
    print(df12.columns)


def open_13coeffs ():
    df13 =  pd.read_csv("igrf13coeffs.txt", sep="\s+", skiprows= 3)
    d2015 = df13["2015.0"]
    print (d2015)
# open_13coeffs () #to print file contents

# def array_13coeffs():
    
#     # print(arr2020)
#     # print(arr2020.size) #to check arrays have worked

# array_13coeffs ()
def edit_hdf5 ():
    with h5py.File("igrfDB.h5", mode = "r+") as h5file:
        data2015edit = h5file["data"]["dvGh2015"]
        data2020edit = h5file["data"]["dvGh2020"]
        df13 =  pd.read_csv("igrf13coeffs.txt", sep="\s+", skiprows= 3)
        d2015 = df13["2015.0"]
        d2020 = df13["2020.0"]
        arr2015 = np.array(d2015)
        arr2020 = np.array(d2020)
        # for d in data2015edit:
        del data2015edit["DATA"]
        del data2020edit["DATA"]
        dset = data2015edit.create_dataset("DATA", data = arr2015) #format for creating new data
        dset2 = data2020edit.create_dataset("DATA", data = arr2020)
        print(dset)
    
# edit_hdf5()
