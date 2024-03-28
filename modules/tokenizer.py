import keyword 
import re

class Tokenizer:

    def tokenize(self, lines):
        # for line in lines:
        #     print(line)

        list = keyword.kwlist 
        # print(list)


        delimiter = [':',',',';', ' ', '()']

        operator = ['+', '-', '*', '%', '/', '**', '//', '=', '+=', '-=', '*=', '/=', '%=', '//=', '**=', '&=', '|=', '^=','>>=', '<<=', '==', '!=', '<', '>', '<=', '>=', 'and', 'or', 'not', '<<', '>>','&', 'is', 'not']

        operatorList = []
        keywordList = []
        literalList = []
        identifierList = []
        separatorList = []

        for line in lines:
            words = line.split()
            literal = (re.findall('"([^"]*)"', line))
            for word in words:
                #print("Before: ",word)
                if (word in list and all(word not in lit for lit in literal)):
                    keywordList.append(word)
                #This part (word not in lit for lit in literal) is iterating through the list of literals and checking each one 
                #with word to ensure they aren't literals
                if (word in operator and all(word not in lit for lit in literal)):
                    operatorList.append(word)

                if(word.isidentifier() == True and word not in keyword.kwlist and all(word not in lit for lit in literal)):
                    identifierList.append(word)

                if(word in delimiter and all(word not in lit for lit in literal) and word not in separatorList):
                    separatorList.append(word)

                if (word.isdigit() == True):
                    literalList.append(word)
                #print("After: ",word)
            # inside .finall what it's doing is finding the substrings inside strings that have ""

            #I need to use .extend because adds the specified list elements (or any iterable) to the end of the current list rather
            # than add the entire iterable as a single element to the end of the list.
            literalList.extend(literal)

        return keywordList, literalList, operatorList, identifierList, separatorList

'''import keyword 
import re

class Tokenizer:

    def tokenize(self, lines):
        # for line in lines:
        #     print(line)

        list = keyword.kwlist 
        # print(list)

        operator = ['+', '-', '*', '%', '/', '**', '//', '=', '+=', '-=', '*=', '/=', '%=', '//=', '**=', '&=', '|=', '^=','>>=', '<<=', '==', '!=', '<', '>', '<=', '>=', 'and', 'or', 'not', '<<', '>>','&', 'is', 'not']

        operatorList = []
        keywordList = []
        literalList = []
        identifierList = []

        for line in lines:
            words = line.split()
            literal = (re.findall('"([^"]*)"', line))
            for word in words:
                if (word in list and all(word not in lit for lit in literal)):
                    keywordList.append(word)
                #This part (word not in lit for lit in literal) is iterating through the list of literals and checking each one 
                #with word to ensure they aren't literals
                if (word in operator and all(word not in lit for lit in literal)):
                    operatorList.append(word)

                if(word.isidentifier() == True and all(word not in lit for lit in literal)):
                    identifierList.append(word)

                if (word.isdigit() == True):
                    literalList.append(word)
            # inside .finall what it's doing is finding the substrings inside strings that have ""

            #I need to use .extend because adds the specified list elements (or any iterable) to the end of the current list rather
            # than add the entire iterable as a single element to the end of the list.
            literalList.extend(literal)

        return keywordList, literalList, operatorList, identifierList'''