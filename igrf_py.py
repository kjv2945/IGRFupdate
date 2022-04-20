import h5py
import numpy as np
filename = "igrfDB.hf" #file name to use throughout

with h5py.File("igrfDB.h5", mode="r") as h5file: #use with so everything indented know to call to file
    print (h5file.name)
    print (h5file.keys())
    print (h5file["data"])
    print (h5file["header"])
    

    for d in h5file["data"]:
        print (d)