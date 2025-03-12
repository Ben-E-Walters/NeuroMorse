import tonic
import torch
from LinClass import Net
#from STDPNetwork import Train, test etc. Make sure functions are the same.

#Run tests on DVS GEstures, SHD and other datasets.
#This script is reserved for the STDP network only, so it should follow a similar trend. Make sure STDP network has train and test functions.
#Datasets to definitely run: DVS Gestures, SHD, Spiking Speech Command (SSC), ASL DVS.
#Datasets to consider: Braille dataset, Google speech commands from NeuroBench.

# Dataset = 'DVS Gestures'
#Dataset = 'SSC'
#Dataset = 'SHD'
#Dataset = 'ASL DVS'

# Names = ['DVS','ASL','SSC','SHD']



#Have to redefine training and testing due to differences in NeuroMorse dataset.

def LoadDataset(data_name,train = True):
    match data_name:
        case 'DVS':
            dataset = tonic.datasets.DVSGesture(save_to='./data',train=train)

            frame_transform = tonic.transforms.Compose([
                tonic.transforms.ToFrame(sensor_size=dataset.sensor_size,n_time_bins=100),
                torch.from_numpy,
                torch.flatten

            ])

            dataset = tonic.datasets.DVSGesture(save_to= './data',transform = frame_transform,train = train)
        
        

