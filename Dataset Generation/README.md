# Overview

This folder contains the python scripts used to generate the original noisy variants of the NeuroMorse dataset. 

# DatasetGenerator.py
Initially, DatasetGenerator.py was used to create the initial python files (stored in .pckl format), which created the TrainDataset.pckl and TestDataset.pckl files which store the dataset as python objects. For the training dataset, each entry is presented as a tuple of a 'txp' array and its associated keyword. The Testset is presented as a tuple of a 'txp' array and a python dictionary. The array is the event-based data, whilst the dictionary contains all keywords as keys, with the values stored as the number of instance, start_times and end_times for the keywords.

# AddNoise.py
This script takes the stored .pckl files and creates noisy variants of the dataset, and then stores them in a python format.

# DatasetConversion.py

This script takes the python files and transforms them into the hdf5 format for broader usage.