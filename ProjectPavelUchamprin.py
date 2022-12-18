"""""
BDA350- Final Project
(This project is out of 100 marks and is worth 20% of your final grade)
Due date: Wednesday December 8th at Midnight

Student name: Pavel Uchamprin
Student id: 163173198
Date: 08.12.2021

"""""
#Using time library to record time the execution of the code takes.
import time

f = open("adventures_of_huckleberry_finn.txt", "r")

#Turns all words into lowercase words and stores into list
def get_words(data):
    result = []

    for w in data.split():
        word = ""
        for char in w:
            if char.lower() in "abcdefghijklmnopqrstuvwxyz":
                word += char.lower()
        result.append(word)
    return result

#Turns the letters into ascending order and returns the letters in a tuple
def get_key(word):
    key = list(word)
    key.sort()
    return tuple(key)


def print_list(lst):
    print(", ".join(lst))



#count the frequency a word is found in the text
def word_freq(word, words):
    return words.count(word)


start = time.time()
anagrams = {}
words = get_words(f.read())

for word in words:
    key = get_key(word)
    if (key in anagrams):
        anagrams[key].append(word)
    else:
        anagrams[key] = [word]

#Makes a list of unique elements based on the list
def unique_list(lst):
    result = []
    for e in lst:
        if e not in result:
            result.append(e)
    return result

#returns a new list that does not contain the word
def remove_word(word, lst):
    result = []
    for w in lst:
        if w != word:
            result.append(w)
    return result

#FIlling up the dictionary with words
for key in anagrams:
    anagrams[key] = unique_list(anagrams[key])

for key in anagrams:
   if len(anagrams[key]) > 1:
    print(anagrams[key], len(anagrams[key]))

print_stuff = []
#Processing the anagrams, adds the tuple of anagrams and provides the frequency of them as a final output.
for key in anagrams:
    curr = []
    if len(anagrams[key]) < 2:
        continue
    for word in anagrams[key]:
        frequency = word_freq(word, words)
        curr.append(tuple([word] + remove_word(word, anagrams[key]) + [frequency]))
    print_stuff.append(curr)

end = time.time()
print(f"Time spent on this function - getting_anograms: {end - start}, in seconds")


#Returns the list of anagrams corresponding to the given word
def search_anagram(word, anagrams):
    key = get_key(word)
    if key in anagrams:
        return anagrams[key]
    else:
        return []

for t in print_stuff:
    print(t)
#Creates a condition that asks for user's input and search the word in the text file if it has anagram.
while True:
    w = input("\n\nGive me a word or exit(enter): ")
    if w=="exit":
        exit()
    if len(w) == 0:
        break
    a = search_anagram(w, anagrams)
    if len(a) > 0:
        print(f" 'The word exists in the text: {w}. The frequency of the word in the text is: {word_freq(w, words)},",
              end="")
        for word in a:
            if w != word:
                print(
                    f" The anogram of the found word: {word}. The frequency of the anagram word: {word} in text is:", {word_freq(word, words)}, end="")


    else:
        print(f"Word: {w} does not exist")

