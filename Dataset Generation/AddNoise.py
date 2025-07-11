import numpy as np
import torch
import matplotlib.pyplot as plt
import tonic.functional as functional
import pickle
import timeit
import h5py
#Specify parameters for noise
lowDroprate = 0.25/7.5
highDroprate = 0.5/7.5

lowJitter = 1
highJitter = 2

lowPoisson = 0.05
highPoisson = 0.1

#### Load Data ####

#Open Previous training and testing sets
f = open('./data/TrainDataset.pckl','rb')
TrainDataset = pickle.load(f)
f.close()

f = open('./data/TestDataset.pckl','rb')
TestDataset = pickle.load(f)
f.close()

#### If working with hdf5 files:
# test_a = h5py.File('Morse Code Dataset/Test/Clean.h5','r+')
# train_a = h5py.File('Morse Code Dataset/Train/Clean.h5','r+')

# arr = np.empty(shape = test_a['Spikes']['Times'][0].shape,dtype = [('t','<f4'), ('x','<f4'), ('p', '<f4')])

# arr['t'] = test_a['Spikes']['Times'][0]
# arr['x'] = test_a['Spikes']['Channels'][0]
# arr['p'] = np.ones_like(arr['t'])


# TrainDataset = []
# TestDict = {}
# for i in range(50):
#     train_arr = np.empty(shape = train_a['Spikes']['Times'][i].shape,dtype = [('t','<f4'), ('x','<f4'), ('p', '<f4')])
#     train_arr['t'] = train_a['Spikes']['Times'][i]
#     train_arr['x'] = train_a['Spikes']['Channels'][i]
#     train_arr['p'] = np.ones_like(train_arr['t'])
#     TrainDataset.append((train_arr,train_a['Labels']['Labels'][i]))

#     #Format TestDictionary for Test Dataset
#     label = test_a['Labels']['Labels'][i]
#     word_count = np.shape(test_a['Labels']['Start Times'][0])[0]
#     TestDict[label] = [word_count,test_a['Labels']['Start Times'][i],test_a['Labels']['End Times'][i]]

# TestDataset = (arr,TestDict)
#### End of loading ####



#Different noisy conditions.
DropoutList = ['None','Low','High']
JitterList = ['None','Low','High']
PoissonianList = ['None','Low','High']


np.random.seed(100)

for d in DropoutList:

    if d == 'None':
                Droprate = 0
    elif d == 'Low':
                #Dropout the spikes #Intentionally low rates, as each spike is critically important. Aim for approximately one and two spikes in each input.
                Droprate = lowDroprate 
    elif d == 'High':
                Droprate = highDroprate

    for j in JitterList:

        if j == 'None':
               JitterDev = 0
        elif j == 'Low':
               JitterDev = lowJitter #Standard deviation of just one and two timesteps
        elif j == 'High':
               JitterDev = highJitter


        for p in PoissonianList:
            
            if p =='None':
                   PoissonRate = 0.0
            elif p == 'Low':
                   PoissonRate = lowPoisson #Number of poissonian spikes per timestep. Alternative is to say 1/0.05 = average time between spikes.
            elif p == 'High':
                   PoissonRate = highPoisson

            #### Add noise to training set ###
            NoiseDataset = []
            for data,label in TrainDataset:
                #Calculate Dropout
                ReplacedData = np.delete(data,np.random.random(data.shape)<Droprate)

                #Calculate Jitter
                if JitterDev>0:
                    for x in ReplacedData:
                        #    tNew = x[0] + np.random.randint(-JitterDev,JitterDev) #Use for uniform distribution
                        x[0]+= np.random.normal(0,JitterDev,1)
                        if x[0] < 0:
                            TimeAdd = -x[0]
                        else:
                            TimeAdd = 0
                        x[0] += TimeAdd

                #Calculate amount of Poisson Noise:
                flag = False
                times = np.zeros(2)
                if PoissonRate >0:
                    while flag == False:
                        PoissonTimes = np.random.exponential(1/PoissonRate,2)
                        times += PoissonTimes
                        if times[0] < ReplacedData[-1][0]:
                            ReplacedData = np.insert(ReplacedData,1,(times[0],0,1))
                            
                        if times[1] < ReplacedData[-1][0]:
                            ReplacedData = np.insert(ReplacedData,1,(times[1],1,1))

                        if (times[0] >ReplacedData[-1][0]) & (times[1]>ReplacedData[-1][0]):
                            flag = True

                NoiseDataset.append((np.unique(ReplacedData),label))

            f = open('./data/Train/Train_Dropout-%s_Jitter-%s_Poisson-%s.pckl' %(d,j,p),'wb')
            pickle.dump(NoiseDataset,f)
            f.close()

            ### Add noise to Test Dataset ###
            NoiseDataset = []
            TestData = TestDataset[0] 
            start_time = timeit.default_timer()
            
            #Calculate Dropout
            ReplacedData = np.delete(TestData,np.random.random(TestData.shape)<Droprate)
            

            #Calculate Jitter                        
            if JitterDev>0:
                t_jitter = np.random.normal(0,JitterDev,ReplacedData.__len__())
                ReplacedData['t'] = ReplacedData['t'] + t_jitter
            
            #Calculate amount of Poisson Noise:
            if PoissonRate >0:
                Channel0_Poisson = np.random.exponential(1/PoissonRate,TestData[-1][0].__int__())
                Channel1_Poisson = np.random.exponential(1/PoissonRate,TestData[-1][0].__int__())

                Channel0_times = np.cumsum(Channel0_Poisson)
                Channel1_times = np.cumsum(Channel1_Poisson)

                Channel0_times = Channel0_times[Channel0_times<TestData[-1][0]]
                Channel1_times = Channel1_times[Channel1_times<TestData[-1][0]]

                Channel0_array = np.zeros(Channel0_times.shape[0],dtype = [('t','<f4'),('x','<f4'),('p','<f4')])
                Channel1_array = np.zeros(Channel1_times.shape[0],dtype = [('t','<f4'),('x','<f4'),('p','<f4')])

                Channel0_array['t'] = Channel0_times
                Channel0_array['x'] = 0
                Channel0_array['p'] = 1

                Channel1_array['t'] = Channel1_times
                Channel1_array['x'] = 1
                Channel1_array['p'] = 1


                ReplacedData = np.concatenate((ReplacedData,Channel0_array,Channel1_array))
            #Save dataset
            NoiseDataset.append((np.unique(ReplacedData),TestDataset[1]))
            print('Time Elapsed: %f'%(timeit.default_timer() - start_time))
            f = open('./data/Test/Test_Dropout-%s_Jitter-%s_Poisson-%s.pckl' %(d,j,p),'wb')
            pickle.dump(NoiseDataset,f)
            f.close()


