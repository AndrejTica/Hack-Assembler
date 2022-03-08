import sys
import parser

def openFile(fileName):
    try:
        if len(sys.argv) == 1:
            return open(fileName)
        else:
            return open(sys.argv[1])
    except FileNotFoundError:
        print("File not found, check the path variable or name")
        exit()

flag=False
def instr(line):
    if line[0]=="@":
        flag=True
        temp=bin(line[1:])
        binary=temp[2:]
        return "0"+binary
    else:
        return "111"

with openFile("assembler.asm") as f:

    while True:
        line=f.readline()
        if "//" in line:
            i= line.find("//")
            line=line[0:i]
        if not line:
            break
        x=instr(line)






