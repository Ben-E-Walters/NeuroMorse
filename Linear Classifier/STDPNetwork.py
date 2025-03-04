import numpy as np
import torch
#From LinClass import Net


##### Test Set Verification #####
#Evaluate network's ability to identify keywords in test set using STDP.
#STDP parameters
NegLength = 15
PosLength = 15
DelT = np.linspace(-NegLength,PosLength,NegLength+PosLength+1)
WUpdate = np.zeros(PosLength+NegLength+1)
Ap = 1
WUpdate[(NegLength):(PosLength + NegLength + 1)] = Ap*np.linspace(1,0,PosLength+1)

Window = np.zeros((2,PosLength + NegLength+1))
Window[0,:] = DelT
Window[1,:] = WUpdate
#Note: using causal, weight dependant STDP rule from: "An Optimized Deep Spiking Neural Network Architecture Without Gradients"


num_channels = 2
num_classes = 50
num_class = 50 #Number of classification neurons

TestNet = Net(num_channels,num_class)
TestNet.STDP = Window
#Lower initial threshold for spiking activity
init_wt = torch.rand_like(TestNet.fc1.weight.detach())
initthresh = torch.ones_like(TestNet.lif1.threshold.detach())
with torch.no_grad():
    TestNet.fc1.weight.copy_(init_wt)
    TestNet.lif1.threshold.copy_(initthresh)

epochs = 50
SpikeData = []

#Convert each dataset to spikes to be fed to network.
#Should create function for this.
for i in range(num_classes):
    data, label = Dataset[i]
    data_neuro = torch.zeros((int(data[-1][0])+1+word_space,num_channels))
    for idx in data: 
        data_neuro[int(idx[0]),int(idx[1])] = 1
    SpikeData.append(data_neuro)

TestNet.PlotWeight('Initial Weights.png')

#Homeostatic regulation parameters
Ath = 1e-1
Tau_th = Ath/num_class/20 #20 is chosen arbitrarily, should represent average number of timesteps for each input.

for epo in range(epochs):
    #Convert each training input into spikes, and append into a list
    a = torch.randperm(num_classes) #For random order
    random.shuffle(SpikeData)

    input_times = torch.zeros(num_channels)
    SpikeStream = torch.cat(SpikeData,0)
    SpikeStream = SpikeStream.to(torch.float)

    TestNet.mem1.zero_()

    for t in range(SpikeStream.shape[0]):
        spk1, mem1 = TestNet.step(SpikeStream[t,:])
        input_times[SpikeStream[t,:]>0] = t

        #Update threshold activity
        with torch.no_grad():
            NewThresh = TestNet.lif1.threshold.detach() - Tau_th + Ath*spk1.squeeze()
            TestNet.lif1.threshold.copy_(NewThresh)

        if torch.sum(spk1)>0:
            delta_t = t - input_times
            TestNet.W1_Update(delta_t,spk1)
            TestNet.mem1.zero_()

TestNet.PlotWeight('Final Weight.png')

#One additional run with no STDP or homeostatic regulation for class assignment.
SpikeData = []


for i in range(num_classes):
    data, label = Dataset[i]
    data_neuro = torch.zeros((int(data[-1][0])+1+word_space,num_channels))
    for idx in data: 
        data_neuro[int(idx[0]),int(idx[1])] = 1
    SpikeData.append(data_neuro)

Recorder = torch.zeros((num_classes,num_class))
i = 0

for data in SpikeData:
    for t in range(data.shape[0]):
        spk1, mem1 = TestNet.step(data[t,:])
        Recorder[i,:] += spk1.squeeze()
    i +=1

#TODO: Run some form of loop to verify for all 27 cases of noise.
#Put the below script into another script file and use test or something like that. Submit seperate batch files each time.

#Using maximum spike count as a verification tool
vals, idx_classification = torch.max(Recorder,dim=0) #idx_classification is numerical value of label.

TestDict = TestSet[1]
TestingEndList = [] #List of list for all end times for each keyword

for key in TestDict.keys():
    TestingEndList.append(TestDict[key][2])

counter = 0
start_time = timeit.default_timer()

#compile spike sequence for test dataset
TestNeuro = torch.zeros((int(TestSet[0][-1][0])+1,num_channels))
for idx in TestSet[0]:
    TestNeuro[int(idx[0]),int(idx[1])] = 1
    counter +=1
    if counter % 10000000 == 0:
        print('Time elapsed: %d, Counter = %d' %(timeit.default_timer() - start_time,counter))

TestTuples = []
correct_spikes = 0
incorrect_spikes = 0

start_time = timeit.default_timer()

#Not technically a confusion matrix, just a measure of correct vs incorrect for each class
conf_matrix = torch.zeros((50,2))

for t in range(TestNeuro.shape[0]):
        spk1, mem1 = TestNet.step(TestNeuro[t,:])
        input_times[TestNeuro[t,:]>0] = t

        if t%10000000 ==0:
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

