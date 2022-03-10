from InstructionType import *
import sys

class Parser:
    infile = ''
    line = None

    def __init__(self, infile):
        try:
            self.infile = open(infile, 'r')
        except:
            print ("Bad file name.")
            sys.exit(2)

    def __del__(self):
        print ("Closing file " + str(self.infile))
        self.infile.close()

    def hasMoreLines(self):
        curPos = self.infile.tell()
        hasLine = bool(self.infile.readline())
        self.infile.seek(curPos)
        return hasLine

    def advance(self):
        self.line = self.infile.readline().lstrip().rstrip()
        while self.line == '' or self.line[0] == "/" or self.line == '\n' or self.line == '\r\n':
            self.line = self.infile.readline()
        if self.line.find("/") > -1:
            self.line = self.line[:self.line.find("/")]
        self.line = self.line.lstrip().rstrip()
    
    def instructionType(self):
        if self.line[0] == "@":
            return InstructionType.A_INSTRUCTION
        elif self.line[0] == "(":
            return InstructionType.L_INSTRUCTION
        else:
            return InstructionType.C_INSTRUCTION

    def symbol(self):
        if self.line[0] == "@":
            return self.line[1:].rstrip()
        elif self.line[0] == "(":
            return self.line[1:-1].rstrip()
        return "xxx"

    def dest(self):
        if self.line.find("=") != -1:
            end = self.line.find("=")
            return self.line[:end].rstrip()
        else:
            return None

    def comp(self):
        end = len(self.line)
        begin = 0
        if self.line.find(";") != -1:
            end = self.line.find(";") 
        if self.line.find("=") != -1:
            begin = self.line.find("=") + 1
        return self.line[begin:end].rstrip()

    def jump(self):
        if self.line.find(";") != -1:
            begin = self.line.find(";") + 1
            return self.line[begin:].rstrip()
        else:
            return None