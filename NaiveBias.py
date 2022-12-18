"""""""""
Pavel Uchamprin
Student id: 163173198
Workshop 5

"""""""""
import os
import nltk
from nltk.corpus import stopwords
import math
import string
import pandas as pd
#this function reads the labeled file
def readlabeledFolderContent(path):
    sents = []
    j = 0
    #opens the file and reading the lines
    file_list = os.listdir(path)
    for filename in sorted(file_list):
        with open(path + '/' + filename, 'r', encoding = 'utf-8') as infile:
            lines = infile.readlines()[1:]
            #adding the lines to the list
            sents.append(lines)
    #removing all stopwords and punctuations from the text and adding the clean text to a new list as a dictionary where keys are labels and values are words belonging to the label
    no_noise=[]
    dic_lab_text=[]
    stop = set(stopwords.words('english'))
    for lis in sents:
        if "#" in lis:
            continue
        for strin in lis:
            moby_tokens = nltk.word_tokenize(strin)
            text_no_stop_words_punct = [t for t in moby_tokens if not (t in stop or t in string.punctuation)]
            no_noise.append(text_no_stop_words_punct)
    for word in no_noise:
        label = word[0]
        words = word[1:]
        cur_dic={label:words}
        dic_lab_text.append(cur_dic)

    return dic_lab_text

labeled = readlabeledFolderContent("C://Users//Lenovo//.PyCharmCE2018.3//config//scratches//PAshaLevWorkshop//labeled_dataset")

#this function reads the unlabeled file
def readunlabeledFolderContent(path):
    sentss = []
    j = 0
    file_list = os.listdir(path)
    for filename in sorted(file_list):
        with open(path + '/' + filename, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()[1:]
            sentss.append(lines)
# removing all stopwords and punctuations from the text and adding the clean text to a new list as a dictionary where keys are labels equal to None and values are words belonging to the label none
    no_noise=[]
    dic_lab_text = []
    stop = set(stopwords.words('english'))
    for lis in sentss:
        for strin in lis:
            moby_tokens = nltk.word_tokenize(strin)
            text_no_stop_words_punct = [t for t in moby_tokens if not (t in stop or t in string.punctuation)]
            no_noise.append(text_no_stop_words_punct)
    for word in  no_noise:
        label = "None"
        words = word[1:]
        cur_dic = {label: words}
        dic_lab_text.append(cur_dic)
    return dic_lab_text

labeled_unlabeled=labeled+readunlabeledFolderContent("C://Users//Lenovo//.PyCharmCE2018.3//config//scratches//PAshaLevWorkshop//unlabeled_dataset")

#
words=[]
for dic in labeled_unlabeled:
    words.append(list(dic.values())[0])


def tf_idf(corpus):

    def cal_freq(d):
        # counts the total amount of the items in each document and counts their frequency which will be stored in dictionary
        r = {}
        N = len(d)
        for i in d:
            if i in r:
                r[i] += 1
            else:
                r[i] = 1
        for key in r.keys():
            r[key] = r[key] / N
        return r
    res={}
    i=0
    # adds the document to dictionary
    for document in corpus:
        cur_d = cal_freq(document)
        res[i] = cur_d
        i += 1
    # IDF(t) = log_e(Total number of documents / Number of documents with term t in it).
    # uses the list I made with all present words from all documents and the presence of each word in document to find out IDF
    up = []

    # gets the list with words that present in all 3 documents
    for l in corpus:
        up += l
    up = list(set(up))

    idfs = {}
    for word in up:
        count = 0
        for doc in corpus:
            if word in doc:
                count += 1
        idfs[word] = math.log(len(corpus) / count)
    #Setting the shape of the matrix which woul dbe filled with the vectrozied values with related labeles
    matrix= [[None]*len(up) for i in range(len(corpus))]
    for i in range(len(corpus)):
        for j in range(len(up)):
            idf = idfs[up[j]]
            tf=res[i].get(up[j],0)
            matrix[i][j]=tf*idf
    return matrix,up

res=tf_idf(words)
label=[]
for dic in labeled_unlabeled:
    label.append(list(dic.keys())[0])
#creating dataframe
column_name=[]
vector,words=res[0],res[1]
column_name= ["label"]+words
data=[]
for i in range(len(label)):
    vector[i].insert(0,label[i])
dataframe=pd.DataFrame(vector,columns=column_name)


train= dataframe.loc[lambda x:(x['label'] != "None")]

#applying naive bayes to the model
from sklearn.naive_bayes import GaussianNB
#training and predicting the testing model
model=GaussianNB()
model.fit(train.iloc[:,1:train.shape[1]],train["label"])
test= dataframe.loc[lambda x:(x['label'] == "None")]
print(model.predict(test.iloc[:,1:test.shape[1]]))

