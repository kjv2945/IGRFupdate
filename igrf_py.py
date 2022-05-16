import h5py
import numpy as np
import pandas as pd


def open_hdf5 (): 
    with h5py.File("igrfDB.h5", mode="r") as h5file: #use with so everything indented know to call to file
        # print (h5file.name) ## root group called /
        # print (h5file.keys()) ## views groups 
        # print (h5file["data"]) ## view amount of 'members' in each group
        # print (h5file["header"])
        # print (h5file.values())
        # print (h5file["data"]["dvGh2015"]["DATA"][:]) # prints all data in group 
        newdset = f.create_dataset("IGRF2020", (195), dtype = int) 
        data = h5file["data"]["dvGh2015"]["DATA"]
        print (data)
# open_hdf5 () # to run function 

def edit_hdf5 ():
    with h5py.File("igrfDB.h5", mode="r") as h5file:
        arr = np.arange(100) # array
        for d in h5file:
            dset = h5file.create_dataset("data/", data = arr) #format for creating new data
edit_hdf5 ()

def open_12coeffs ():
    df12 = pd.read_csv("igrf12coeffs.txt", sep="\s+", skiprows= 3)
    print(df.columns)


def open_13coeffs ():
    df13 =  pd.read_csv("igrf13coeffs.txt", sep="\s+", skiprows= 3)
    d2015 = df13["2015.0"]
    print (d2015)
# open_13coeffs () #to print file contents

def array_13coeffs():
    df13 =  pd.read_csv("igrf13coeffs.txt", sep="\s+", skiprows= 3)
    d2015 = df13["2015.0"]
    d2020 = df13["2020.0"]
    arr2015 = np.array([d2015])
    arr2020 = np.array([d2020])
    # print(arr2020)
    # print(arr2020.size) #to check arrays have worked

array_13coeffs ()

