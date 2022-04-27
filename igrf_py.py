import h5py
import numpy as np
filename = "igrfDB.hf" #file name to use throughout

with h5py.File("igrfDB.h5", mode="r") as h5file: #use with so everything indented know to call to file
    print (h5file.name) ## root group called /
    print (h5file.keys()) ## views groups 
    print (h5file["data"]) ## view amount of 'members' in each group
    print (h5file["header"])
    print (h5file.values())
    print (h5file["data"]["dvGh2020"]["DATA"][:]) # prints all data in group 



