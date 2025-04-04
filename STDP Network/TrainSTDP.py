import torch
import dill as pickle
import os
import subprocess
import uuid
import time
import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from STDPNetwork import Net
# from STDPNetwork import GenerateSTDP, Assign_Hidden_Layer


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
                network.W1_Update(delta_t,spk1)
                network.mem1.zero_()

    network.PlotWeight('Final Weight.png')
    return network

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

def GenerateSTDP(PosLength,NegLength,Ap):
    # Generate STDP window
    
    DelT = torch.linspace(-NegLength,PosLength,NegLength+PosLength+1)
    WUpdate = torch.zeros(PosLength+NegLength+1)
    
    WUpdate[(NegLength):(PosLength + NegLength + 1)] = Ap*torch.linspace(1,0,PosLength+1)

    Window = torch.zeros((2,PosLength + NegLength+1))
    Window[0,:] = DelT
    Window[1,:] = WUpdate
    return Window
    #Note: using causal, weight dependant STDP rule from: "An Optimized Deep Spiking Neural Network Architecture Without Gradients"

def Assign_Hidden_Layer(network,dataset, word_space = 15,test = False):
    #Determine which neuron is assigned to which keyword in the training set.
    #Assignment run
    SpikeData = []
    for i in range(network.num_class):
            data, label = dataset[i]
            data_neuro = torch.zeros((int(data[-1][0])+1+word_space,network.num_inputs))
            for idx in data: 
                data_neuro[int(idx[0]),int(idx[1])] = 1
            SpikeData.append((data_neuro,i))
    if test ==False:
        Recorder = torch.zeros((network.num_class,network.num_class))
        i = 0
        for data,label in SpikeData:
            for t in range(data.shape[0]):
                spk1, mem1 = network.step(data[t,:])
                Recorder[i,:] += spk1.squeeze()
            i +=1

        #Using maximum spike count as a verification tool
        vals, idx_classification = torch.max(Recorder,dim=0) #idx_classification is numerical value of label.
        network.idx_classification = idx_classification
    else:
        conf_matrix = torch.zeros((TestNet.num_class,TestNet.num_class))
        for data,label  in SpikeData:
            output = torch.zeros(network.num_class) #Record output for classification
            network.mem1.zero_()
            for t in range(data.shape[0]):
                spk1, mem1 = network.step(data[t,:])
                output += spk1.squeeze()
            #Determine maximum spike count and corresponding class and update conf matrix
            idx = torch.argmax(output)
            conf_matrix[label,network.idx_classification[idx].item()] += 1

            plt.figure(figsize = (15,10))
            img = sns.heatmap(
                    conf_matrix,annot= True, cmap = "YlGnBu",cbar_kws= {"label":"Scale"}
                )
            plt.xlabel("Predicted Label")
            plt.ylabel("Actual Label")
            plt.savefig('Confusion Matrix.svg') #1st row is correct spikes, 2nd row is incorrect spikes
            plt.close()
        print(torch.sum(torch.diagonal(conf_matrix)))






##### Test Set Verification #####
f = open('./data/Top50Dataset.pckl','rb')
TrainSet = pickle.load(f)
f.close()

#Should we train with our noisy datasets? That might be something we should investigate. Also, I do wonder why we're adding fixed levels of noise for one particular seed,
#surely it's more rigorous to provide code that adds noise independantly. Something to consider.
#TODO: add code that allows dataset to be loaded with appropriate level of noise. Use defined parameters for each level of noise.
#For creating multiple test scripts at once
p = ['None','Low','High']
j = ['None','Low','High']
d = ['None','Low','High']


#timesteps between words:
word_space = 15


#Network parameters
num_channels = 2
num_classes = 50
num_class = 50 #Number of classification neurons

TestNet = Net(num_channels,num_class)
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
epochs = 50



TestNet.PlotWeight('Initial Weights.png')

#Homeostatic regulation parameters
TestNet.Ath = 1e-1
TestNet.Tau_th = TestNet.Ath/num_class/20 #20 is chosen arbitrarily, should represent average number of timesteps for each input.
TestNet.eta = 0.1


TestNet = Train(TestNet,TrainSet,epochs)

#Assign classes to the hidden layer
Assign_Hidden_Layer(TestNet,TrainSet,test = False)

# TestNet.idx_classification = idx_classification

#Re present the training set to the network and calculate classification accuracy

Assign_Hidden_Layer(TestNet,TrainSet, test = True)

#Save network and network assignment
f = open('Network.pckl','wb')
pickle.dump(TestNet,f)
f.close()


#Below code was to submit seperate job script
# for dropout in d:
#     for jitter in j:
#         for poisson in p:
#             dataset_filename = 'Test_Dropout-%s_Jitter-%s_Poisson-%s' %(dropout,jitter,poisson)

#             args = " --network_filename Network.pckl --dataset_filename %s" %(dataset_filename)

#             #Create a shell script so that each test is submitted.
#             bash_script = """#!/bin/bash -l
# #Edit this script to suit your purposes
# #SBATCH --nodes=1
# #SBATCH --ntasks-per-node=1
# #SBATCH --cpus-per-task=5
# #SBATCH --mem=1000G
# #SBATCH --job-name=Test
# #SBATCH --time=50:00:00
# #SBATCH --partition=general
# #SBATCH --account= #CHOOSE
# #SBATCH -o "%s"
# #SBATCH -e "%s"
# #SBATCH --constraint=epyc3
# #SBATCH --batch=epyc3

# python TestSTDP.py%s

# """ %(os.path.join(os.getcwd(), 'out' + dataset_filename+'.txt'),
#         os.path.join(os.getcwd(), 'error' +dataset_filename+'.txt'),
#         args+'.pckl')#This is to edit the above script.


#             myuuid = str(uuid.uuid4())
#             with open(os.path.join(os.getcwd(), "%s.sh" % myuuid), "w+") as f:
#                 f.writelines(bash_script)

#             res = subprocess.run("sbatch %s.sh" % myuuid, capture_output=True, shell=True)
#             print(args)
#             print(res.stdout.decode())
#             os.remove(os.path.join(os.getcwd(), "%s.sh" % myuuid))
#             time.sleep(2)
            

# Test(TestNet,TestSet,idx_classification)
#Have all of the testing done with this script, may need to write a bash script to run them all simultaneously.