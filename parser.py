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
        flag=False
        d=""
        for i in range(len(self.line)):
            if self.line[i]=="=":
                flag=True
                break
            if self.line[i]==";":
                if flag==False:
                    return None
                break
            d+=self.line[i]

        return d.strip()


    def jmp(self):
        flag = False
        j = ""
        for i in range(len(self.line)):
            if self.line[i - 1] == ";":
                flag=True
            if flag==True:
                j += self.line[i]
            if self.line[i]==" "and flag==True:
                break

        return j.strip()






