class StringProcessor:
    def getString(self):
        self.input_string = input("Enter the line: ")

    def printString(self):
        print(self.input_string.upper())


sp = StringProcessor()
sp.getString()
sp.printString()