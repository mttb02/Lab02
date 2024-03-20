class Dictionary:
    def __init__(self):
        self.tuple = []

    def addWord(self, p_aliena, p_italiana):
        temp_traduzioni = []
        for tupla in self.tuple:
            if tupla[0] == p_aliena:
                tupla[1] += p_italiana
                return
        self.tuple.append([p_aliena, p_italiana])

    def translate(self, paliena):
        traduzioni = None
        for coppia in self.tuple:
            if coppia[0] == paliena:
                traduzioni = coppia[1]
        return traduzioni

    def translateWordWildCard(self, p_aliena):
        parole = []
        for parola in self.tuple:
            if len(parola[0]) == len(p_aliena):
                uguale = True
                counter = 0  # Contatore di "?"
                for i in range(0, len(p_aliena)-1):
                    if parola[0][i] != p_aliena[i]:
                        if p_aliena[i] == '?':
                            counter += 1
                        else:
                            uguale = False
                if uguale and counter == 1:
                    parole += self.translate(parola[0])
        return parole

    def __str__(self):
        temp_stringa = ""
        for tupla in self.tuple:
            temp_stringa += "Alien: "+tupla[0]+" Italien:"
            for i in range(0, len(tupla[1])):
                temp_stringa += " "+tupla[1][i]
            temp_stringa += '\n'
        return temp_stringa

