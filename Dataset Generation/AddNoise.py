import numpy as np
import torch
import matplotlib.pyplot as plt
import tonic.functional as functional
import pickle
import timeit



f = open('Top50Dataset.pckl','rb')
TrainDataset = pickle.load(f)
f.close()

f = open('Top50Testset.pckl','rb')
TestDataset = pickle.load(f)
f.close()

DropoutList = ['None','Low','High']
JitterList = ['None','Low','High']
PoissonianList = ['None','Low','High']


np.random.seed(100)

for d in DropoutList:

    if d == 'None':
                Droprate = 0
    elif d == 'Low':
                #Dropout the spikes
                Droprate = 0.25/7.5
    elif d == 'High':
                Droprate = 0.5/7.5

    for j in JitterList:

        if j == 'None':
               JitterDev = 0
        elif j == 'Low':
               JitterDev = 1
        elif j == 'High':
               JitterDev = 2


        for p in PoissonianList:
            
            if p =='None':
                   PoissonRate = 0.0
            elif p == 'Low':
                   PoissonRate = 0.05
            elif p == 'High':
                   PoissonRate = 0.1


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
                        times += PoissonTimes.round()
                        if times[0] < ReplacedData[-1][0]:
                            ReplacedData = np.insert(ReplacedData,1,(times[0],0,1))
                            
                        if times[1] < ReplacedData[-1][0]:
                            ReplacedData = np.insert(ReplacedData,1,(times[1],1,1))

                        if (times[0] >ReplacedData[-1][0]) & (times[1]>ReplacedData[-1][0]):
                            flag = True

                NoiseDataset.append((np.unique(ReplacedData),label))

            f = open('Train_Dropout-%s_Jitter-%s_Poisson-%s.pckl' %(d,j,p),'wb')
            pickle.dump(NoiseDataset,f)
            f.close()

            ### Test Dataset ###
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
                Channel0_Poisson = np.random.exponential(1/PoissonRate,TestData[-1][0])
                Channel1_Poisson = np.random.exponential(1/PoissonRate,TestData[-1][0])

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

            NoiseDataset.append((np.unique(ReplacedData),TestDataset[1]))
            print('Time Elapsed: %f'%(timeit.default_timer() - start_time))
            f = open('Test_Dropout-%s_Jitter-%s_Poisson-%s.pckl' %(d,j,p),'wb')
            pickle.dump(NoiseDataset,f)
            f.close()


