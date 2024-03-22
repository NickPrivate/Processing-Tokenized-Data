from tabulate import tabulate

class OutputFormatter:
    #Step 4 formats and prints the code and tokenized output in a nice format
    def output(self, lines, keywords, literals, operators, identifiers):
        for line in lines:
            print(line)
        print()

        keywords = ', '.join(keywords)
        literals = ', '.join(literals)
        operators = ', '.join(operators)
        identifiers = ', '.join(identifiers)

        table = [
            ['Keywords', keywords],
            ['Literals', literals],
            ['Operators', operators],
            ['Identifiers', identifiers]
        ]
        print(tabulate(table, headers=['Category', 'Tokens'], tablefmt='fancy_grid'))
        pass