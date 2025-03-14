import tonic
import matplotlib.pyplot as plt
import torch
import timeit
import dill as pickle
from LinClass import Net
from STDPNetwork import GenerateSTDP

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

def LoadDataset(data_name,train = True,n_time_bins = 200):
    match data_name:
        case 'DVS':
            dataset = tonic.datasets.DVSGesture(save_to='./data',train=train)

            frame_transform = tonic.transforms.Compose([
                tonic.transforms.ToFrame(sensor_size=dataset.sensor_size,n_time_bins=n_time_bins),
                torch.from_numpy,
                

            ])

            dataset = tonic.datasets.DVSGesture(save_to= './data',transform = frame_transform,train = train)

        case 'ASL':
            dataset = tonic.datasets.ASLDVS(save_to='./data')

            frame_transform = tonic.transforms.Compose([
                tonic.transforms.ToFrame(sensor_size=dataset.sensor_size, n_time_bins = n_time_bins),
                torch.from_numpy,

            ])
            dataset = tonic.datasets.ASLDVS(save_to='./data',transform=frame_transform)
        case 'SHD':
            dataset = tonic.datasets.SHD(save_to='./data', train=train)

            #Below code is the transformation that we want. This gives us spikes where each 0th dimension represents a timestep and the remaining dimensions
            #represent the rest of the spiking data. It will also convert to tensor for us to then implement in spiketorch.
            frame_transform = tonic.transforms.Compose([
                tonic.transforms.ToFrame(sensor_size=dataset.sensor_size, n_time_bins = n_time_bins),
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

def Train(network,TrainData,epochs = 50,n_time_bins = 200):
    #This is general code for any network on any dataset.

    for epo in range(epochs):
        #Generate the spikes to present to the network.
        #TODO may need some code to help format the inputs for other datasets. This may still work though.



        #Convert each training input into spikes, and append into a list
        a = torch.randperm(TrainData.__len__()) #For random order
        start_time = timeit.default_timer()
        count = 0
        for idx in a:

            if count %50 ==0:
                print('time elapsed: %f' %(timeit.default_timer()-start_time))
                plt.figure()
                plt.imshow(network.fc1.weight.detach()[:,0:700])
                plt.savefig('Weight %i.png' %(count))
                plt.close()

            SpikeData = TrainData[idx][0].to(torch.float)


            input_times = torch.zeros(network.num_inputs) #Determines the most recent input.
            
            network.mem1.zero_()

            count +=1

            for t in range(n_time_bins):
                spk1, mem1 = network.step(SpikeData[t].flatten())
                input_times[SpikeData[t].flatten()>0] = t

                #Update threshold activity
                with torch.no_grad():
                    NewThresh = network.lif1.threshold.detach() - network.Tau_th + network.Ath*spk1.squeeze()
                    network.lif1.threshold.copy_(NewThresh)

                if torch.sum(spk1)>0:
                    delta_t = t - input_times
                    network.W1_Update(delta_t,spk1)
                    network.mem1.zero_()

    network.PlotWeight('Final Weight.png')
    return network


def TrainDVS():
    #Train STDP network for DVS dataset.

    n_time_bins = 200
    #Load dataset
    TrainData = LoadDataset(data_name='DVS',train = True,n_time_bins=200)
    # #Network parameters
    num_inputs = 128*128*2 #Equivalent to number of input channels for the dataset.
    num_classes = 11 #Number of classes but also number of output neurons


    

    TestNet = Net(num_inputs,num_classes)
    #Lower initial threshold for spiking activity
    init_wt = torch.rand_like(TestNet.fc1.weight.detach())
    initthresh = torch.ones_like(TestNet.lif1.threshold.detach())
    with torch.no_grad():
        TestNet.fc1.weight.copy_(init_wt)
        TestNet.lif1.threshold.copy_(initthresh)


    #STDP parameters:
    Ap = 1
    NegLength = 15
    PosLength = 15
    TestNet.STDP = GenerateSTDP(PosLength,NegLength,Ap)
    TestNet.PosLength = 15
    TestNet.NegLength = 15

    #Training epochs
    epochs = 50 #May be too much. must justify smaller value with potentially validation accuracy or something.



    TestNet.PlotWeight('Initial Weights.png')

    

    #Homeostatic regulation parameters
    TestNet.Ath = 1e-1
    TestNet.Tau_th = TestNet.Ath/num_classes/n_time_bins 
    TestNet.eta = 0.1

    #Now Train the network and then test the network.
    TestNet = Train(TestNet,TrainData,epochs = epochs,n_time_bins=n_time_bins)

    f = open('DVSTrainedNetwork.pckl','wb')
    pickle.dump(TestNet,f)
    f.close()

    # return TestNet
    
def TrainSSC():
    #Train STDP network for DVS dataset.

    n_time_bins = 200
    #Load dataset
    TrainData = LoadDataset(data_name='SSC',train = True,n_time_bins=200)
    # #Network parameters
    num_inputs = 700 #Equivalent to number of input channels for the dataset.
    num_classes = 35 #Number of classes but also number of output neurons
   
    

    TestNet = Net(num_inputs,num_classes)
    #Lower initial threshold for spiking activity
    init_wt = torch.rand_like(TestNet.fc1.weight.detach())
    initthresh = torch.ones_like(TestNet.lif1.threshold.detach())
    with torch.no_grad():
        TestNet.fc1.weight.copy_(init_wt)
        TestNet.lif1.threshold.copy_(initthresh)


    #STDP parameters:
    Ap = 1
    NegLength = 15
    PosLength = 15
    TestNet.STDP = GenerateSTDP(PosLength,NegLength,Ap)
    TestNet.PosLength = 15
    TestNet.NegLength = 15

    #Training epochs
    epochs = 50 #May be too much. must justify smaller value with potentially validation accuracy or something.



    TestNet.PlotWeight('Initial Weights.png')

    

    #Homeostatic regulation parameters
    TestNet.Ath = 1e-1
    TestNet.Tau_th = TestNet.Ath/num_classes/n_time_bins 
    TestNet.eta = 0.1

    #Now Train the network and then test the network.
    TestNet = Train(TestNet,TrainData,epochs = epochs,n_time_bins=n_time_bins)

    f = open('SSCTrainedNetwork.pckl','wb')
    pickle.dump(TestNet,f)
    f.close()

def TrainSHD():
    #Train STDP network for DVS dataset.

    n_time_bins = 200
    #Load dataset
    TrainData = LoadDataset(data_name='SHD',train = True,n_time_bins=200)
    # #Network parameters
    num_inputs = 700 #Equivalent to number of input channels for the dataset.
    num_classes = 20 #Number of classes but also number of output neurons
   
    

    TestNet = Net(num_inputs,num_classes)
    #Lower initial threshold for spiking activity
    init_wt = torch.rand_like(TestNet.fc1.weight.detach())
    initthresh = torch.ones_like(TestNet.lif1.threshold.detach())
    with torch.no_grad():
        TestNet.fc1.weight.copy_(init_wt)
        TestNet.lif1.threshold.copy_(initthresh)


    #STDP parameters:
    Ap = 1
    NegLength = 15
    PosLength = 15
    TestNet.STDP = GenerateSTDP(PosLength,NegLength,Ap)
    TestNet.PosLength = 15
    TestNet.NegLength = 15

    #Training epochs
    epochs = 50 #May be too much. must justify smaller value with potentially validation accuracy or something.



    TestNet.PlotWeight('Initial Weights.png')

    

    #Homeostatic regulation parameters
    TestNet.Ath = 1e-1
    TestNet.Tau_th = TestNet.Ath/num_classes/n_time_bins 
    TestNet.eta = 0.1

    #Now Train the network and then test the network.
    TestNet = Train(TestNet,TrainData,epochs = epochs,n_time_bins=n_time_bins)

    f = open('SHDTrainedNetwork.pckl','wb')
    pickle.dump(TestNet,f)
    f.close()





Name = 'SSC' #options include DVS, SSC, SHD and ASL

TrainData = LoadDataset(Name,train = True)
DVSNet = TrainSSC()
# print(TrainData.classes)
# # for i in range(15):
# #     fig, axs = plt.subplots(2)
# #     axs[0].imshow(TrainData[0][0][i,0,:,:])
# #     axs[1].imshow(TrainData[0][0][i,1,:,:])
# #     fig.savefig('Events plot%i.png' %(i))
# #     # plt.figure()
# #     # plt.imshow(TrainData[i][0][:,0,:])
# #     # plt.savefig('SSC%i.png' %(i))
# #     # plt.close()
# print(Name)





        

