# NeuroMorse
Repository for the code generation of the NeuroMorse Dataset, available at 10.5281/zenodo.12702379. Note: due to the large file sizes, the final generated dataset is only available at zenodo.

# Data Storage Scheme
The Data is stored in hdf5 format. For both the training and testing sets, there are 27 seperate files. The 'Clean' files are the original datasets with no noise added. The remaining files contain various types and degrees of noise, as specified by their label. The directory tree for each file is as follows:




# Linear Classifier
This file contains both the linear classifier tests performed on both the training and testing sets.

# Dataset Generation
This folder contains the files used to generate both the clean and noisy versions of the datasets, whilst the DatasetConversion.py file converts from the pckl format to hdf5.
