from modules.file_reader import FileReader
from modules.preprocessor import Preprocessor
from modules.tokenizer import Tokenizer
from modules.output_formatter import OutputFormatter


def main():
    file_path = 'tests/input.txt'  # Adjust the path as necessary
    
    # Step 1: Read file
    file_reader = FileReader(file_path)
    lines = file_reader.read_file()
    
    # Step 2: Preprocess - remove comments and excess whitespace
    preprocessor = Preprocessor()
    processed_lines = preprocessor.preprocess(lines)
    
    # Future steps: Tokenizing and formatting output
    # tokenizer = Tokenizer()
    # tokens = tokenizer.tokenize(processed_lines)
    
    # output_formatter = OutputFormatter()
    # output_formatter.format(tokens)

    # For now, just print the processed lines to verify
    for line in processed_lines:
        print(line)

if __name__ == "__main__":
    main()