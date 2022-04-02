class Code:

    def __init__(self, token):
        self.token=token

    __dictC = {
        None: "000",
        "M":  "001",
        "D":  "010",
        "MD": "011",
        "A":  "100",
        "AM": "101",
        "AD": "110",
        "AMD":"111"
    }


    def __switch(self, value, dict):
        return dict.get(value)

    def dest(self):
        return self.__switch(self.token, self.__dictC)




