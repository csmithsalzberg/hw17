#Caleb Smith-Salzberg, Shaina Peters
#Team darthCall
#SoftDev2 pd7
#K17 -- Reductio ad Absurdum
#2018-04-30

from functools import reduce

allWords = open("hollow.txt", "r")
plainWords = allWords.read()
listWords = plainWords.split()

def freqPhrase(phrase):
    possibleStr = [plainWords[x:x+len(phrase)] for x in range(len(plainWords)-len(phrase))] #list of all substrings with the desired length
    red = [1 for x in possibleStr if x == phrase] #list with a 1 for each matching substring
    if len(red) > 0:
        return reduce( (lambda x,y: x+y), red) #reduce to the sum of the list
    else:
        return 0

print freqPhrase("the man")


def freqWord(word):
    red = [1 for x in listWords if x == word] #list with a 1 for each appearance of the word
    if len(red) > 0:
        return reduce( (lambda x,y: x+y), red) #reduce to the sum of the list
    else:
        return 0
    
print freqWord("of")


def mostFreqWord():
    uniqueWords = set(listWords) #all the unique words
    red = [freqWord(x) for x in uniqueWords] #list of counts for each word
    return reduce( (lambda x,y: max(x,y) ), red) #reduce to the max entry

print mostFreqWord()

