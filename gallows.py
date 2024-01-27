class Gallows:
    def __init__(self):
        self.numberOfAttempts = 6

    def setNumberOfAttempts(self):
        self.numberOfAttempts -= 1

    def printnumberOfAttempts(self):
        print("Number of attempts is", self.numberOfAttempts)