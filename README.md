# IGRFupdate
### *Karla Vincent - AMENTUM internship*  
### &nbsp;
## <u> Purpose </u>
### The purpose of this code is to update the HDF5 database used to describe the International Geomagnetic Reference Field (IGRF). This is a set of spherical harmonic coefficients that can be input into a mathematical model to describe the Earth's magnetic field. In our case, we intend to use the IGRF data for the AE9/AP9/SPM: Radiation Belt and Space Plasma Specification Models. Developed by the Air Force Research Laboratory (AFRL), they model the fluxes of radiation belt and plasma particles in near-Earth space. Amentum Aerospace intends to use this model to alert satellite systems of upcoming radiation hazards to avoid system malfunction.
### Currently, the IGRF data used for the model system is outdated, using the IGRF-12 released in 2015. This describes a Definitive Geomagnetic Reference Field (DGRF) for years up to 2010, a provisional IGRF for 2015 and a predicative secular variation (SV) model for the interval 2015-2020. There is, however, an updated version of the IGRF, IGRF 13, which contains a DGRF for years up to 2015, an IRGF for 2020 and an SV model for the interval 2020-2025. To ensure that Amentum's use of the AE9/AP9/SPM system is as accurate as possible, the HDF5 file containing the coefficients of the IGRF12 must be updated to IGRF13.
### &nbsp;
## <u> Code Description </u>
### When beginning this IGRFupdate, a conda environment was created using
```bash
conda create -n IGRF python=3
```

### The code is divided into 3 main functions:
* Opening and viewing the HDF5 database
* Opening and viewing the txt files of the IGRF coefficients
* Editing the database
### <b> open_hdf5: </b>
### This function employs a with statement. This is a cleaner way of writing code where each line indented under the statement knows to call on the file stated
``` python
with h5py.File("igrfDB.h5", mode="r") as h5file:
```
### The function then prints:
* the root group
* the subgroups contained in the root group 
* the amount of members in these subgroups
* specific data within datasets of the subgroups

### This function was used to intially inspect the HDF5 data file. A HDF5 view program was also utilised. 
### &nbsp;
### <b> open_xcoeffs: </b>
### This function opens the txt file of the IGRF coefficients to inspect the columns and how the data is set up. Employs pandas.read.csv function e.g.
``` python
pd.read_csv("igrf12coeffs.txt", sep="\s+", skiprows= 3)
```
### sep = "\s+" defines the Delimiter to use and skiprows skips the first few rows of the txt file as they contain text describe the file and are unnecessary. 
### &nbsp;
### After comparing our HDF5 database and IGRF12 and 13 coefficients determined our file matches IGRF12. Therefore must update the database to include elements from the IGRF:
* update "2015" dataset to IGRF13 values
* change "2020" dataset to IGRf13 2020 and not 2015-2020 SV
* add dataset for IGRF12 2020-2025 SV
### &nbsp;
### <b> edit_hdf5: </b>
### This function completes the update to the HDF5 database.
### Firstly, employ shutil to copy the original file and create a HDF5update file. Then define:
* datasets to be editied
* group where new datasets will be added under
* arrays of data from coefficients txt file
### The datasets that are being updated must first be deleted. These include:
* "2015" 
* "2020"
* "fvYears" (a dataset containing each year of coefficients). New dataset adds 2025. 
* "iMaxYears" (a dataset only containing the max year). New max year is 2020.
### Then employing create_dataset and create_group create each required new dataset and group to compete updated file. These include groups and datasets for "iSize2025" and "iNmax2025" that are required for each year's coefficients. 
### &nbsp;
### <b> open_hdf5update: </b>
### Uses same format at open_hdf5 but is employed to check edit_hdf5 was successful. HDF5 view also useful to check update was successful. 































 

