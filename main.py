import translator as tr

t = tr.Translator()
t.loadDictionary("dictionary.txt")  # Filename.txt

esegui = True

while esegui:

    t.printMenu()

    txtIn = input()

    # Add input control here!
    try:
        txtIn = int(txtIn)
        if not 1 <= txtIn <= 5:
            raise ValueError
    except ValueError as ve:
        raise ValueError("Input non ammesso")

    if txtIn == 1:
        print("Ok, quale parola devo aggiungere?")
        tempTraduzione = input()
        tempTraduzione = tempTraduzione.lower().split(" ")
        if len(tempTraduzione) < 2:
            raise ValueError("La traduzione deve essere nel formato:\n <parola aliena> <traduzione1>...")
        else:
            for parola in tempTraduzione:
                for carattere in parola:
                    if carattere < 'a' or carattere > 'z':
                        raise ValueError(f"Carattere non ammesso: {carattere}")
            t.handleAdd(tempTraduzione)
            print("Traduzione aggiunta correttamente")

    if txtIn == 2:
        print("Ok, quale parola devo tradurre?")
        traduzioni = t.handleTranslate(input().lower())
        if traduzioni is None:
            print("La parola non è presente nel dizionario")
        else:
            for traduzione in traduzioni:
                print(f"Una traduzione possibile è: {traduzione}")

    if txtIn == 3:
        print("Ok, quale parola devo cercare?")
        temp_parole = t.handleWildCard(input().lower())
        if len(temp_parole) == 0:
            print("La parola non è presente nel dizionario")
        else:
            for parola in temp_parole:
                print(f"Una traduzione possibile è: {parola}")

    if txtIn == 4:
        print("Dizionario")
        print(t.diz.__str__())

    if txtIn == 5:
        print("Arrivederci!")
        esegui = False

    print("") #riga vuota per dividere