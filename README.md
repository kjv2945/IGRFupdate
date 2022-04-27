# IGRFupdate
### *Karla Vincent - AMENTUM internship*  
### &nbsp;

## IGRF coding notes

### 20/4 
#### Open HDF5 with windows termial
```bash
conda create -n IGRF python=3
```
#### with statment 
``` python
with h5py.File("igrfDB.h5", mode="r") as h5file:
```
##### This is a cleaner way of writing code where each line indented under the statement knows to call on the file stated
### **Future Notes**
 * Must launch file through anaconda prompt so ananconda environment can be accessed 
 * Attempted to import h5pyViewer but error showed. After research online found that it is incompatible with python 3
### &nbsp;
### 27/4
* attempted to create conda environment in python 2 to open h5pyviewer. Was unsuccessful
* Downloaded HDF View program which allowed the inspection of each part of file but no representation but found that values for each data column named "DATA" and can view through code by:
``` python
print (h5file["data"]["dvGh2020"]["DATA"][:]) #for example
```

#### After producing the above data and comparing to IGRF12 coefficients found it was the data for SV 2015-2020
* This is the predictive linear secular variation for 2015-2020
#### After cross checking multiple columns the file is identical to IGRF12 coefficients
#### Cross checking with IGRF13 up until 2010 is identical to our file. 2015 is slightly different. 
### Therefore we are missing:
* 2020 IGRF from IGRF13
* SV 2020-2025 from IGRF13

 

