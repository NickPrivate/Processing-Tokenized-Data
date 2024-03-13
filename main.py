import keyword
import nltk
from modules.preprocessor import Preprocessor
from modules.file_reader import FileReader
from modules.tokenizer import Tokenizer
# nltk.download('punkt')

def tokenize():

    file =  "input.txt"

    file_reader = FileReader(file)
    lines = file_reader.read_file()


    keywords = []

    keywordList = keyword.kwlist


    preprocessor = Preprocessor()
    processed_lines = preprocessor.preprocess(lines)

    # for line in processed_lines:
    #     print(line)

    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize(processed_lines)


tokenize()