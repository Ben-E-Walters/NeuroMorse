import torch
import pickle
import random
import timeit
import matplotlib.pyplot as plt
import seaborn as sns
from LinClass import Net
import numpy as np


# def Train(network,train_data):
    #Train data with necessary info

# def Test(network, test_Data):
#TODO: Place network class here as well from LinClass.

def GenerateSTDP(PosLength,NegLength,Ap):
    # Generate STDP window
    
    DelT = np.linspace(-NegLength,PosLength,NegLength+PosLength+1)
    WUpdate = np.zeros(PosLength+NegLength+1)
    
    WUpdate[(NegLength):(PosLength + NegLength + 1)] = Ap*np.linspace(1,0,PosLength+1)

    Window = np.zeros((2,PosLength + NegLength+1))
    Window[0,:] = DelT
    Window[1,:] = WUpdate
    return Window
    #Note: using causal, weight dependant STDP rule from: "An Optimized Deep Spiking Neural Network Architecture Without Gradients"

def GenerateTrainSpikes(Dataset,num_classes = 50, shuffle = True, word_space = 15,num_channels = 2):
    #Use this to generate the data.
    #Also, should look at test set as well. This code should definitely be updated with some sort of transform and with batching.
    #TODO: Introduce a way to batch the data into smaller samples. Not really necessary for training, as training is small.
    SpikeData = []
    #Should randomise order for training set.
    for i in range(num_classes):
        data, label = Dataset[i]
        data_neuro = torch.zeros((int(data[-1][0])+1+word_space,num_channels))
    for idx in data: 
        data_neuro[int(idx[0]),int(idx[1])] = 1
    SpikeData.append(data_neuro)
    if shuffle == True:
        random.shuffle(SpikeData)
    return torch.cat(SpikeData,0) #consider removing torch.cat

def GenerateTestSpikes(TestSet, num_channels = 2):
    #Use this to generate the spikes for the test set.
    #compile spike sequence for test dataset
    #Below requires some form of batching or transform to handle more efficiently.
    #Consider if this is even necessary, wouldn't it be possible just to compare with the input each time and save memory?
    TestNeuro = torch.zeros((int(TestSet[0][-1][0])+1,num_channels))
    start_time = timeit.default_timer()
    counter = 0
    for idx in TestSet[0]:
        TestNeuro[int(idx[0]),int(idx[1])] = 1
        counter +=1
        if counter % 10000000 == 0:
            print('Time elapsed: %d, Counter = %d' %(timeit.default_timer() - start_time,counter))
    return TestNeuro

def Train(network,dataset,epochs):
    #Train network
    for epo in range(epochs):
        TrainSpikes = GenerateTrainSpikes(dataset,50)
        TrainSpikes = TrainSpikes.to(torch.float)

        #Convert each training input into spikes, and append into a list
        a = torch.randperm(network.num_class) #For random order

        input_times = torch.zeros(network.num_inputs) #Determines the most recent input.
        
        network.mem1.zero_()

        for t in range(TrainSpikes.shape[0]):
            spk1, mem1 = network.step(TrainSpikes[t,:])
            input_times[TrainSpikes[t,:]>0] = t

            #Update threshold activity
            with torch.no_grad():
                NewThresh = network.lif1.threshold.detach() - network.Tau_th + network.Ath*spk1.squeeze()
                network.lif1.threshold.copy_(NewThresh)

            if torch.sum(spk1)>0:
                delta_t = t - input_times
                network.W1_Update(delta_t,spk1,network.PosLength)
                network.mem1.zero_()

    network.PlotWeight('Final Weight.png')
    return network

