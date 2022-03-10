#!/usr/bin/python

import sys, getopt
from Parser import Parser
from Code import Code
from SymbolTable import SymbolTable

from InstructionType import *

def main(argv):
    inputfile = ''
    outputfile = ''

    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print ("HASM.py -i <inputfile> -o <outputfile>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ("HASM.py -i <inputfile> -o <outputfile>")
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    
    if outputfile == '' and inputfile != '':
        outputfile = inputfile[:inputfile.find(".")] + ".hack"
    print ('Input file is:', inputfile)
    print ('Output file is:', outputfile)

    symTable = SymbolTable()
    scanner = Parser(inputfile)
    labelAddress = 0

    while(scanner.hasMoreLines()):
        scanner.advance()
        if scanner.instructionType() == InstructionType.L_INSTRUCTION:
            label = scanner.symbol()
            symTable.addEntry(label, labelAddress)
            labelAddress -= 1
        labelAddress += 1

    del scanner

    outfile = open(outputfile, 'w')
    parser = Parser(inputfile)
    translator = Code()
    memAddress = 16

    while(parser.hasMoreLines()):
        inst = 0
        parser.advance()
        if parser.instructionType() in [InstructionType.A_INSTRUCTION]:
            if parser.symbol().isdigit():
                inst = str(bin(int(parser.symbol()))[2:]).zfill(16)
            elif (symTable.contains(parser.symbol())):
                inst = str(bin(symTable.getAddress(parser.symbol())))[2:].zfill(16)
            else:
                symTable.addEntry(parser.symbol(), memAddress)
                memAddress += 1
                inst = str(bin(symTable.getAddress(parser.symbol())))[2:].zfill(16)
        elif parser.instructionType() in [InstructionType.C_INSTRUCTION]:
            inst = "111" + translator.comp(parser.comp()) + translator.dest(parser.dest()) + translator.jump(parser.jump())
        if parser.instructionType() not in [InstructionType.L_INSTRUCTION]:
            outfile.writelines(inst + "\n")
    outfile.close()

if __name__ == '__main__':
    main(sys.argv[1:])
