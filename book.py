from functools import reduce

allWords = open("hollow.txt", "r")
plainWords = allWords.read()
listWords = allWords.read().split()

def freqWord(word):
    red = [1 for x in listWords if x == word]
    return reduce( (lambda x,y: x+y), red)

print freqWord("of")

def freqPhrase(phrase):
    red = [1 for x in [plainWords[:-(len(phrase))] if x:x+len(phrase) == phrase]
    return reduce( (lambda x,y: x+y), red)
