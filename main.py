import sys

def openFile(fileName):
    try:
        if len(sys.argv) == 1:
            return open(fileName)
        else:
            return open(sys.argv[1])
    except FileNotFoundError:
        print("File not found, check the path variable or name")
        exit()

f= openFile("assembler.asm")
print(f.name)


