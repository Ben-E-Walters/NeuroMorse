import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader, TensorDataset
import snntorch as snn
from snntorch import surrogate
import numpy as np
import matplotlib.pyplot as plt
import string

#Create a Morse code dataset.
Morse_Dict = {"a":'.-',
              "b":'-...',
              "c":'-.-.',
              "d":'-..',
              "e":'.',
              "f":'..-.',
              "g":'--.',
              "h":'....',
              "i":'..',
              "j":'.---',
              "k":'-.-',
              "l":'.-..',
              "m":'--',
              "n":'-.',
              "o":'---',
              "p":'.--.',
              "q":'--.-',
              "r":'.-.',
              "s":'...',
              "t":'-',
              "u":'..-',
              "v":'...-',
              "w":'.--',
              "x":'-..-',
              "y":'-.--',
              "z":'--..',
              "1":'.----',
              "2":'..---',
              "3":'...--',
              "4":'....-',
              "5":'.....',
              "6":'-....',
              "7":'--...',
              "8":'---..',
              "9":'----.',
              "0":'-----',
              ".":'.-.-.-',
              ",":'--..--',
              "?":'..--..',
              ":":'---...',
              "'":'.----.',
              "-":'-....-',
              "/":'-..-.',
              "(":'-.--.',
              ")":'-.--.-',
              "\"":'.-..-.',
              "=":'-...-',
              ";":'-.-.-.',
              '$':'...-..-'}


space = 5 #Time between dots and dashes.
letter_space = 10 #Time between letters
word_space = 15 #Time between consecutive words


SpikeArray = []
New_Dataset = []
SpikeDict = {}


#Convert each Morse character into spike array
for key in Morse_Dict.keys():
    time = 0
    b= []
    for i, ch in enumerate(Morse_Dict[key]):
        if ch == '.':
            channel = 0
        elif ch =='-':
            channel = 1
        b.append((time,channel,1))
        time = time+space+1
    SpikeArray = np.array(b,dtype = [('t','<f4'),('x','<f4'),('p','<f4')])
    New_Dataset.append((SpikeArray,key))
    SpikeDict[key] = SpikeArray

#Create Morse Spike Dictionary
Morse_Spike_Dict = {}
for key in Morse_Dict.keys():
    time = 0
    b= []
    for i,ch in enumerate(Morse_Dict[key]):
        if ch == '.':
            channel = 0
        elif ch =='-':
            channel = 1
        b.append((time,channel,1))
        time = time+space+1
    SpikeArray = np.array(b,dtype = [('t','<f4'),('x','<f4'),('p','<f4')])
    Morse_Spike_Dict[key] = SpikeArray

#List of top 50 words        
Top50List = ['the',
             'be',
             'to',
             'of',
             'and',
             'a',
             'in',
             'that',
             'have',
             'i',
             'it',
             'for',
             'not',
             'on',
             'with',
             'he',
             'as',
             'you',
             'do',
             'at',
             'this',
             'but',
             'his',
             'by',
             'from',
             'they',
             'we',
             'say',
             'her',
             'she',
             'or',
             'an',
             'will',
             'my',
             'one',
             'all',
             'would',
             'there',
             'their',
             'what',
             'so',
             'up',
             'out',
             'if',
             'about',
             'who',
             'get',
             'which',
             'go',
             'me']
WordDataset = []

for idx,word in enumerate(Top50List):
    time = 0
    list = []
    for i,ch in enumerate(word):
        Spikes = np.copy(SpikeDict[ch])
        Spikes['t'] += time 
        time = Spikes[-1][0]+(1+letter_space)
        list.append(Spikes)

    WholeArray = np.concatenate(list)
    WordDataset.append((WholeArray,word))


TrainSpikeDataset = []
training_labels = []
num_channels = 2
# Map each word to its index
word_to_index = {word: idx for idx, word in enumerate(Top50List)}

