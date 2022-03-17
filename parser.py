class Parser:
    def __init__(self, line):
        self.line=line

    def comp(self):
        flag=False
        c=""
        for i in range(len(self.line)):
            if self.line[i]=="=":
                flag=True
            if flag==True:
                c+=self.line[i]
        return c


    def dest(self):
        pass
    def jmp(self):
        pass




