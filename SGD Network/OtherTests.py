import tonic
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader, TensorDataset
import snntorch as snn
from snntorch import surrogate
import numpy as np
import matplotlib.pyplot as plt
import string



def LoadDataset(data_name,train = True,n_time_bins = 200):
    match data_name:
        case 'DVS':
            size = 2*128*128
            dataset = tonic.datasets.DVSGesture(save_to=r'C:\Users\benwa\OneDrive\Documents\GitHub\NeuroMorse\Linear Classifier\data',train=train)

            frame_transform = tonic.transforms.Compose([
                tonic.transforms.ToFrame(sensor_size=dataset.sensor_size,n_time_bins=n_time_bins),
                torch.from_numpy,
                FlattenDVSDims

                
                

            ])

            dataset = tonic.datasets.DVSGesture(save_to= r'C:\Users\benwa\OneDrive\Documents\GitHub\NeuroMorse\Linear Classifier\data',transform = frame_transform,train = train)

        case 'ASL':
            dataset = tonic.datasets.ASLDVS(save_to=r'C:\Users\benwa\OneDrive\Documents\GitHub\NeuroMorse\Linear Classifier\data')

            frame_transform = tonic.transforms.Compose([
                tonic.transforms.ToFrame(sensor_size=dataset.sensor_size, n_time_bins = n_time_bins),
                torch.from_numpy,

            ])
            dataset = tonic.datasets.ASLDVS(save_to=r'C:\Users\benwa\OneDrive\Documents\GitHub\NeuroMorse\Linear Classifier\data',transform=frame_transform)
        case 'SHD':
            dataset = tonic.datasets.SHD(save_to=r'C:\Users\benwa\OneDrive\Documents\GitHub\NeuroMorse\Linear Classifier\data', train=train)

            #Below code is the transformation that we want. This gives us spikes where each 0th dimension represents a timestep and the remaining dimensions
            #represent the rest of the spiking data. It will also convert to tensor for us to then implement in spiketorch.
            frame_transform = tonic.transforms.Compose([
                tonic.transforms.ToFrame(sensor_size=dataset.sensor_size, n_time_bins = n_time_bins),
                torch.from_numpy,
                FlattenSHDDims])

            dataset = tonic.datasets.SHD(save_to=r'C:\Users\benwa\OneDrive\Documents\GitHub\NeuroMorse\Linear Classifier\data',transform = frame_transform, train=train)
        
        case 'SSC':
            if train == True:
                split = 'train'
            else:
                split = 'test'
            dataset = tonic.datasets.SSC(save_to=r'C:\Users\benwa\OneDrive\Documents\GitHub\NeuroMorse\Linear Classifier\data',split = split)

            frame_transform = tonic.transforms.Compose([
                tonic.transforms.ToFrame(sensor_size = dataset.sensor_size, n_time_bins = 200),
                torch.from_numpy
            ])
            dataset = tonic.datasets.SSC(save_to=r'C:\Users\benwa\OneDrive\Documents\GitHub\NeuroMorse\Linear Classifier\data',transform= frame_transform, split = split)

    return dataset

#Can replace with classes so that reshaping is easier. 
def FlattenDVSDims(tensor,n_time_bins = 200):
    #Use to flatten the DVS samples (can reshape for others)
    NewTensor = torch.reshape(tensor,(n_time_bins,2*128*128)).to(torch.float)
    return NewTensor

def FlattenSHDDims(tensor,n_time_bins = 200):
    NewTensor = torch.reshape(tensor,(n_time_bins,700)).to(torch.float)
    return NewTensor


#Below is for multilayer network. Adapt, and put into function or class as shown.

#For now, just test script on DVS, and then modify later as needed.

# Parameters
spike_grad = surrogate.fast_sigmoid(slope=15)
beta = 0.8
num_channels = 700  # 700 for SHD, 2*128*128 for DVS
num_classes = 20
learning_rate = 1e-3
num_epochs = 2000

name = 'SHD'
dataset = LoadDataset(data_name=name,train = True,n_time_bins = 200)
test_dataset = LoadDataset(data_name=name,train = False, n_time_bins = 200)

# Create DataLoader
batch_size = 50
train_loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

train_losses = []
test_accuracies = []

# --- Step 2: Define the SNN Model ---
#Need to reinitialise for each dataset due to different output size.
class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(num_channels, 128)  # Input: num_channels, Output: 128
        self.lif1 = snn.Leaky(beta=beta, spike_grad=spike_grad, learn_threshold=True, learn_beta=True)
        self.fc2 = nn.Linear(128, 256)  # Input: 128, Output: 64
        self.lif2 = snn.Leaky(beta=beta, spike_grad=spike_grad, learn_threshold=True, learn_beta=True)
        self.fc3 = nn.Linear(256, num_classes)  # Output: 50 classes
        self.lif3 = snn.Leaky(beta=beta, spike_grad=spike_grad, learn_threshold=True, learn_beta=True)

    def forward(self, x):
        # Initialize hidden states at t=0
        mem1 = self.lif1.init_leaky()
        mem2 = self.lif2.init_leaky()
        mem3 = self.lif3.init_leaky()

        spk1_rec, spk2_rec, spk3_rec = [], [], []

        for t in range(x.size(1)):  # Iterate through time steps
            cur1 = self.fc1(x[:, t, :])  # Linear layer
            spk1, mem1 = self.lif1(cur1, mem1)  # Spiking activation
            spk1_rec.append(spk1)

            cur2 = self.fc2(spk1)  # Linear layer
            spk2, mem2 = self.lif2(cur2, mem2)  # Spiking activation
            spk2_rec.append(spk2)

            cur3 = self.fc3(spk2)  # Linear layer
            spk3, mem3 = self.lif3(cur3, mem3)  # Spiking activation
            spk3_rec.append(spk3)

        spk3_rec = torch.stack(spk3_rec, dim=1)
        return spk3_rec.mean(dim=1)  # Aggregate spikes over time

# Initialize the model
model = Net()

# --- Step 3: Define Training Pipeline ---
criterion = nn.CrossEntropyLoss()  # Loss for classification
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

#Addcomments
# Training loop
for epoch in range(num_epochs):
    model.train()
    epoch_loss = 0

    for data, target in train_loader:
        optimizer.zero_grad()

        #fix later
        target = target.to(torch.long)
        # Forward pass
        outputs = model(data)
        loss = criterion(outputs, target)

        # Backward pass
        loss.backward()
        optimizer.step()

        epoch_loss += loss.item()
    
    print(f"Epoch {epoch+1}/{num_epochs}, Loss: {epoch_loss/len(train_loader):.4f}")

# --- Step 4: Evaluation ---
def evaluate_model(loader):
    model.eval()
    correct = 0
    total = 0

    with torch.no_grad():
        for data, target in loader:
            outputs = model(data)
            _, predicted = outputs.max(1)
            total += target.size(0)
            correct += (predicted == target).sum().item()

    accuracy = 100 * correct / total
    print(f"Accuracy: {accuracy:.2f}%")
    return accuracy

# Evaluate the model on the training set (or validation/test set if available)
accuracy = evaluate_model(train_loader)
print(f"Train accuracy: {accuracy:.2f}%")