def Assign_Hidden_Layer(network,dataset, word_space = 15):
    #Determine which neuron is assigned to which keyword in the training set.
    #Assignment run
    #One additional run with no STDP or homeostatic regulation for class assignment.
    SpikeData = []


    for i in range(network.num_class):
        data, label = dataset[i]
        data_neuro = torch.zeros((int(data[-1][0])+1+word_space,network.num_inputs))
        for idx in data: 
            data_neuro[int(idx[0]),int(idx[1])] = 1
        SpikeData.append(data_neuro)

    Recorder = torch.zeros((network.num_class,network.num_class))
    i = 0
    for data in SpikeData:
        for t in range(data.shape[0]):
            spk1, mem1 = network.step(data[t,:])
            Recorder[i,:] += spk1.squeeze()
        i +=1

    #Using maximum spike count as a verification tool
    vals, idx_classification = torch.max(Recorder,dim=0) #idx_classification is numerical value of label.
    return idx_classification

def Test(network,dataset,idx_classification):
    #Test the network
    TestDict = dataset[1]
    TestingEndList = [] #List of list for all end times for each keyword

    for key in TestDict.keys():
        TestingEndList.append(TestDict[key][2])
    
    correct_spikes = 0
    incorrect_spikes = 0

    start_time = timeit.default_timer()

    #Not technically a confusion matrix, just a measure of correct vs incorrect for each class
    conf_matrix = torch.zeros((50,2))

    TestSpikes = GenerateTestSpikes(dataset)
    # TestSpikes = torch.ones((10000,2))
    # TestSpikes[200:300,0] = 1

    
    input_times = torch.zeros(network.num_inputs)
    for t in range(TestSpikes.shape[0]):
            spk1, mem1 = network.step(TestSpikes[t,:])
            input_times[TestSpikes[t,:]>0] = t

            if t%1000000 ==0 & t>0:
                print('Time Elapsed: %d, t = %d, correct = %i, incorrect = %i' %(timeit.default_timer()-start_time,t,correct_spikes,incorrect_spikes))

            if torch.sum(spk1)>0:
                spk1_label = idx_classification[spk1.nonzero()][0,1].item()
                if t in TestingEndList[spk1_label]:
                    correct_spikes +=1
                    conf_matrix[spk1_label,0] +=1
                else:
                    incorrect_spikes +=1
                    conf_matrix[spk1_label,1] +=1
                    
    print('Correct Spikes')
    print(correct_spikes)
    print('Incorrect Spikes')
    print(incorrect_spikes)
    print('Confusion Matrix')
    print(conf_matrix)

    plt.figure(figsize = (15,10))
    img = sns.heatmap(
            conf_matrix,annot= True, cmap = "YlGnBu",cbar_kws= {"label":"Scale"}
        )
    plt.xlabel("Predicted Label")
    plt.ylabel("Actual Label")
    plt.savefig('Confusion Matrix.svg') #1st row is correct spikes, 2nd row is incorrect spikes
    plt.close()

# def run(network,dataset)
    #Consider using above code for further convenience.





# ##### Test Set Verification #####
# f = open('Top50Dataset.pckl','rb')
# TrainSet = pickle.load(f)
# f.close()

# #Should we train with our noisy datasets? That might be something we should investigate. Also, I do wonder why we're adding fixed levels of noise for one particular seed,
# #surely it's more rigorous to provide code that adds noise independantly. Something to consider.
# #TODO: add code that allows dataset to be loaded with appropriate level of noise. Use defined parameters for each level of noise.

# f = open('Top50Testset.pckl','rb')
# TestSet = pickle.load(f)
# f.close()
# #For now, use pckl files for convenience. Think about using h5 files or other code for easy loading.

# #timesteps between words:
# word_space = 15


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


# epochs = 50



# TestNet.PlotWeight('Initial Weights.png')

# #Homeostatic regulation parameters
# TestNet.Ath = 1e-1
# TestNet.Tau_th = TestNet.Ath/num_class/20 #20 is chosen arbitrarily, should represent average number of timesteps for each input.
# TestNet.eta = 0.1

# TestNet = Train(TestNet,TrainSet)

# #Save the network

# idx_classification = Assign_Hidden_Layer(TestNet,TrainSet)

# f = open('Network,Idx.pckl','wb')
# pickle.dump((TestNet,idx_classification),f)
# f.close()


# Test(TestNet,TestSet,idx_classification)