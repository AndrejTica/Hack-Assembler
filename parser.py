class Parser:
    def __init__(self, line):
        self.line=line

    def comp(self):
        flag=False
        flag2=False
        count=0
        c=""
        for i in range(len(self.line)):
            if self.line[i-1]=="=":
                flag=True
            if self.line[i]==";":
                flag2=True
                count=i
            if flag==True:
                if self.line[i]==";":
                    return c.strip()
                c += self.line[i]
            if flag2==True:
                for j in range(count):
                    c+=self.line[j]

                return c.strip()

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
                    return "None!"
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






