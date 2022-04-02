import sys
from parser import Parser

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
    if "@" in line:
        #flag=True
        index=line.index("@")
        temp=bin(int(line[index+1:]))
        binary=temp[2:]
        lenght=len(binary)
        dif=15-lenght
        temp1=""
        for x in range(dif):
            temp1+="0"
        binary=temp1+binary
        return "0"+binary
    else:
        return "111"

num_lines=0
with openFile("assembler.asm") as c:
    num_lines = sum(1 for line in c)

with openFile("assembler.asm") as f:
    counter=0
    while True:
        line=f.readline()
        if "//" in line:
            i= line.find("//")
            line=line[0:i]
            flag=True

        x=instr(line)
        if x[0]=="0":
            out=x
            #print(out)
        elif x[0]=="1":
            parser=Parser(line)
            j=parser.jmp()
            c=parser.comp()
            d=parser.dest()

            print(d)
            print(c)
            print(j)

            j=""
            c=""

        counter=counter+1
        if counter==num_lines+1:
            break







