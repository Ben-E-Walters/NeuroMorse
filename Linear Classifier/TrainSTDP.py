import torch
import pickle
import os
import subprocess
import uuid
import time
from LinClass import Net
from STDPNetwork import GenerateSTDP, GenerateTestSpikes, GenerateTrainSpikes, Train, Test, Assign_Hidden_Layer


##### Test Set Verification #####
f = open('Top50Dataset.pckl','rb')
TrainSet = pickle.load(f)
f.close()

#Should we train with our noisy datasets? That might be something we should investigate. Also, I do wonder why we're adding fixed levels of noise for one particular seed,
#surely it's more rigorous to provide code that adds noise independantly. Something to consider.
#TODO: add code that allows dataset to be loaded with appropriate level of noise. Use defined parameters for each level of noise.

p = ['None','Low','High']
j = ['None','Low','High']
d = ['None','Low','High']
#For now, use pckl files for convenience. Think about using h5 files or other code for easy loading.

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

#Training epochs
epochs = 50



TestNet.PlotWeight('Initial Weights.png')

#Homeostatic regulation parameters
TestNet.Ath = 1e-1
TestNet.Tau_th = TestNet.Ath/num_class/20 #20 is chosen arbitrarily, should represent average number of timesteps for each input.
TestNet.eta = 0.1

TestNet = Train(TestNet,TrainSet,epochs)

#Assign classes to the hidden layer
idx_classification = Assign_Hidden_Layer(TestNet,TrainSet)

TestNet.idx_classification = idx_classification

#Save network and network assignment
f = open('Network.pckl','wb')
pickle.dump(TestNet,f)
f.close()


for dropout in d:
    for jitter in j:
        for poisson in p:
            dataset_filename = 'Test_Dropout-%s_Jitter-%s_Poisson-%s.pckl'

            args = " --network_filename Network.pckl --dataset_filename %s" %(dataset_filename)

            #Create a shell script so that each test is submitted.
            bash_script = """#!/bin/bash -l
#Edit this script to suit your purposes
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=5
#SBATCH --mem=1000G
#SBATCH --job-name=Test
#SBATCH --time=50:00:00
#SBATCH --partition=general
#SBATCH --account=a_rahimi
#SBATCH -o "%s"
#SBATCH -e "%s"
#SBATCH --constraint=epyc3
#SBATCH --batch=epyc3


module load anaconda3/2022.05
source /sw/auto/rocky8.6/epyc3/software/Anaconda3/2022.05/etc/profile.d/conda.sh
conda activate myenv
cd /scratch/user/benwalters/Morse Code Dataset/Linear Classifier
python TestSTDP.py%s

""" %(  os.path.join(os.getcwd(), 'out' + dataset_filename+'.txt'),
        os.path.join(os.getcwd(), 'error' +dataset_filename+'.txt'),
        args)#This is to edit the above script.


    myuuid = str(uuid.uuid4())
    with open(os.path.join(os.getcwd(), "%s.sh" % myuuid), "w+") as f:
        f.writelines(bash_script)

    res = subprocess.run("sbatch %s.sh" % myuuid, capture_output=True, shell=True)
    print(args)
    print(res.stdout.decode())
    os.remove(os.path.join(os.getcwd(), "%s.sh" % myuuid))
    time.sleep(2)
            

# Test(TestNet,TestSet,idx_classification)
#Have all of the testing done with this script, may need to write a bash script to run them all simultaneously.