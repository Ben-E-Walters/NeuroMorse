import numpy as np
import matplotlib.pyplot as plt
import tonic.functional as functional
import pickle
import string

#Create a Morse code dataset.

#Parameters for NeuroMorse
space = 5 #Time between dots and dashes.
letter_space = 10 #Time between letters
word_space = 15 #Time between consecutive words


#Relate characters to Morse code
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





SpikeArray = [] #Array in txp format to be used
SpikeDict = {} #Convert characters into Morse spike sequences




#Create Morse Spike Dictionary
Morse_Spike_Dict = {} #keys = characters, values = spike array (txp format)
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


#List of top 50 words in English language        
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

WordDataset = [] #Each item contains tuple of array and word associated with array
for idx,word in enumerate(Top50List):
    time = 0
    list = []
    for i,ch in enumerate(word):
        Spikes = np.copy(Morse_Spike_Dict[ch])
        Spikes['t'] += time 
        time = Spikes[-1][0]+(1+letter_space)
        list.append(Spikes)

    WholeArray = np.concatenate(list)
    WordDataset.append((WholeArray,word))

#Save training set in easy to use python format. To be converted to HDF5 format.
f = open('../data/Top50Dataset.pckl' ,'wb')
pickle.dump(WordDataset,f)
f.close()

### Test Set ###
#Have to create an array of spike times as well as dictionary to identify when keywords occur.
#Dictionary of keyword instances in the test set. key = keyword, value = [num_instances_of_kword, Start_times,End_times]
test_dict = {'the':[0,[],[]],
             'be':[0,[],[]],
             'to':[0,[],[]],
             'of':[0,[],[]],
             'and':[0,[],[]],
             'a':[0,[],[]],
             'in':[0,[],[]],
             'that':[0,[],[]],
             'have':[0,[],[]],
             'i':[0,[],[]],
             'it':[0,[],[]],
             'for':[0,[],[]],
             'not':[0,[],[]],
             'on':[0,[],[]],
             'with':[0,[],[]],
             'he':[0,[],[]],
             'as':[0,[],[]],
             'you':[0,[],[]],
             'do':[0,[],[]],
             'at':[0,[],[]],
             'this':[0,[],[]],
             'but':[0,[],[]],
             'his':[0,[],[]],
             'by':[0,[],[]],
             'from':[0,[],[]],
             'they':[0,[],[]],
             'we':[0,[],[]],
             'say':[0,[],[]],
             'her':[0,[],[]],
             'she':[0,[],[]],
             'or':[0,[],[]],
             'an':[0,[],[]],
             'will':[0,[],[]],
             'my':[0,[],[]],
             'one':[0,[],[]],
             'all':[0,[],[]],
             'would':[0,[],[]],
             'there':[0,[],[]],
             'their':[0,[],[]],
             'what':[0,[],[]],
             'so':[0,[],[]],
             'up':[0,[],[]],
             'out':[0,[],[]],
             'if':[0,[],[]],
             'about':[0,[],[]],
             'who':[0,[],[]],
             'get':[0,[],[]],
             'which':[0,[],[]],
             'go':[0,[],[]],
             'me':[0,[],[]]}

#Remove punctuation from corpus (ignoring identifying keywords with punctuation spike sequences for now)
with open('../data/corpus.txt', 'r', encoding='utf8') as f:
    corpus = f.read().lower().split()

# Create a translation table
translator = str.maketrans('', '', string.punctuation)

# Remove punctuation from each word
cleaned_testset = [word.translate(translator) for word in corpus]

# Remove any empty strings resulting from removing punctuation-only words
cleaned_testset = [word for word in cleaned_testset if word]


#Add the num_instances, start_times to test_dict. Create array of spike times for test set by appending to list.
for word in cleaned_testset:
        if word in Top50List:
            test_dict[word][0] +=1
            test_dict[word][1].append(time) #Start times
            
        
        for i,ch in enumerate(word):
            if ch in Morse_Spike_Dict:
                Spikes = np.copy(Morse_Spike_Dict[ch])
                Spikes['t'] += time 
                time = Spikes[-1][0]+(1+letter_space)
                list.append(Spikes)
        time += word_space - letter_space #To account for already added letter_space

TestArray = np.concatenate(list)

#Append end times to each array
for i in range(50):
    data, label = WordDataset[i]
    test_dict[label][2] = test_dict[label][1] +data[-1][0] + word_space



#Save array and test_dictionary in python format. Will convert to HDF5 format.
f = open('../data/Top50Testset.pckl' ,'wb')
pickle.dump((TestArray,test_dict),f)
f.close()

#Print counts of keywords in test set.
for key in test_dict.keys():
    print('Word: %s. Number: %i' %(key,test_dict[key][0]))

rows = 50
columns = 50
plotting = np.zeros((rows,2*columns))
counter = 0

#Plot the first 2500 timesteps of the test set.
for j in range(columns):
    time = 0
    
    while time<rows:
        row_idx = TestArray[counter][0]%rows
        plotting[row_idx.__int__(),TestArray[counter][1].__int__()+2*j] = 1
        time += TestArray[counter][0] - j*rows
        counter+=1
plt.figure()
plt.imshow(plotting,vmin = 0,vmax = 1)
plt.title('First 2500 timesteps')
plt.savefig('TestSetRaster.png')
plt.close()


#Plot Examples from training set
for j in range(50):
    
    data,label = WordDataset[j]
    
    plotting = np.zeros((int(data[-1][0])+1,2))
    for i in data: 
        plotting[int(i[0]),int(i[1])] = 1

    plt.figure()
    plt.imshow(plotting,vmin = 0, vmax = 1)
    plt.title('Spike Sequence for \'%s\'.png' %(label))
    plt.xlabel('Timesteps')
    plt.ylabel('Channel')
    plt.savefig('Spike Sequence for \'%s\'.png' %(label))
    plt.close()






