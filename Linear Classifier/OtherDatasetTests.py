import tonic
import matplotlib.pyplot as plt
import torch
import timeit
import dill as pickle
from STDPNetwork import Net
from STDPNetwork import GenerateSTDP

import seaborn as sns

#Run tests on DVS GEstures, SHD and other datasets.
#This script is reserved for the STDP network only, so it should follow a similar trend. Make sure STDP network has train and test functions.
#Datasets to definitely run: DVS Gestures, SHD, Spiking Speech Command (SSC), ASL DVS.
#Datasets to consider: Braille dataset, Google speech commands from NeuroBench.

# Dataset = 'DVS Gestures'
#Dataset = 'SSC'
#Dataset = 'SHD'
#Dataset = 'ASL DVS'

# Names = ['DVS','ASL','SSC','SHD']


def LoadDataset(data_name,train = True,n_time_bins = 200):
    match data_name:
        case 'DVS':
            dataset = tonic.datasets.DVSGesture(save_to='../data',train=train)

            frame_transform = tonic.transforms.Compose([
                tonic.transforms.ToFrame(sensor_size=dataset.sensor_size,n_time_bins=n_time_bins),
                torch.from_numpy,
                

            ])

            dataset = tonic.datasets.DVSGesture(save_to= '../data',transform = frame_transform,train = train)

        case 'ASL':
            dataset = tonic.datasets.ASLDVS(save_to='../data')

            frame_transform = tonic.transforms.Compose([
                tonic.transforms.ToFrame(sensor_size=dataset.sensor_size, n_time_bins = n_time_bins),
                torch.from_numpy,

            ])
            dataset = tonic.datasets.ASLDVS(save_to='../data',transform=frame_transform)
        case 'SHD':
            dataset = tonic.datasets.SHD(save_to='../data', train=train)

            #Below code is the transformation that we want. This gives us spikes where each 0th dimension represents a timestep and the remaining dimensions
            #represent the rest of the spiking data. It will also convert to tensor for us to then implement in spiketorch.
            frame_transform = tonic.transforms.Compose([
                tonic.transforms.ToFrame(sensor_size=dataset.sensor_size, n_time_bins = n_time_bins),
                torch.from_numpy])

            dataset = tonic.datasets.SHD(save_to='../data',transform = frame_transform, train=train)
        
        case 'SSC':
            if train == True:
                split = 'train'
            else:
                split = 'test'
            dataset = tonic.datasets.SSC(save_to='../data',split = split)

            frame_transform = tonic.transforms.Compose([
                tonic.transforms.ToFrame(sensor_size = dataset.sensor_size, n_time_bins = 200),
                torch.from_numpy
            ])
            dataset = tonic.datasets.SSC(save_to='../data',transform= frame_transform, split = split)

    return dataset

def Train(network,TrainData,epochs = 50,n_time_bins = 200):
    #This is general code for any network on any dataset.
    start_time = timeit.default_timer()
    for epo in range(epochs):
        #Generate the spikes to present to the network.
        #TODO may need some code to help format the inputs for other datasets. This may still work though.



        #Convert each training input into spikes, and append into a list
        a = torch.randperm(TrainData.__len__()) #For random order
        
        
        for idx in a:
            SpikeData = TrainData[idx][0].to(torch.float)
            input_times = torch.zeros(network.num_inputs) #Determines the most recent input.
            
            network.mem1.zero_()


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
        print('time elapsed:%f' %(timeit.default_timer() - start_time))

    network.PlotWeight('Final Weight.png')
    return network

def AssignNeurons(network,TrainData,n_time_bins = 200):
    #Give each of the output neurons a label based on max spike count
    Recorder = torch.zeros((network.num_class,network.num_class))
    i = 0
    network.mem1.zero_()
    for SpikeData, label in TrainData:
        SpikeData = SpikeData.to(torch.float)
        for t in range(n_time_bins):
            spk1, mem1 = network.step(SpikeData[t].flatten())
            Recorder[label,:] += spk1.squeeze() #y axis is actual label, x axis is predicted label


    #Using maximum spike count as a verification tool
    vals, idx_classification = torch.max(Recorder,dim=0) #idx_classification is numerical value of label.
    return idx_classification, Recorder

def Test(network,TestData,n_time_bins = 200):
    conf_matrix = torch.zeros((network.num_class,network.num_class))
    for SpikeData, label in TestData:
        SpikeData = SpikeData.to(torch.float)
        output = torch.zeros(network.num_class) #Record output for classification
        network.mem1.zero_()
        for t in range(n_time_bins):
            spk1, mem1 = network.step(SpikeData[t].flatten())
            output += spk1.squeeze()
        #Determine maximum spike count and corresponding class and update conf matrix
        idx = torch.argmax(output)
        conf_matrix[label,network.idx_classification[idx].item()] += 1
    return conf_matrix
        


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

    return TestNet, TrainData, n_time_bins
    
def TrainSSC():
    #Train STDP network for SSC dataset. Modify below network, STDP and homeostatic parameters as needed.

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
    #View initial weights
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
    return TestNet, TrainData, n_time_bins

def TrainSHD():
    #Train STDP network for SHD dataset.

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

    return TestNet, TrainData, n_time_bins
###########################################
if __name__ == '__main__':
    dataname = 'DVS' #Options include 'DVS','SHD','SSC'
    match dataname:
        case 'DVS':
            network, TrainData, n_time_bins = TrainDVS() #Options are TrainDVS(), TrainSHD() and TrainSSC()
        case 'SHD':
            network, TrainData, n_time_bins = TrainSHD()
        case 'SSC':
            network, TrainData, n_time_bins = TrainSSC()

    idx_classification, Recorder = AssignNeurons(network,TrainData,n_time_bins = n_time_bins)
    network.idx_classification = idx_classification.to(torch.int)

    #Plot Recorder to see spiking patterns during assignment
    plt.figure()
    img = sns.heatmap(Recorder,annot=True, cmap = 'hot_r',cbar_kws= {"label":"Scale"})
    plt.xlabel('Predicted Label')
    plt.ylabel('Actual Label')
    plt.savefig(dataname +'Recorder.png')
    plt.close()

    TestData = LoadDataset(data_name=dataname,train = False,n_time_bins=200)

    conf_matrix = Test(network,TestData,n_time_bins = n_time_bins)

    f = open(dataname +'ConfusionMatrix.pckl','wb')
    pickle.dump(conf_matrix,f)
    f.close()


    plt.figure()
    img = sns.heatmap(conf_matrix,annot=True, cmap = 'hot_r',cbar_kws= {"label":"Scale"})
    plt.xlabel('Predicted Label')
    plt.ylabel('Actual Label')
    plt.savefig(dataname + 'Confusion Matrix.png')
    plt.close()

    correct = torch.sum(torch.diagonal(conf_matrix))

    error = correct/torch.sum(conf_matrix)
    print('error:%f'%(error))








        

