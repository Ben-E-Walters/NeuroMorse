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

#Remove punctuation from corpus (ignoring identifying keywords with punctuation spike sequences for now)
with open('./data/Validation/validation.txt', 'r', encoding='utf8') as f:
    corpus = f.read().lower().split()

# Create a translation table
translator = str.maketrans('', '', string.punctuation)

# Remove punctuation from each word
cleaned_testset = [word.translate(translator) for word in corpus]

# Remove any empty strings resulting from removing punctuation-only words
cleaned_testset = [word for word in cleaned_testset if word]


#Have to create an array of spike times as well as dictionary to identify when keywords occur.
#Dictionary of keyword instances in the test set. key = keyword, value = [num_instances_of_kword, Start_times,End_times]
validation_dict = {'the':[0,[],[]],
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


#Add the num_instances, start_times to test_dict. Create array of spike times for test set by appending to list.
for word in cleaned_testset:
        if word in Top50List:
            validation_dict[word][0] +=1
            validation_dict[word][1].append(time) #Start times
            
        
        for i,ch in enumerate(word):
            if ch in Morse_Spike_Dict:
                Spikes = np.copy(Morse_Spike_Dict[ch])
                Spikes['t'] += time 
                time = Spikes[-1][0]+(1+letter_space)
                list.append(Spikes)
        time += word_space - letter_space #To account for already added letter_space

ValidationArray = np.concatenate(list)

#Append end times to each array
for i in range(50):
    data, label = WordDataset[i]
    validation_dict[label][2] = validation_dict[label][1] +data[-1][0] + word_space

#Save array and test_dictionary in python format. Will convert to HDF5 format.
f = open('./data/Validation/ValidationSet.pckl' ,'wb')
pickle.dump((ValidationArray,validation_dict),f)
f.close()