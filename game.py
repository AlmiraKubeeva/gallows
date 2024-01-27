from word import Word
from field import Field
from gallows import Gallows
class Game:
    def __init__(self):
        self.word = Word()
        self.field = Field(self.word.word)
        self.gallows = Gallows()


    def printGame(self):
        self.field.printField()
        self.gallows.printnumberOfAttempts()

    def startGame(self):
        self.printGame()
        while self.gallows.numberOfAttempts > 0 and not self.field.isFieldFull():
            letter = input()
            if self.word.letterIsFromThisWord(letter):
                indexes = self.word.returnIndexesOfLettersFromWord(letter)
                for index in indexes:
                    self.field.pushLetter(letter, index)
            else:
                self.gallows.setNumberOfAttempts()
            self.printGame()
        if self.gallows.numberOfAttempts == 0:
            print("Проигрыш")
        if self.field.isFieldFull():
            print("Победа!")