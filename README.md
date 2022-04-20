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

