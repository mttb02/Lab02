class Dictionary:
    def __init__(self):
        self.tuple = []
        pass

    def addWord(self, pAliena, pItaliana):
        traduzioni = self.translate(pAliena)
        if(traduzioni==None):
            traduzioni = []
        traduzioni.append(pItaliana)
        if len(traduzioni)==1:
            self.tuple.append((pAliena, traduzioni))
        else:
            for t in self.tuple:
                if t[0] == pAliena:
                    t = (pAliena, traduzioni) #Non sono sicuro
        pass

    def translate(self, pAliena):
        for coppia in self.tuple:
            if coppia[0]==pAliena:
                return coppia[1]
        return None
        pass

    def translateWordWildCard(self, pAliena):
        parole = []
        for parola in self.tuple:
            differenze = 100
            if(len(parola[0])==len(pAliena)):
                differenze = 0
                for i in range(0, len(pAliena)-1):
                    if ((parola[0])[i]!=pAliena[i]) and pAliena[i]!='?':
                        differenze+=1
            if(differenze == 0):
                parole.append(parola[1])
        return parole

    def __str__(self):
        stringa = ""
        for tupla in self.tuple:
            stringa += tupla[0]+" "+tupla[1]+'\n'
        return(stringa)

