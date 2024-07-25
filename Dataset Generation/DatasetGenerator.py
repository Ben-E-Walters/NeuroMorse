import numpy as np
import matplotlib.pyplot as plt
import tonic.functional as functional
import pickle

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
    for i,ch in enumerate(Morse_Dict[key]):
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

f = open('Top50Dataset.pckl' ,'wb')
pickle.dump(WordDataset,f)
f.close()

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

f = open('corpus.txt','r',encoding="utf8")
time = 0
list = []

for string in f:
    Stringlist = string.lower().split()

    for word in Stringlist:
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

f.close()

#Append end times to each array
for i in range(50):
    data, label = WordDataset[i]
    # a = test_dict[label]
    test_dict[label][2] = test_dict[label][1] +data[-1][0] + word_space

TestArray = np.concatenate(list)

f = open('Top50Testset.pckl' ,'wb')
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
        plotting[row_idx,TestArray[counter][1]+2*j] = 1
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
    
    plotting = np.zeros((data[-1][0]+1,2))
    for i in data: 
        plotting[i[0],i[1]] = 1

    plt.figure()
    plt.imshow(plotting,vmin = 0, vmax = 1)
    plt.title('Spike Sequence for \'%s\'.png' %(label))
    plt.xlabel('Timesteps')
    plt.ylabel('Channel')
    plt.savefig('Spike Sequence for \'%s\'.png' %(label))
    plt.close()






