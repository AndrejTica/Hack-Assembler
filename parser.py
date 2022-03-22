class Parser:
    def __init__(self, line):
        self.line=line

    def comp(self):
        flag=False
        c=""
        for i in range(len(self.line)):
            if self.line[i-1]=="="or self.line[i-1]==";":
                flag=True
            if flag==True:
                c+=self.line[i]
            if self.line[i]==" "and flag==True:
                break
        return c.strip()


    def dest(self):
        pass
    def jmp(self):
        pass




