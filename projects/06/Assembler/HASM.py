#!/usr/bin/python

import sys, getopt
from Parser import Parser
from Code import Code

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

    outfile = open(outputfile, 'w')
    parser = Parser(inputfile)
    translator = Code()

    while(parser.hasMoreLines()):
        inst = 5
        parser.advance()
        if parser.instructionType() in [InstructionType.A_INSTRUCTION, InstructionType.L_INSTRUCTION]:
            if parser.symbol().isdigit():
                inst = str(bin(int(parser.symbol()))[2:]).zfill(16)
        else:
            inst = "111" + translator.comp(parser.comp()) + translator.dest(parser.dest()) + translator.jump(parser.jump())
        print (inst)
        outfile.writelines(inst + "\n")
    outfile.close()

if __name__ == '__main__':
    main(sys.argv[1:])
