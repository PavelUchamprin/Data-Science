"""""""""
Pavel Uchamprin

Student Id: 163173198


"""""""""
import math
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
import string
from nltk.corpus import brown
import nltk

data = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
tags = brown.tagged_words(categories='news')
pos_tags = [val for key, val in tags]

#top 20 most frequent
fd = nltk.FreqDist(pos_tags)
common_tags = fd.most_common(20)
conditions = data.conditions()
#shows all words that present more in plural form than singular
for word in conditions:
    if data[word]['NNS'] > data[word]['NN']:
        print(word)
#it shows which word has the most distinct tag and append it to the list
tags = []
for condition in conditions:
    tags.append((condition, len(data[condition])))
lst = ["information information data train","computer information cpu computer","computer retrieval information"]
i = 0
res = {}

up = []

#gets the list with words that present in all 3 documents
for l in lst:
    l = l.split()
    up += l

up = list(set(up))

print(up)
#TF(t) = (Number of times term t appears in a document) / (Total number of terms in the document).
#this function counts
def cal_freq(d):
    #counts the total amount of the items in each document and counts their frequency which will be stored in dictionary
    r = {}
    N = len(d)
    for i in d:
        if i in r:
            r[i] += 1
        else:
            r[i] = 1
    for key in r.keys():
        r[key] = r[key]/N
    return r
#adds the document to dictionary
for document in lst:
    document = document.split()
    cur_d = cal_freq(document)
    res[i] = cur_d
    i += 1
print(res)

# IDF(t) = log_e(Total number of documents / Number of documents with term t in it).
#uses the list I made with all present words from all documents and the presence of each word in document to find out IDF
idfs = {}
for word in up:
    count = 0
    for doc in lst:
        doc = doc.split()
        if word in doc:
            count += 1
    idfs[word]=math.log(len(lst)/count)
print(idfs)

#cousine similarity
#transfomr the strings to vectors
vect= CountVectorizer().fit_transform(lst)
#turns list into array
vectors= vect.toarray()
#counting similarity vector score
csim=cosine_similarity(vectors)
def cousine_sim_vectors(vec1,vec2):
    #reshaping the array
    vec1=vec1.reshape(1,-1)
    vec2=vec2.reshape(1,-1)
    return cosine_similarity(vec1,vec2)[0][0]
print("d1 and d2: ",cousine_sim_vectors(vectors[0],vectors[1]))
print("d1 and d3: ",cousine_sim_vectors(vectors[0],vectors[2]))
print("d1 and d1: ",cousine_sim_vectors(vectors[0],vectors[0]))


#last taks, it opens the file and cleans it and removes all punctuation and stopwords
li=[]
f = open("corpus5.txt", "r")
stopwords = stopwords.words("english")
for x in f:
    a = x.split()
    if x not in stopwords and x not in string.punctuation:
        li.append(a)