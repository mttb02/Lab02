from dictionary import Dictionary

class Translator:

    def __init__(self):
        self.diz = Dictionary()
        pass

    def printMenu(self):
        print("------------------------------")
        print("  Transaltor Alien-Italian")
        print("------------------------------")
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcat")
        print("4. Stampa tutto il Dizionario")
        print("5. Exit")
        print("------------------------------")
        pass

    def loadDictionary(self, dict):
        with open(dict, 'r', encoding='utf-8') as f:
            for riga in f:
                riga = (riga.strip('\n')).split(" ")
                if len(riga) == 2:
                    self.diz.addWord(riga[0], [riga[1]])

    def handleAdd(self, entry):
        for t in entry[1:]:
            self.diz.addWord(p_aliena=entry[0], p_italiana=t)

    def handleTranslate(self, query):
        return self.diz.translate(query)

    def handleWildCard(self, query):
        return self.diz.translateWordWildCard(query)