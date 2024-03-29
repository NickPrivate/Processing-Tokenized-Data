import keyword
import re

class Tokenizer:
    def tokenize(self, lines):
        # Step 3 Tokenize the preprocessed lines, set up data for the output
        kwlist = keyword.kwlist

        pattern = r"""
            (?:==|!=|<=|>=|\+\+|--|\+=|-=|\*=|/=|//=|%=|&=|\|=|\^=|>>=|<<=|\*\*=?|&&|\|\||<<|>>|&|\||\^|\+|-|\*|/|%|=|<|>|!|~) | # Operators
            "[^"\\]*(?:\\.[^"\\]*)*" |      # Double quoted string literals
            '[^'\\]*(?:\\.[^'\\]*)*' |      # Single quoted string literals
            \b[a-zA-Z_][a-zA-Z0-9_]*\b |    # Identifiers including keywords
            \d+\.\d+ | \d+ |                # Numeric literals (floats and integers)
            [:;,\(\)]                       # Separators, capture each character separately
        """

        regex = re.compile(pattern, re.VERBOSE)

        operatorList = []
        keywordList = []
        literalList = []
        identifierList = []
        separatorList = []

        for line in lines:
            tokens = regex.findall(line)
            for token in tokens:
                if token in kwlist:
                    keywordList.append(token)
                elif re.match(r"""(?:==|!=|<=|>=|\+\+|--|\+=|-=|\*=|/=|//=|%=|&=|\|=|\^=|>>=|<<=|\*\*=?|&&|\|\||<<|>>|&|\||\^|\+|-|\*|/|%|=|<|>|!|~)""", token):
                    operatorList.append(token)
                elif token in ['(', ')', ':', ',', ';']:
                    separatorList.append(token)
                elif token.startswith(('"', "'")) or token.isdigit():
                    literalList.append(token)
                elif token.isidentifier():
                    identifierList.append(token)

        return keywordList, literalList, operatorList, identifierList, separatorList
