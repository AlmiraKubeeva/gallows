import random

words = ['кошка', "собака", "колобок", "картина", "человек"]

class Word:
    def __init__(self):
        numOfWord = random.randint(0, len(words) - 1)
        self.word = words[numOfWord]
    
    def letterIsFromThisWord(self, letter):
        if letter in self.word:
            return True
        else:
            return False

    def returnIndexesOfLettersFromWord(self, letter):
        indexes = []
        for i in range(0, len(self.word)):
            if self.word[i] == letter:
                indexes.append(i)
        return indexes

