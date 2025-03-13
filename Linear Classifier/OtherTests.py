import tonic
import matplotlib.pyplot as plt
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
                tonic.transforms.ToFrame(sensor_size=dataset.sensor_size,n_time_bins=200),
                torch.from_numpy,
                

            ])

            dataset = tonic.datasets.DVSGesture(save_to= './data',transform = frame_transform,train = train)

        case 'ASL':
            dataset = tonic.datasets.ASLDVS(save_to='./data')

            frame_transform = tonic.transforms.Compose([
                tonic.transforms.ToFrame(sensor_size=dataset.sensor_size, n_time_bins = 200),
                torch.from_numpy,

            ])
            dataset = tonic.datasets.ASLDVS(save_to='./data',transform=frame_transform)
        case 'SHD':
            dataset = tonic.datasets.SHD(save_to='./data', train=train)

            #Below code is the transformation that we want. This gives us spikes where each 0th dimension represents a timestep and the remaining dimensions
            #represent the rest of the spiking data. It will also convert to tensor for us to then implement in spiketorch.
            frame_transform = tonic.transforms.Compose([
                tonic.transforms.ToFrame(sensor_size=dataset.sensor_size, n_time_bins = 200),
                torch.from_numpy])

            dataset = tonic.datasets.SHD(save_to='./data',transform = frame_transform, train=train)
        
        case 'SSC':
            if train == True:
                split = 'train'
            else:
                split = 'test'
            dataset = tonic.datasets.SSC(save_to='./data',split = split)

            frame_transform = tonic.transforms.Compose([
                tonic.transforms.ToFrame(sensor_size = dataset.sensor_size, n_time_bins = 200),
                torch.from_numpy
            ])
            dataset = tonic.datasets.SSC(save_to='./data',transform= frame_transform, split = split)

    return dataset





# Name = 'SSC' #options include DVS, SSC, SHD and ASL

# TrainData = LoadDataset(Name,train = True)
# for i in range(15):
#     # fig, axs = plt.subplots(2)
#     # axs[0].imshow(TrainData[0][0][i,0,:,:])
#     # axs[1].imshow(TrainData[0][0][i,1,:,:])
#     # fig.savefig('Events plot%i.png' %(i))
#     plt.figure()
#     plt.imshow(TrainData[i][0][:,0,:])
#     plt.savefig('SSC%i.png' %(i))
#     plt.close()
# print(Name)



# #Network parameters
# num_channels = 2
# num_classes = 50
# num_class = 50 #Number of classification neurons

# TestNet = Net(num_channels,num_class)
# #Lower initial threshold for spiking activity
# init_wt = torch.rand_like(TestNet.fc1.weight.detach())
# initthresh = torch.ones_like(TestNet.lif1.threshold.detach())
# with torch.no_grad():
#     TestNet.fc1.weight.copy_(init_wt)
#     TestNet.lif1.threshold.copy_(initthresh)


# #STDP parameters:
# Ap = 1
# NegLength = 15
# PosLength = 15
# TestNet.STDP = GenerateSTDP(PosLength,NegLength,Ap)
# TestNet.PosLength = 15
# TestNet.NegLength = 15

# #Training epochs
# epochs = 50



# TestNet.PlotWeight('Initial Weights.png')

# #Homeostatic regulation parameters
# TestNet.Ath = 1e-1
# TestNet.Tau_th = TestNet.Ath/num_class/20 #20 is chosen arbitrarily, should represent average number of timesteps for each input.
# TestNet.eta = 0.1

        