for i in range(50):
    data, label = WordDataset[i]
    training_labels.append(word_to_index.get(label))
    data_neuro = torch.zeros((int(data[-1][0])+1+word_space, num_channels))
    for idx in data: 
        # idx[0] = spike time
        # idx[1] = 0 if dot 1 if dash
        data_neuro[int(idx[0]),int(idx[1])] = 1
    TrainSpikeDataset.append(data_neuro)


# Load a little bit of the corpus (test data)
with open('corpus.txt', 'r', encoding='utf8') as f:
    corpus = f.read().lower().split()

# Select a random subset of words from the corpus
subset_size = 100000  # Adjust this number as needed
# subset_indices = random.sample(range(len(corpus)), subset_size)
test_subset = corpus[0:subset_size]

# Create a translation table
translator = str.maketrans('', '', string.punctuation)

# Remove punctuation from each word
cleaned_test_subset = [word.translate(translator) for word in test_subset]

# Remove any empty strings resulting from removing punctuation-only words
cleaned_test_subset = [word for word in cleaned_test_subset if word]

# Constants (same as in the training script)
num_channels = 2  # Dots and dashes
word_space = 15  # Spacing between words
letter_space = 10  # Spacing between letters

# Map each word to its index or OOV label
word_to_index = {word: idx for idx, word in enumerate(Top50List)}
OOV_label = 50  # Label for OOV words

# Create spike trains for each word in the test subset
TestSpikeDataset = []
test_labels = []

for word in cleaned_test_subset:
    # Initialize spike train data and label
    data = []
    label = word_to_index.get(word, OOV_label)  # Assign label or OOV label
    time = 0

    # Generate spike train for the word
    for ch in word:
        if ch in Morse_Spike_Dict:
            # Retrieve the spike train for the character
            char_spikes = np.copy(Morse_Spike_Dict[ch])

            # Adjust the spike times to account for the current time
            char_spikes['t'] += time

            # Convert to the desired structured array format
            char_spikes_t_x = np.zeros(len(char_spikes), dtype=[('t', '<f4'), ('x', '<f4')])
            char_spikes_t_x['t'] = char_spikes['t']
            char_spikes_t_x['x'] = char_spikes['x']

            # Append the character's spike train to the word's data
            data.extend(char_spikes_t_x)

            # Update time for the next character
            time = char_spikes['t'][-1] + letter_space
        else:
            # Skip characters not in Morse_Spike_Dict
            continue

    # Add spacing for the next word
    if data:
        # Append the word's spike train to the dataset
        data = np.array(data, dtype=[('t', '<f4'), ('x', '<f4')])

        # Create a binary spike train tensor
        max_time = int(data[-1]['t']) + 1 + word_space  # Add word spacing
        data_neuro = torch.zeros((max_time, num_channels))  # Time x Channels

        # Populate the spike train tensor
        for idx in data:
            data_neuro[int(idx['t']), int(idx['x'])] = 1

        # Append the processed word's spike train and label
        TestSpikeDataset.append(data_neuro)
        test_labels.append(label)

# # Find all indices where the label is 50 (OOV)
# oov_indices = [i for i, label in enumerate(test_labels) if label == 50]

# print(f"Total OOV samples available: {len(oov_indices)}")

# # Desired number of OOV samples to add
# desired_oov_samples = 1

# # Check if enough OOV samples are available
# if len(oov_indices) < desired_oov_samples:
#     print(f"Only {len(oov_indices)} OOV samples available. Selecting all available samples.")
#     selected_oov_indices = oov_indices  # Select all available
# else:
#     # Randomly select 10 unique indices
#     selected_oov_indices = random.sample(oov_indices, desired_oov_samples)

# print(f"Selected OOV sample indices: {selected_oov_indices}")

# # Extract spike trains for selected OOV samples
# selected_oov_spike_trains = [TestSpikeDataset[i] for i in selected_oov_indices]

# # Extract labels (all should be 50)
# selected_oov_labels = [test_labels[i] for i in selected_oov_indices]

