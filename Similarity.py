
"""
# 
# Workshop 2
# 
# Student name: Pavel Uchamprin
# 
# Student id: 163173198
#
# 
# """

import random
import nltk
from nltk.corpus import wordnet as wn


def fem_mal_names():
	#calling corpus names which contains males and females names
	names = nltk.corpus.names
	#file id represents list with the names. I access the index 0 in each name, so I count how many female and male names start with every letter compare them
	cfd = nltk.ConditionalFreqDist((fileid,name[0]) for fileid in names.fileids() for name in names.words(fileid))
	cfd.plot()

#This function  finds the 50 most frequently occurring words of a text that are not stopwords
#and Store the n most likely words in a list words, then randomly choose a word from the list using random.choice()
def freq_non_stopwords_and_nth_item(text):
	#return a string only if it is not punctuation
	nopunc = [w for w in text.split() if w.isalpha()]
	#tokenize divides the text on separate strings
	nltk_tokens = nltk.tokenize.word_tokenize(text)
	#it gets all stopwords from nltk corpus
	stopwords = nltk.corpus.stopwords.words('english')
	#applying no punctuation and stopwords in order to avoid extra words
	Cleanedwords= nltk.FreqDist(w.lower() for w in nltk_tokens if w in nopunc and w not in stopwords)
	#using most common command in order to top 50 words
	mostCommon= Cleanedwords.most_common(50)
	print(mostCommon)
	#getting a random word from a most likely words
	random_word=random.choice(mostCommon)
	print("Randomr_word",random_word)

def top_bigrams(text):
	# return a string only if it is not punctuation
	nopunc = [w for w in text.split() if w.isalpha()]
	# tokenize divides the text on separate strings
	nltk_tokens = nltk.word_tokenize(text)
	# it gets all stopwords from nltk corpus
	stopwords = nltk.corpus.stopwords.words('english')
	# applying no punctuation and stopwords in order to avoid extra words
	Cleanedwords= [i for i in nltk_tokens if i not in stopwords and i in nopunc]
	#cleanwords gets divided on separate bigrams
	bigrams = nltk.bigrams(Cleanedwords)
	#putting bigrams into dictionary
	dictionary = nltk.FreqDist(bigrams)
	# using most common command in order to top 50 biagrams
	return print(dictionary.most_common(50))

fem_mal_names()
f= open("warlordofmars.txt","r", encoding = "utf-8")
text = f.read()
freq_non_stopwords_and_nth_item(text)
top_bigrams(text)



#this function scoring similarity between all words
def similarity(word1, word2):
	#using negative infinity in order to find a maximum
	maximum = -float("inf")
	for s1 in wn.synsets(word1):
		for s2 in wn.synsets(word2):
			#comparison of similarity with found similarity
			maximum = max(maximum, s1.path_similarity(s2))
	return maximum

#adding all nouns in the list
listt= ["car-automobile", "gem-jewel", "journey-voyage", "boy-lad", "coast-shore", "asylum-madhouse", "magician-wizard", "midday-noon", "furnace-stove",
	   "food-fruit", "bird-cock", "bird-crane", "tool-implement", "brother-monk", "lad-brother", "crane-implement", "journey-car", "monk-oracle", "cemetery-woodland", "food-rooster",
	   "coast-hill", "forest-graveyard", "shore-woodland", "monk-slave", "coast-forest", "lad-wizard","chord-smile", "glass-magician", "rooster-voyage", "noon-string"]
sort_list=[]
#creating sublists of list with 2 separate words. Example: ["car" , "automobile"].
list_sep = [item.split('-') for item in listt]
#access each word
for item in list_sep:
	word1,word2 = item
	score = similarity(word1,word2)
	#adding all pairs and their similarities score in the list
	sort_list.append((score, word1 + "-" + word2))
# sorting words by their similarity in order of decreasing similarity
sorted_list = sorted(sort_list, key = lambda x : x[0], reverse = True)
print(sorted_list)



