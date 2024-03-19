import translator as tr

t = tr.Translator()


while(True):

    t.printMenu()

    t.loadDictionary("dictionary.txt") #Filename.txt

    txtIn = input()

    # Add input control here!

    if int(txtIn) == 1:
        print("Ok, quale parola devo aggiungere?\n")
        txtIn = input()
        for p in txtIn:
            for c in p.lower():
                if c!=' ' and (c < 'a' or c > 'z'):
                    raise ValueError
        t.handleAdd(txtIn)
        print("Aggiunta")
        txtIn = -1
        pass

    if int(txtIn) == 2:
        print("Ok, quale parola devo tradurre?\n")
        print(f'La traduzione è: {t.handleTranslate(input())}')
        pass

    if int(txtIn) == 3:
        t.handleWildCard(input())
        pass

    if int(txtIn) == 4:
        print(t.diz.__str__())
        break

    if int(txtIn) == 5:
        exit()