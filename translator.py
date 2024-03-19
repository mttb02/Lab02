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
                if len(riga)==2:
                    self.diz.addWord(riga[0], [riga[1]])

        pass

    def handleAdd(self, entry):
        entry = entry.split(" ")
        traduzioni = []
        for i in range(1, len(entry)):
            traduzioni.append(entry[i])

        for t in traduzioni:
            self.diz.addWord(entry[0], [t])

        pass

    def handleTranslate(self, query):
        return self.diz.translate(query)
        pass

    def handleWildCard(self, query):
        print(f'Le parole sono: {self.diz.translateWordWildCard(query)}')
        pass