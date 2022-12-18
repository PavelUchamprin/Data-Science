

import os, time, re, sys

"""
index will lead from terms to documents that contain the terms and frequency of
the terms in each document. An example is below.
"""
index = {'Ontario': {1: 1},
         'years': {2: 5, 1: 1},
         'Premier': {2: 2, 1: 2},

 }


"""
This function displays the menu as follows
    1. Indexing
    3. Exit
It then prompts the user for a valid input.
Input: None
Output: a valid integer
"""
def printMenu():
    number = int(input(" Enter the number"))
    while number != 1 and number != 3:
        print(" Try again")

    return number


"""
This function takes a text file as input and removes all stop words.
Input: text
Output: text with no stop words
"""
#check every word in the text and remove stopwords
def stopWordRemoval(text):
    txt = text.split()
    text = []
    stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
    for word in txt:
        text = [word for word in txt if word.lower() not in stopwords]
        word = word.strip()
        word = word.strip(word[0])
        text.append(word)
    return text


"""
This function takes a text file as input and removes all punctuations.
Input: text
Output: text with no punctuations
"""
import string
def punctuationsRemoval(text):
    cleanText=[]
    punctuations = '''!()-[]{};:''"\,<>./?@#$%^&*_~'''
    for small in text:
        for word in small:
            if word == "":
                text.remove(word)
            else:
                for letter in word:
                        if letter in punctuations:
                            word = word.replace(letter, "")
                cleanText.append(word)
    return cleanText
"""
This functions takes a clean text as argument,  and appends TermDocFreqFile
 with the list of terms, the  document in which they appear and their frequencies.
 termDocFreqFile format: 3 columns, values separated with space
    Term doc# freq
    Ontario 1 5
    years 1 1
    sugar 1 2

Input: cleanText, and document id
output: termDocFreqFile format: 3 columns, values seperated with space
"""
def appendTermDocFreq(file_count, cleanText, termDocFreqFile):
    #добавить лист в листе в один большой лист и потом считать
    checked = []
    for li in cleanText:
        for p in li:
            if p not in checked:
                checked.append(p)
    for i in range(0, len(checked)):
         termDocFreqFile.write(str(checked[i]) + " " + str(file_count) + " " + str(checked.count(i)) + "\n")




"""""
This function reads termDocFreqFile line by line and append the global index
that go from terms as keys to list of documents that contain them with their frequencies as val.
Appending the index works as follows:
    - for line in termDocFreqFile,
        - if the term does not exist in index,
            add the term as key, the value will be a dictionary containg docid:freq as key:val in index
        - if the term already exists in index, append the val (which is a dictionary) with docid:freq
   input:
       termDocFreqFile
   output:
       fill in the index structure global variable defined in top of the module.

   """
def genIndex(termDocFreqFile):
    pass


"""
This function reads all the text files in the folder 'dataset', appends them to a list,
and returns the list.
Input: None
Output: a list if texts
"""
def readFolderContent():
    final_file_list = []
    files = []
    file_list = os.listdir('C:/Users/Lenovo/.PyCharmCE2018.3/config/scratches/stopwords/dataset/dataset')
    for i in file_list:
        s = int(i[:-4])
        final_file_list.append(s)
    final_file_list = sorted(final_file_list)
    for filename in final_file_list:
        with open('C:/Users/Lenovo/.PyCharmCE2018.3/config/scratches/stopwords/dataset/dataset' + '/' + str(filename) + '.txt', 'r', encoding='utf-8') as infile:
            files.append(infile.read())
    return files

"""
This function creates necessary files needed in this project.
For more information about this function review the flowchart given in the instructions.
"""
def indexing():
    termDocFreqFile = open("TermDocFreq.txt", 'w',encoding='utf-8')

    stopWordsRemoved = []
    puncRemoved = []
    # readFolderContent is called to create a list of files.
    files = readFolderContent()
    file_count=0
    for file in files:
        stopWordsRemoved.append(stopWordRemoval(file))  # Call stopWordRemoval function to remove all stop words.
        puncRemoved.append(punctuationsRemoval(stopWordsRemoved))  # Call punctuationsRemoval function to remove all punctuations
        appendTermDocFreq(file_count,puncRemoved, termDocFreqFile)  # Call appendTermDocFreq function to append to termDocFreqFile
        genIndex(file_count)  # Call genIndex function to append to the global index file
        file_count += 1

def main():
    option=printMenu()
    if option == 1:
        indexing()



if __name__ == "__main__":
       main()