import h5py
import pickle
import numpy as np


#Convert dataset to hdf5 format.
Dropout = ['None','Low','High']
Jitter = ['None','Low','High']
Poisson = ['None','Low','High']

#Opening this file for TestDictionary
f = open('../data/Top50Testset.pckl','rb')
TestSet = pickle.load(f)
TestDict = TestSet[1]
f.close()






for d in Dropout:
    for j in Jitter:
        for p in Poisson:

            if (d =='None' )& (j =='None') & (p=='None'):
                name = 'Clean'              
            else:
                name = 'Dropout-%s Jitter-%s Poisson-%s' %(d,j,p)

            ### For Train Dataset ###
            f = open('../data/Train/Train_Dropout-%s_Jitter-%s_Poisson-%s.pckl' %(d,j,p),'rb')
            Dataset = pickle.load(f)
            f.close()

            file = h5py.File('../data/Train/%s.h5' %(name),'w')
            file_test = h5py.File('../data/Test/%s.h5' %(name),'w')

            Spikes = []
            Channels = []
            Labels = []
            #Using format outlined in the paper titled: NEUROMORSE: A TEMPORALLY STRUCTURED DATASET FOR NEUROMORPHIC COMPUTING
            for idx in Dataset:
                TimeList = []
                ChannelList = []
                for event in idx[0]:
                    TimeList.append(event[0])
                    ChannelList.append(event[1])
                Spikes.append(TimeList)
                Channels.append(ChannelList)
                Labels.append(idx[1])

            
            Spike_group = file.create_group('Spikes')
            dt = h5py.vlen_dtype(np.dtype('float64'))
            dt_labels = h5py.string_dtype()

            SpikeDataset = Spike_group.create_dataset('Times',(50,),dtype = dt) 
            ChannelDataset = Spike_group.create_dataset('Channels',(50,),dtype = dt)

            Label_group = file.create_group('Labels')
            LabelDataset = Label_group.create_dataset('Labels',(50,),dtype = dt_labels)

            for i in range(50):
                SpikeDataset[i] = np.array(Spikes[i])
                ChannelDataset[i] = np.array(Channels[i])
                LabelDataset[i] = Labels[i]


            ### For Test Dataset ###
            f = open('../data/Test/Test_Dropout-%s_Jitter-%s_Poisson-%s.pckl' %(d,j,p),'rb')
            TestDataset = pickle.load(f)
            f.close()

            Spike_group = file_test.create_group('Spikes')
            
            dt = h5py.vlen_dtype(np.dtype('float64'))
            dt_labels = h5py.string_dtype()

            TimeDataset = Spike_group.create_dataset('Times',(1,),dtype = dt)
            ChannelDataset = Spike_group.create_dataset('Channels',(1,), dtype = dt)

            dt = h5py.vlen_dtype(np.dtype('float64'))
            dt_labels = h5py.string_dtype()
            Label_group = file_test.create_group('Labels' )
            LabelsDataset = Label_group.create_dataset('Labels',(50,),dtype = dt_labels)
            StartTimesDataset = Label_group.create_dataset('Start Times',(50,),dtype = dt)
            EndTimesDataset = Label_group.create_dataset('End Times',(50,),dtype = dt)

            TimeList = []
            ChannelList = []

            for event in TestDataset[0][0]:
                TimeList.append(event[0])
                ChannelList.append(event[1])
            
            TimeDataset[0] = np.array(TimeList)
            ChannelDataset[0] = np.array(ChannelList)

            for idx,key in enumerate(TestDataset[0][1]):
                LabelsDataset[idx] = key
                StartTimesDataset[idx] = np.array(TestDict[key][1])
                EndTimesDataset[idx] = np.array(TestDict[key][2])



            







                



