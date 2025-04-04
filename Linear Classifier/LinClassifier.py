import torch
import torch.nn as nn
import snntorch as snn
import numpy as np
import pickle
import random
import matplotlib.pyplot as plt
import timeit
import seaborn as sns
from STDPNetwork import Net

### #Create single neuron network for linear regression ###

f = open('./data/Top50Dataset.pckl','rb') #Obviously need to change based on location of running
Dataset = pickle.load(f)
f.close()

f = open('./data/Top50Testset.pckl','rb')
TestSet = pickle.load(f)
f.close()

num_inputs = 2
num_class = 1
network = Net(num_inputs,num_class)
with torch.no_grad():
    #Set threshold high, only interested in accumulated membrane potential.
    network.lif1.threshold.copy_(10000*torch.ones_like(network.lif1.threshold.detach()))
    
m_values = []
mem_plot = []

word_space = 15
#Find the accumulated membrane potential for each element in the training set.
for i in range(50):
    data,label = Dataset[i]
    data_neuro = torch.zeros((int(data[-1][0])+1+word_space,2))
    network.mem1.zero_()
    for idx in data: 
        data_neuro[int(idx[0]),int(idx[1])] = 1
    
    for j in range(data_neuro.shape[0]):
        spk1, mem1 = network.step(data_neuro[j,:])
        mem_plot.append(mem1)
    m_values.append(network.mem1.item())

# print('Membrane potential values')
# print(m_values)

#Create one-hot encoding for each word:
y= np.zeros((50,50))
for i in range(50):
    y[i,i] = 1


#Perform linear regression. Here we use y = x*Beta, where Beta = (x^T*x)^(-1)*(x^t)*y
x= np.ones((50,2))
x[:,0] = np.array(m_values)

inverse = np.linalg.inv(np.matmul(x.transpose(1,0),x))
beta = np.matmul(np.matmul(inverse,x.transpose(1,0)),y)

#Perform inference with this value of beta
class_results = np.matmul(x,beta)
#Use argmax to determine which label
test = np.argmax(class_results,0,keepdims=True)
print('test')
print(test)
testlist = []
correct = 0
for i in range(50):
    if test[0,i] == i:
        correct+=1
#ALTERNATIVE: Instead of argmax, can use Mean Square Error on class_results with labels y. Yielded similar results.

# for i in range(50):
#     MSE = np.sum(np.square(class_results[i,:] - b),0)
#     idx = np.argmin(MSE)
#     testlist.append(idx)
#     if idx == i:
#         correct+=1
# # print(test)
# print(testlist)
print('Total Correct:{}'.format(correct))



















    



