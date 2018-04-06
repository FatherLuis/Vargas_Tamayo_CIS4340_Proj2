# Class name: Analyzer
# Class Author: Luis E. Vargas Tamayo
# Purpose of the class: Checks if a given string follows the rules given by the file
# Date: 2/2/2018
# List of changes with dates: none
# Special Notes: none


class Analyser:

    # Method Name: __init__
    # Purpose: Class Constructor
    # Parameter: self, integer, integer, list
    # Method used: none
    # Return Value: none
    # Date:  April 2, 2019
    def __init__(self, intStartingState, intAcceptState, lstRulebook):

        self.currentState = intStartingState
        self.acceptState = intAcceptState
        self.ruleBook = lstRulebook

    # Method Name: __init__
    # Purpose: Class Constructor
    # Parameter: self
    # Method used: none
    # Return Value: none
    # Date:  April 2, 2019
    def vocabCheck(self, strUserInput):

        # Variable holds the value of the parameter
        vocab = strUserInput

        # Iterates through the string
        for i in range(len(vocab)):

            # IF THE STRING AT A GIVEN INDEX IS A, THEN DO CODE
            if vocab[i] == 'a':
                self.currentState = self.ruleBook[0][self.currentState - 1]
            # IF THE STRING AT A GIVEN INDEX IS B, THEN DO CODE
            elif vocab[i] == 'b':
                self.currentState = self.ruleBook[1][self.currentState - 1]
            else:
                # IF THERE IS A LETTER THAT IS NOT A 'A' OR A 'B' THEN THE USER INPUT IS INVALID
                return False

        # RETURNS A BOOLEAN: CHECKS IF THE CURRENT STATE IS EQUAL TO THE ACCEPTED STATE
        return True if self.currentState == self.acceptState else False
