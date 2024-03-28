from tabulate import tabulate

class OutputFormatter:
    #Step 4 formats and prints the code and tokenized output in a nice format
    def output(self, lines, keywords, literals, operators, identifiers, separators):
        for line in lines:
            print(line)
        print()

        keywords = ', '.join(keywords)
        literals = ', '.join(literals)
        operators = ', '.join(operators)
        identifiers = ', '.join(identifiers)
        separators = ', '.join(separators)

        total_tokens_count = sum([len(keywords.split(', ')), len(literals.split(', ')), len(operators.split(', ')), len(identifiers.split(', ')), len(separators.split(', '))])


        table = [
            ['Keywords', keywords],
            ['Literals', literals],
            ['Operators', operators],
            ['Identifiers', identifiers],
            ['Separators', separators],
            ['Total Tokens', total_tokens_count]
        ]
        print(tabulate(table, headers=['Category', 'Tokens'], tablefmt='fancy_grid'))
        pass