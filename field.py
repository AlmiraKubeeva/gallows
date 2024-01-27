class Field:
    def __init__(self, word):
        self.field = []
        for emptyLetter in range(1, len(word) + 1):
            self.field.append('_')

    def pushLetter(self, letter, index):
        self.field[index] = letter

    def printField(self):
        print(self.field)

    def isFieldFull(self):
        for i in self.field:
            if i == "_":
                return False
        return True
