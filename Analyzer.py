

class Analyser:

    def __init__(self,intStartingState,intAcceptState,lstRulebook):

        self.currentState = intStartingState
        self.acceptState = intAcceptState
        self.ruleBook = lstRulebook

    def vocabCheck(self, strUserInput):

        vocab = strUserInput

        for i in range(len(vocab)):

            if vocab[i] == 'a':

                print(self.currentState)
                self.currentState = self.ruleBook[0][self.currentState -1]
                print(self.currentState)

            elif vocab[i] == 'b':

                print(self.currentState)
                self.currentState = self.ruleBook[1][self.currentState -1]
                print(self.currentState)

        return True if self.currentState == self.acceptState else False


