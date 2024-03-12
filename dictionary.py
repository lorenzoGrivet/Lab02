class Dictionary:
    def __init__(self,dizionario):
        self.dizionario=dizionario
        pass

    def addWord(self,parola,traduzione):
        self.dizionario[parola]=traduzione
        pass

    def translate(self,query):
        trad=self.dizionario[query]
        return trad
        pass

    def translateWordWildCard(self,query):
        trad=""
        for a in self.dizionario.keys():
            if len(query)==len(a):
                for i in range(0,len(query)-1):
                    if (query[i]==a[i]) or query[i]==".":
                        trad=a

        return self.dizionario[trad]
        pass