# # Verify extraction
# print(f"Number of selected OOV spike trains: {len(selected_oov_spike_trains)}")
# print(f"Corresponding labels: {selected_oov_labels}")

# Append OOV spike trains to TrainSpikeDataset
# TrainSpikeDataset += selected_oov_spike_trains
# training_labels += selected_oov_labels


# Determine the maximum length of spike trains
max_length = max(tensor.shape[0] for tensor in TrainSpikeDataset)

# Pad all tensors to max_length
for i in range(len(TrainSpikeDataset)):
    padding = max_length - TrainSpikeDataset[i].shape[0]
    TrainSpikeDataset[i] = F.pad(TrainSpikeDataset[i], (0, 0, 0, padding), mode='constant', value=0)  # Pad at the end

max_length = max(tensor.shape[0] for tensor in TestSpikeDataset)

# Pad all tensors to max_length
for i in range(len(TestSpikeDataset)):
    padding = max_length - TestSpikeDataset[i].shape[0]
    TestSpikeDataset[i] = F.pad(TestSpikeDataset[i], (0, 0, 0, padding), mode='constant', value=0)  # Pad at the end

# Stack all spike train tensors into a single tensor
inputs = torch.stack(TrainSpikeDataset)  # Shape: [num_words, max_length, num_channels]
test_inputs = torch.stack(TestSpikeDataset) 


# Convert labels to a torch tensor
labels = torch.tensor(training_labels)  # Shape: [num_words]
test_labels = torch.tensor(test_labels)

# Create a TensorDataset
dataset = TensorDataset(inputs, labels)
test_dataset = TensorDataset(test_inputs, test_labels)



# Parameters
spike_grad = surrogate.fast_sigmoid(slope=15)
beta = 0.8
num_channels = 2  # Dots and dashes
learning_rate = 1e-3
num_epochs = 2000 #2000

# Create DataLoader
batch_size = 50
train_loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

train_losses = []
test_accuracies = []

# --- Step 2: Define the SNN Model ---
class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(num_channels, 128)  # Input: num_channels, Output: 128
        self.lif1 = snn.Leaky(beta=beta, spike_grad=spike_grad, learn_threshold=True, learn_beta=True)
        self.fc2 = nn.Linear(128, 256)  # Input: 128, Output: 64
        self.lif2 = snn.Leaky(beta=beta, spike_grad=spike_grad, learn_threshold=True, learn_beta=True)
        self.fc3 = nn.Linear(256, 50)  # Output: 50 classes
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

# Training loop
for epoch in range(num_epochs):
    model.train()
    epoch_loss = 0

    for data, target in train_loader:
        optimizer.zero_grad()

        # Forward pass
        outputs = model(data)
        loss = criterion(outputs, target)

        # Backward pass
        loss.backward()
        optimizer.step()

        epoch_loss += loss.item()
    
    print(f"Epoch {epoch+1}/{num_epochs}, Loss: {epoch_loss/len(train_loader):.4f}")

#Here, we should have something for top-5 and top-1 class
# --- Step 4: Evaluation ---
def evaluate_model(loader):
    model.eval()
    correct = 0
    total = 0
    top_5 = 0

    with torch.no_grad():
        for data, target in loader:
            outputs = model(data)
            _, predicted = outputs.max(1)
            total += target.size(0)
            _ , top5predicted = torch.topk(outputs,5,1)
            top_5 += torch.sum(top5predicted== target.unsqueeze(1).repeat(1,5))
            correct += (predicted == target).sum().item()

    accuracy = 100 * correct / total
    top5Accuracy = 100* top_5/total
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"top_5_Accuracy: {top5Accuracy:.2f}%")
    return accuracy

# Evaluate the model on the training set (or validation/test set if available)
accuracy = evaluate_model(train_loader)
print(f"Train accuracy: {accuracy:.2f}%")

test_accuracy = evaluate_model(test_loader)
print(f"Test accuracy: {test_accuracy:.2f}%")
