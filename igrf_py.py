import array
from audioop import add
import h5py
import numpy as np
import pandas as pd
import shutil



def open_hdf5 (): #function to view data within file
    with h5py.File("igrfDB.h5", mode="r") as h5file: #use with so everything indented know to call to file
        # print (h5file.name) ## root group called /
        # print (h5file.keys()) ## views groups 
        # print (h5file["data"]) ## view amount of 'members' in each group
        # print (h5file["header"])
        # print (h5file.values())
        # print (h5file["data"]["dvGh2015"]["DATA"][:]) # prints all data in group 
        data2015 = h5file["data"]["dvGh2015"]["DATA"][:]
        data2020 = h5file["data"]["dvGh2020"]["DATA"]
        
        # print (data2015)

        
# open_hdf5 () # to run function 

# def edit_hdf5 ():
        
# # edit_hdf5 ()

def open_12coeffs ():
    df12 = pd.read_csv("igrf12coeffs.txt", sep="\s+", skiprows= 3)
    print(df12.columns)


def open_13coeffs ():
    df13 =  pd.read_csv("igrf13coeffs.txt", sep="\s+", skiprows= 3)
    d2015 = df13["2020-25"]
    print (df13.columns)
# open_13coeffs () #to print file contents

# def array_13coeffs():
    
#     # print(arr2020)
#     # print(arr2020.size) #to check arrays have worked

# array_13coeffs ()
def edit_hdf5 ():
    shutil.copy('igrfDB.h5',"igrfDBupdate.h5")
    with h5py.File("igrfDBupdate.h5", mode = "r+") as h5file:
        data2015edit = h5file["data"]["dvGh2015"]
        data2020edit = h5file["data"]["dvGh2020"]
        datafv = h5file["data"]["fvYears"]["DATA"]
        addgroup = h5file["data"]

        df13 =  pd.read_csv("igrf13coeffs.txt", sep="\s+", skiprows= 3)
        d2015 = df13["2015.0"]
        d2020 = df13["2020.0"]
        d2025 = df13["2020-25"]

        arr2015 = np.array(d2015)
        arr2020 = np.array(d2020)
        arr2025 = np.array(d2025)
        arrfv1 = np.array(datafv, dtype="f4")
        arrfv2 = np.append(arrfv1, float(2025.0))
        
        del data2015edit["DATA"]
        del data2020edit["DATA"]
        del addgroup["iMaxYear"]
        del addgroup["fvYears"]

        dset = data2015edit.create_dataset("DATA", data = arr2015) #format for creating new data
        dset2 = data2020edit.create_dataset("DATA", data = arr2020)

        grp = addgroup.create_group("dvGh2025")
        dset3 = grp.create_dataset("DATA", data=arr2025)

        grp2 = addgroup.create_group("iNmax2025")
        dset4 = grp2.create_dataset("DATA", data=int(13))

        grp3 = addgroup.create_group("iSize2025")
        dset5 = grp3.create_dataset("DATA", data = int(195))

        grp4 = addgroup.create_group("iMaxYear")
        dset6 = grp4.create_dataset("DATA", data = int(2020))

        grp5 = addgroup.create_group("fvYears")
        dset6 = grp5.create_dataset("DATA", data = arrfv2)

        
        # print(dset)
    
edit_hdf5()

def open_hdf5update () :
    with h5py.File("igrfDBupdate.h5", mode="r") as h5file: #use with so everything indented know to call to file
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
# open_hdf5update ()
