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

with openFile("assembler.asm") as f:

    while True:
        line=f.readline()
        if "//" in line:
            i= line.find("//")
            line=line[0:i]

        if not line:
            break

        print(line.strip())



