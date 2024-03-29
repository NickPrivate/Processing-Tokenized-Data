import keyword
import nltk
from modules.preprocessor import Preprocessor
from modules.file_reader import FileReader
from modules.tokenizer import Tokenizer
from modules.output_formatter import OutputFormatter

def output():
    file = "input.txt"
    file_reader = FileReader(file)
    lines = file_reader.read_file()
        
    preprocessor = Preprocessor()
    processed_lines = preprocessor.preprocess(lines)

    tokenizer = Tokenizer()
    keywords, literals, operators, identifiers, separators = tokenizer.tokenize(processed_lines)

    OutputFormatter().output(processed_lines, keywords, literals, operators, identifiers, separators)

output()