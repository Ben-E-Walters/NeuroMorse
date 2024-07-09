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

start_time = timeit.default_timer()

for d in DropoutList:

    if d == 'None':
                Droprate = 0
    elif d == 'Low':
                #Dropout the spikes
                Droprate = 0.25/7.5 #Average number of spikes is 7.5 in training set.
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
                   PoissonRate = 0
            elif p == 'Low':
                   PoissonRate = 0.05
            elif p == 'High':
                   PoissonRate = 0.1


            NoiseDataset = []
            for data,label in TrainDataset:
                #Calculate Dropout
                ReplacedData = np.delete(data,np.random.random(data.shape)<Droprate)

                #Calculate Jitter, with uniform distribution
                if JitterDev>0:
                    for x in ReplacedData:
                        #    tNew = x[0] + np.random.randint(-JitterDev,JitterDev) #Use for uniform distribution
                        x[0]+= np.random.normal(0,JitterDev,1).round()
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

                # ReplacedData.sort()
                NoiseDataset.append((np.unique(ReplacedData),label))

            f = open('Train_Dropout-%s_Jitter-%s_Poisson-%s.pckl' %(d,j,p),'wb')
            pickle.dump(NoiseDataset,f)
            f.close()

            ### Test Dataset ###
            NoiseDataset = []
            TestData = TestDataset[0] #NOTE: will not adjust start and end times for each element in the training set, as dropout,
            
            #Calculate Dropout
            ReplacedData = np.delete(TestData,np.random.random(TestData.shape)<Droprate)

            #Calculate Jitter
            if JitterDev>0:
                for x in ReplacedData:
                    #    tNew = x[0] + np.random.randint(-JitterDev,JitterDev) #Use for uniform distribution
                    x[0]+= np.random.normal(0,JitterDev,1).round()
                    if x[0] < 0:
                        TimeAdd = -x[0]
                    else:
                        TimeAdd = 0
                    x[0] += TimeAdd

            #Calculate amount of Poisson Noise:
            flag = False
            times = np.zeros(2)
            NewArray = []
            if PoissonRate >0:
                while flag == False:
                    PoissonTimes = np.random.exponential(1/PoissonRate,2)
                    times += PoissonTimes.round()
                    if times[0] < ReplacedData[-1][0]:
                        # ReplacedData = np.insert(ReplacedData,1,(times[0],0,1)) #Very slow
                        NewArray.append((times[0],0,1))
                                                
                    if times[1] < ReplacedData[-1][0]:
                        # ReplacedData = np.insert(ReplacedData,1,(times[1],1,1))
                        NewArray.append((times[1],1,1))

                    if (times[0] >ReplacedData[-1][0]) & (times[1]>ReplacedData[-1][0]):
                        flag = True

            a = ReplacedData.tolist()
            a.extend(NewArray)
            ReplacedData = np.array(a,dtype = [('t','<i4'),('x','<i4'),('p','<i4')] )
            
            NoiseDataset.append((np.unique(ReplacedData),TestDataset[1]))
            f = open('Test_Dropout-%s_Jitter-%s_Poisson-%s.pckl' %(d,j,p),'wb')
            pickle.dump(NoiseDataset,f)
            f.close()

            print('Time:%f' %(timeit.default_timer() - start_time))