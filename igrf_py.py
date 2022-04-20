import h5py

with h5py.File("igrfDB.h5", mode="r") as h5file:
    print (h5file.name)
    print (h5file.keys())
    print (h5file["data"])
    print (h5file["header"])

    for d in h5file["data"]:
        print (d)