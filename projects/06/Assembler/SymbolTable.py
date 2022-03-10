class SymbolTable:
    table = {}
    def __init__(self):
        self.addEntry("R0", 0)
        self.addEntry("R1", 1)
        self.addEntry("R2", 2)
        self.addEntry("R3", 3)
        self.addEntry("R4", 4)
        self.addEntry("R5", 5)
        self.addEntry("R6", 6)
        self.addEntry("R7", 7)
        self.addEntry("R8", 8)
        self.addEntry("R9", 9)
        self.addEntry("R10", 10)
        self.addEntry("R11", 11)
        self.addEntry("R12", 12)
        self.addEntry("R13", 13)
        self.addEntry("R14", 14)
        self.addEntry("R15", 15)
        self.addEntry("SCREEN", 16384)
        self.addEntry("KBD", 24576)
        self.addEntry("SP", 0)
        self.addEntry("LCL", 1)
        self.addEntry("ARG", 2)
        self.addEntry("THIS", 3)
        self.addEntry("THAT", 4)

    def addEntry(self, symbol, address):
        self.table[symbol] = address

    def contains(self, symbol):
        return symbol in self.table

    def getAddress(self, symbol):
        return self.table[symbol]